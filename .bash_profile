############
# .profile #
############

# loading .bashrc #
[[ -f $HOME/.bashrc ]] && . $HOME/.bashrc

# Autorun #
if [[ -z $DISPLAY && $XDG_VTNR -eq 1 ]]; then
	exec startx
fi

export DYLAN=~/dylan
export OPEN_DYLAN_HOME=${DYLAN}/opendylan-2024.1

# PATH #
export PATH=$HOME/.local/bin:$HOME/.cargo/bin:$PATH
export PATH=$PATH:~/Bin:${OPEN_DYLAN_HOME}/bin

# Programs #
export TERM="kitty"
export NAVIGATOR="firefox"
export EDITOR="nvim"

# Clear temp directory #
[[ -d $HOME/tmp ]] && /bin/rm -rf $HOME/tmp/*
