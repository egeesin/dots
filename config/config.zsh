#!/bin/zsh

# If not running interactively, don't do anything
[ -z "$PS1" ] && return

## Auto Completion
setopt extended_glob
zstyle :compinstall filename '/Users/ege/.zshrc'
zstyle ':completion:*:descriptions' format '%U%B%d%b%u'
zstyle ':completion:*:warnings' format '%BSorry, no matches for: %d%b'

zmodload zsh/zpty

# Vi-like Control
bindkey -v
KEYTIMEOUT=1

## Ctrl-P Ctrl-N History
bindkey '^P' history-search-backward
bindkey '^N' history-search-forward
bindkey '\e[A' history-search-backward
bindkey '\e[B' history-search-forward

# if you want red dots to be displayed while waiting for completion
COMPLETION_WAITING_DOTS="true"

## Prompt Setup
set mark-symlinked-directories on
# Show all autocomplete results at once
set page-completions off
# If there are more than 200 possible completions for a word, ask to show them all
set completion-query-items 200
# Show extra file information when completing, like `ls -F` does
set visible-stats on
# Be more intelligent when autocompleting by also looking at the text after
# the cursor. For example, when the current line is "cd ~/src/mozil", and
# the cursor is on the "z", pressing Tab will not autocomplete it to "cd
# ~/src/mozillail", but to "cd ~/src/mozilla". (This is supported by the
# Readline used by Bash 4.)
set skip-completed-text on
# Allow UTF-8 input and output, instead of showing stuff like $'\0123\0456'
set input-meta on
set output-meta on
set convert-meta off

#
# Settings
#

# Resolve DOT_DIR (assuming ~/.dots on distros without readlink and/or $BASH_SOURCE/$0)
READLINK=$(command -v greadlink || command -v readlink)
CURRENT_SCRIPT=$BASH_SOURCE

if [[ -n $CURRENT_SCRIPT && -x "$READLINK" ]]; then
	SCRIPT_PATH=$($READLINK -f "$CURRENT_SCRIPT")
	DOT_DIR=$(dirname "$(dirname "$SCRIPT_PATH")")
elif [ -d "$HOME/.dots" ]; then
	DOT_DIR="$HOME/.dots"
else
	echo "Unable to find dots, exiting."
	return # `exit 1` would quit the shell itself
fi

DOT_CACHE="$DOT_DIR/.cache.sh"
[ -f "$DOT_CACHE" ] && . "$DOT_CACHE"

# Finally we can source the dots (order matters)
for DOTFILE in "$DOT_DIR"/system/{function,function-*,path,env,alias,completion,grep,prompt}; do
	[ -f "$DOTFILE" ] && . "$DOTFILE"
done

if [ "$(uname -s)" = "Darwin" ]; then
	for DOTFILE in "$DOT_DIR"/system/{function,env,alias}_mac; do
		[ -f "$DOTFILE" ] && . "$DOTFILE"
	done
fi

if [ "$(uname -s)" = "Linux" ]; then # Arch Linux, in this case.
	for DOTFILE in "$DOT_DIR"/system/{function,env,alias}_tux; do
		[ -f "$DOTFILE" ] && . "$DOTFILE"
	done
fi

# Clean up
unset READLINK CURRENT_SCRIPT SCRIPT_PATH DOTFILE


[[ "$(uname -s)" = "Darwin" ]] && fpath=(/usr/local/share/zsh-completions $fpath)

# ZPlug
. ~/.zplug/init.zsh

zplug "plugins/git", from:oh-my-zsh
# zplug "marzocchi/zsh-notify"
# zplug "lukechilds/zsh-nvm"
zplug "zsh-users/zsh-completions"
zplug "zsh-users/zsh-syntax-highlighting", defer:2
zplug "lukechilds/zsh-better-npm-completion", defer:2
zplug "mafredri/zsh-async", from:github
# zplug "sindresorhus/pure", use:pure.zsh, from:github, as:theme

if zplug check || zplug install; then
	zplug load
fi

autoload -Uz compinit
compinit

ZSH_THEME=""
autoload -U promptinit; promptinit

# Wise words from little cow
#cowthink -f stegosaurus.cow | lolcat  # some funny stuff.

# Starship Prompt
eval "$(starship init zsh)"

# PyWal
# [[ -e ~/.cache/wal/colors-tty.sh ]] && source ~/.cache/wal/colors-tty.sh


if [[ -z $TMUX && -z $SSH_CONNECTION && -z $DISPLAY && $XDG_VTNR -eq 1 ]]; then
	exec startx
else
	export GPG_TTY
	GPG_TTY=$(tty)
fi

[ -f ~/.fzf.zsh ] && source ~/.fzf.zsh

# [[ "$(uname -s)" == "Linux" ]] && . /usr/share/nvm/init-nvm.sh
# TODO: Check if there is Linux+fnm equivalent of the command above.
unset zle_bracketed_paste
