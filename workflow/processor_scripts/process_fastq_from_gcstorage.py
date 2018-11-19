import argparse
import os
import subprocess as sp
import sys
import time


def get_args():
    description = '''Takes a bucket path, searches the directories in the bucket for fastq files, downloads, runs FASTQC
    and cleans up the fastq files to save space.'''
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('-b', '--bucket-path', required=True,
                        help='The bucket address to download fastqs from.')
    parser.add_argument('-wd', '--working-dir', required=True,
                        help='TThe path to perform the tasks in.')
    parser.add_argument('-cwl', '--cwl-script-path', required=True,
                        help='The path to the cwl protocol to be run.')
    parser.add_argument('-sum', '--summariser_script_path', required=True,
                        help='The path to python summariser script.')

    return parser.parse_args()


def _proc_handler(cmd):
    proc = sp.Popen(cmd, shell=True, stdout=sp.PIPE, stderr=sp.STDOUT)
    stdout, stderr = proc.communicate()
    if proc.returncode != 0:
        print(cmd)
        print(stderr)
        print(stdout)
        sys.exit(1)
    else:
        return stdout


def _get_bucket_contents(bucket_path):
    cmd = f'''gsutil ls {bucket_path}'''
    lst = _proc_handler(cmd).decode('utf-8')
    lst = lst.splitlines()
    return lst


def _get_fastq_paths(bucket):
    limit = 5

    while bucket[0][-6:] != '.fq.gz' and bucket[0][-9:] != '.fastq.gz':
        bucket = _get_bucket_contents(bucket[0])
        limit -= 1

        if limit == 0:
            return []

    return [path for path in bucket if path[-6:] == '.fq.gz' or path[-9:] == '.fastq.gz']


def get_fastq_files_from_cloud(bucket_path,):
    fastq_paths = []

    bucket_lst = _get_bucket_contents(bucket_path)
    for bucket in bucket_lst:
        fastq_paths.extend(_get_fastq_paths([bucket]))

    return fastq_paths


class FastQC():
    def __init__(self, working_dir):
        self.wd = working_dir
        self.run_log = os.path.join(self.wd, 'run_log.txt')
        self.processed_log = os.path.join(self.wd, 'files_processed.txt')
        self.failed_log = os.path.join(self.wd, 'failed.txt')

    @classmethod
    def copy_file(cls, remote_path, local_dir):
        filename = remote_path.split('/')[-1]
        local_path = os.path.join(local_dir, filename)

        cmd = f'''gsutil cp {remote_path} {local_path}'''
        _ = _proc_handler(cmd)
        return local_path

    @classmethod
    def run_cwl_pipeline(cls, cwl_file, fastq_path):
        run_cmd = f'''cwl-runner {cwl_file} --fastqFile {fastq_path}'''
        _ = _proc_handler(run_cmd)
        rm_cmd = f'''rm -f {fastq_path}'''
        _ = _proc_handler(rm_cmd)

    def summarise_fastqc_output(self, script_path):
        wd = self.wd
        cmd = f'''python {script_path} -i {wd}'''
        _ = _proc_handler(cmd)

    def _log_progress(self, message):
        with open(self.run_log, 'a') as log:
            log.write(' '.join([message, 'at:', time.ctime()])+'\n')

    def _log_file_completed(self, file):
        with open(self.processed_log, 'a') as log:
            log.write(file + '\n')

    def _log_failed(self, file):
        with open(self.processed_log, 'a') as log:
            log.write(file + '\n')

    def _load_progress(self):
        with open(self.processed_log, 'r') as log:
            for line in log:
                yield line.strip('\n')



    def fastqc_file_handler(self, remote_path, cwl_script_path):
        self._log_progress(' '.join(['Copying of', remote_path, 'starting']))
        local_file_path = self.copy_file(remote_path, self.wd)
        self._log_progress(' '.join(['Copying of', remote_path, 'completed']))
        self._log_progress(' '.join(['Processing of', remote_path, 'starting']))
        self.run_cwl_pipeline(cwl_script_path, local_file_path)
        self._log_progress(' '.join(['Processing of', remote_path, 'completed']))
        self._log_file_completed(remote_path)


def main():
    args = get_args()
    fastq_file_path_list = get_fastq_files_from_cloud(args.bucket_path)
    fq = FastQC(args.working_dir)

    if os.path.isfile(fq.processed_log):
        # A bit of hack to stop having to start from the beginning
        previous = list(fq._load_progress())
        fastq_file_path_list = list(set(fastq_file_path_list) - set(previous))

    print('Beginning analysis.')
    for fastq_path in fastq_file_path_list:
        try:
            fq.fastqc_file_handler(fastq_path, args.cwl_script_path)
        except:
            fq._log_failed(fastq_path)

    print('Beginning summarisation process')
    fq.summarise_fastqc_output(args.summariser_script_path)


if __name__ == '__main__':
    main()
