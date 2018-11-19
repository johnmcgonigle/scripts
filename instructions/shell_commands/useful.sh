## declare an array variable
declare -a arr=("nothingToHarvestRetCode" "harvestedOKRetCode" "serverUnresolvedRetCode" "serverStoppedRetCode" "harvestFailedRetCode" "terminateFailedRetCode" "serverMissingIdsRetCode")

for i in "${arr[@]}"; do
    echo "$i"\n
done

for i in *.fastq.gz; do
	filename=${i%.*}
    echo "$filename"
done

for i in *.fastq.gz; do
	filename=${i%.*}
    zcat "$i" | head -n 160000 > /mnt/data/charles-river/Primary/WXS/mini_fq_Oncotest-2012/${filename}
done

ftp:/­/­ftp.­sra.­ebi.­ac.­uk/­vol1/­fastq/­ERR234/­ERR234329/­ERR234329_1.­fastq.­gz


for i in *.fastq; do
	gzip $i
done

for i in *.fastq.gz; do
	filename=${i%.*}
    zcat "$i" | head -n 1600 > /mnt/data/illumina/Primary/WXS/cut-down/${filename}
done

curl -H "Authorization: Basic cmVwb3NpYm90Om4zcDhtNXAz" https://registry.repositive.io:5000/v2/bwa/tags/list

curl -H "Authorization: Basic cmVwb3NpYm90Om4zcDhtNXAz" https://registry.repositive.io:5000/v2/_catalog