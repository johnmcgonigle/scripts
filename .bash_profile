# .bash_profile

# Get the aliases and functions
if [ -f ~/.bashrc ]; then
	. ~/.bashrc
fi
alias pyver='python -c '"'"'import sys; print(''"''.''"''.join(map(str, sys.version_info[:3])))'"'"''
# alias sapweb='deactivate && source ~/SapWeb/bin/activate && cd /scratch/personal/jmcgonigle/sapientia-web/ && pyver'
# alias sapcli='deactivate && source ~/SapCli/bin/activate && cd /scratch/personal/jmcgonigle/sapientia-client/ && pyver'
# alias repo=' cd /scratch/personal/jmcgonigle/sapientia-web'

## Git commands
alias add='git add '
alias st='git status'
alias co='git co -m '
alias gdev='git co dev'
alias rebase='git pull --rebase'
alias commit=' git commit -m '
alias prev=' git commit --amend'
alias sq=" git commit -m 'squash'"

# Bash commands
alias ls="ls -G"
alias l='ls -Fhtlr'
alias lsj=' ls -lhra'
alias szj='du -ha'
alias sztot='du -hs'
alias les=' less -S'
alias tma=' tmux attach -t '
alias tmls=' tmux ls '
# alias bsubmit='deactivate && cd ~/scripts/bsubs/'

#Tmux commands
alias tmn=' tmux new -s '
alias tmk=' tmux kill-session -t '

# alias staging='PGPASSWORD=Orange18a psql -h staging-db.sapientia.co.uk -U postgres sapientia '
# alias grch38='PGPASSWORD=somesecret psql -h 10.10.1.65 -U postgres sapientia_grch38 '
# alias dbread='PGPASSWORD=tatws63cabets psql -h staging-db.sapientia.co.uk -U readonly sapientia'
# alias dkr='docker run -v /scratch:/scratch -v ~/sapientia-web:/app --rm -t -i 144563655722.dkr.ecr.eu-west-1.amazonaws.com/congenica/pipeline:latest'
# alias ts='docker run --rm -ti -v $DANCER_APPDIR:/app -e DANCER_APPDIR=$DANCER_APPDIR -e DANCER_ENVIRONMENT=staging -v /scratch/data:/data -v /scratch/projects:/scratch/projects -v /scratch/personal:/scratch/personal -v /efs:/efs --entrypoint /bin/bash congenica/pipeline:latest'


function cdmod()
 {
     function cdscr()
     { 
       scripts_dir=$(echo "cd ${HOME}/git/scripts/")
       $scripts_dir
       ls -lh
     }
     function cdst()
     { 
       work_dir=$(echo "cd ${HOME}/work_dir")
       $work_dir
       ls -lh
     }

     function cdgit()
     { 
       git_dir=$(echo "cd ${HOME}/git")
       $git_dir
       ls -lh
     }

     function cdsw()
     { 
       sw=$(echo "cd ${HOME}/sw")
       $sw
       ls -lh
     }

     function cdtun()
     { 
       seq_dir=$(echo "cd ${HOME}/.ssh")
       $seq_dir
       ls -lh
     }
 }
cdmod

source ~/git/.git-completion.bash
source ~/BaseDev/bin/activate