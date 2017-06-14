#!/usr/bin/env bash
LRED='\033[1;31m'
LBLU='\033[1;34m'
GRN='\033[0;32m'
ORG='\033[0;33m'
LCYN='\033[0;36m'
WHT='\033[1;37m'
NC='\033[0m'
echo -e "         Welcome to"
echo ""
echo -e "${WHT}  ege's${LBLU}  __ _ _"
echo -e "${LBLU}        / _(_) | ___  ___ "
echo -e "${LBLU}       | |_| | |/ _ \/ __|"
echo -e "${LBLU}      _|  _| | |  __/\__ \ "
echo -e "${LBLU}     (_)_| |_|_|\___||___/"
# Inspired from webpro/dotfiles & olzraiti/dotfiles

ask() {
	while true; do
		if [ "${2:-}" = "Y" ]; then
			prompt="Y/n"
			default=Y
		elif [ "${2:-}" = "N" ]; then
			prompt="y/N"
			default=N
		else
			prompt="y/n"
			default=
		fi
		read -p "$1 [$prompt] " REPLY </dev/tty
		if [ -z "$REPLY" ]; then
			REPLY=$default
		fi
		case "$REPLY" in
			Y*|y*) return 0 ;;
			N*|n*) return 1 ;;
		esac
	done
}
# Directory variables
export DOT_DIR X_DIR
DOT_DIR="$( cd "$(dirname "${BASH_SOURCE[0]}" )" && pwd )"
X_DIR="$HOME/.extra"

# Update dotfiles itself first
[ -d "$DOT_DIR/.git" ] && git --work-tree="$DOT_DIR" --git-dir="$DOT_DIR/.git" pull origin master

# GPG & Pass
if [ -d $X_DIR ]; then 
	export GNUPGHOME="$X_DIR/secret/gnupg"
	export PASSWORD_STORE_DIR="$X_DIR/secret/pass"
fi

# Bunch of symlinks
echo ""
echo -e "${LCYN}█▓▒░░ ${WHT}Symlinking shell and git configurations…\n"
ln -sfv "$DOT_DIR/runcom/zshrc" ~/.zshrc
ln -sfv "$DOT_DIR/runcom/gemrc" ~/.gemrc
ln -sfv "$DOT_DIR/git/gitconfig" ~/.gitconfig
ln -sfv "$DOT_DIR/git/gitignore-global" ~/.gitignore_global

# Download & install macOS-specific packages
if [[ "$(uname -s)" == "Darwin" ]]; then
	echo ""
	echo -e "${LCYN}█▓▒░░ ${WHT}Installing packages for ${LBLU}macOS${WHT}…\n"
	export PATH="/usr/local/bin:$PATH"
	command -v brew > /dev/null 2&>1 || ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
	brew doctor
	brew update
	brew upgrade

	brew bundle --file=$DOT_DIR/install/Brewfile
	# Just in case doesn't work,
	#. "$DOT_DIR/etc/brew.sh"
	#. "$DOT_DIR/etc/cask.sh"

	. "$DOT_DIR/install/gem.sh"
	echo -e "${LCYN}█▓▒░░ ${ORG}brew ${WHT}-> ${GRN}✔\n" 


# Download & install Linux-specific packages
elif [[ "$(uname -s)" == "Linux" ]]; then
	echo ""
	echo -e "${LCYN}█▓▒░░ ${WHT}Downloading packages from ${LBLU}Arch repo and AUR${WHT}…\n"

	[[ ! -x "pacaur" ]] && $DOT_DIR/install/pacaur-setup.sh

	# multilib needs to activated before this lines!
	sudo pacman -Syu --noconfirm

	echo -e "${LCYN}█▓▒░░ ${WHT}Installing packages…\n"

	. "$DOT_DIR/install/pac.sh"

	echo -e "${LCYN}█▓▒░░ ${LBLU}pacman/pacaur ${NC}-> ${GRN}Done!\n" 
fi

# Install npm/pip packages
echo ""
echo -e "${LCYN}█▓▒░░ ${WHT}Installing ${LRED}npm/pip ${WHT}packages…\n"

. "$DOT_DIR/install/npm.sh"
. "$DOT_DIR/install/pip.sh"

echo -e "${LCYN}█▓▒░░ ${LRED}npm/pip ${NC}-> ${GRN}Done!\n"

# Run tests
bats $DOT_DIR"/test/*.bats"

echo ""
echo -e "${LCYN}█▓▒░░ ${WHT}Symlinking configuration files…\n"
. "$DOT_DIR/link.sh"
echo -e "${LCYN}█▓▒░░ ${WHT}Configurations ${NC}-> ${GRN}Done!\n" 

# Install extra stuff if X_DIR exists
if [ -d "$X_DIR" -a -f "$X_DIR/install.sh" ]; then
	echo ""
	echo -e "${WHT}█▓▒░░ Installing extra stuff…\n"
	sudo $X_DIR/install.sh
	echo -e "${LCYN}█▓▒░░ ${WHT}Extra stuff ${NC}-> ${GRN}Done!\n" 
fi

# Install Zplug
echo ""
echo -e "${LCYN}█▓▒░░ ${WHT}Installing Zplug…\n"
[[ ! -x "zplug" ]] && curl -sL https://raw.githubusercontent.com/zplug/installer/master/installer.zsh | zsh
echo -e "${LCYN}█▓▒░░ ${WHT}Zplug ${NC}-> ${GRN}Done!\n" 

# Questions, questions…
echo ""
echo -e "${LCYN}█▓▒░░ ${WHT}One last step…\n"
if [[ "$(uname -s)" == "Darwin" ]]; then
    if ask "Do you want to set MPD?" Y; then
		brew services start mpd
	fi
	if ask "Do you want to set Transmission Daemon?" Y; then
		brew services start transmission
	fi
	if ask "Do you want to change macOS settings & dock?" Y; then
        mkdir -p ~/Pictures/Screenshots
		. "$DOT_DIR/macos/defaults.sh"
		. "$DOT_DIR/macos/defaults-chrome.sh"
		. "$DOT_DIR/macos/dock.sh"
	fi
	if ask "Do you want to change default shell to ZSH?" Y; then
	    chsh -s /bin/zsh
	fi
	chmod go-w '/usr/local/share'
elif [[ "$(uname -s)" == "Linux" ]]; then
    if ask "Do you want to enable and start Music Player Daemon?" Y; then
		systemctl --user enable mpd.service
		systemctl --user start mpd.service
	fi
	if ask "Do you want to change default shell to ZSH?" Y; then
	    chsh -s /bin/zsh
	fi
fi
echo -e "${LCYN}█▓▒░░ ${GRN}Dotfiles installation completed.\n" 
echo ""
echo -e "If it's your first time you execute install.sh, reboot the machine to see full progress."
echo -e "If you having issues, want to participate my work, please don't hesitate. https://github.com/egeesin/dotfiles/issues" 
echo ""
echo -e "Thanks for trying my dotfiles. *-*" 
