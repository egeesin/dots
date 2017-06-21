#!/usr/bin/env bash
LRED='\033[1;31m'
LBLU='\033[1;34m'
GRN='\033[0;32m'
ORG='\033[0;33m'
LCYN='\033[0;36m'
WHT='\033[1;37m'
NC='\033[0m'
echo ""
echo -e "         Welcome to"
echo -e "${WHT}  ege's${LBLU}  __ _ _"
echo -e "${LBLU}        / _(_) | ___  ___ "
echo -e "${LBLU}       | |_| | |/ _ \/ __|"
echo -e "${LBLU}      _|  _| | |  __/\__ \ "
echo -e "${LBLU}     (_)_| |_|_|\___||___/"
# Inspired from webpro, mathiasbynens, olzraiti

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
		read -r -p "$1 [$prompt] " REPLY </dev/tty
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
export DOT_DIR DOT_CACHE X_DIR
DOT_DIR="$( cd "$(dirname "${BASH_SOURCE[0]}" )" && pwd )"
DOT_CACHE="$DOT_DIR/.cache.sh"
X_DIR="$HOME/.extra"

# Common functions
. "$DOT_DIR/system/function"

# Update dotfiles itself first
if is-executable git -a -d "$DOT_DIR/.git"; then git --work-tree="$DOT_DIR" --git-dir="$DOT_DIR/.git" pull origin master; fi

# GPG & Pass
if [[ -d "$X_DIR" ]]; then 
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

# GOPATH
export GOPATH="$HOME/.go"
export PATH="$GOPATH/bin:$GOROOT/bin:$PATH"

# Download & install macOS-specific packages
if [[ "$(uname -s)" == "Darwin" ]]; then
	echo ""
	echo -e "${LCYN}█▓▒░░ ${WHT}Installing packages for ${LBLU}macOS${WHT}...\n"
	. "$DOT_DIR/install/brew.sh"
	. "$DOT_DIR/install/gem.sh"
	echo -e "${LCYN}█▓▒░░ ${ORG}Homebrew packages ${NC}-> ${GRN}Done!\n" 

# Download & install Linux-specific packages
elif [[ "$(uname -s)" == "Linux" ]]; then
	echo ""
	echo -e "${LCYN}█▓▒░░ ${WHT}Downloading packages from ${LBLU}Arch repo and AUR${WHT}...\n"

	if is-executable pacaur; then "$DOT_DIR/install/pacaur-setup.sh"; fi

	# Before start the installation, uncomment multilib (for steam, wine) and archlinuxfr just in case
	[[ -d $X_DIR ]] && install -m 644 -o root -g root $X_DIR/mbp11x/etc/pacman.conf -t /etc

	sudo pacman -Syu --noconfirm

	echo -e "${LCYN}█▓▒░░ ${WHT}Installing packages...\n"

	. "$DOT_DIR/install/pac.sh"

	echo -e "${LCYN}█▓▒░░ ${LBLU}Official and AUR packages ${NC}-> ${GRN}Installed!\n" 
fi

# Install npm/pip packages
echo ""

. "$DOT_DIR/install/npm.sh"
. "$DOT_DIR/install/pip.sh"

echo -e "${LCYN}█▓▒░░ ${LRED}Node and Python packages${NC}-> ${GRN}Installed!\n"

# Run tests if bats exists
if is-executable bats; then bats test/*.bats; else echo -e "${WHT}█▓▒░░ ${WHT}Tests ${NC}-> ${WHT}Skipped (bats not found)\n"; fi

echo ""
echo -e "${LCYN}█▓▒░░ ${WHT}Symlinking configuration files...\n"
if [[ "$(ls -1 $DOT_DIR/config/ | wc -l)" == "$(cat $DOT_DIR/symlinks | wc -l)" ]]; then
	# Count configs depending on OS
	[[ "$(uname -s)" == "Darwin" ]] && echo -e "${GRN}█▓▒░░ ${WHT}$(cat $DOT_DIR/symlinks | grep -v '_tux' | wc -l)${NC} files are available to link.\n"
	[[ "$(uname -s)" == "Linux" ]] && echo -e "${GRN}█▓▒░░ ${WHT}$(cat $DOT_DIR/symlinks | grep -v '_mac' | wc -l)${NC} files are available to link.\n"
	. "$DOT_DIR/link.sh"
echo -e "${LCYN}█▓▒░░ ${WHT}Configurations ${NC}-> ${GRN}Linked!\n" 
else
	echo ""
	echo -e "${ORG}ERR: ${WHT}Unspecified configs in dotfiles/symlinks. Please check and update ~/.dotfiles/symlinks"
	echo -e "After installation process, reset machine, open the shell, then type ${LCYN}dot link" 
	echo -e "${WHT}So you can use your favorite CLI tools with your configuration." 
	echo ""
	echo -e "${LRED}█▓▒░░ ${WHT}Configurations ${NC}-> ${ORG}Failed\n" 
fi

# Install extra stuff if X_DIR exists
if [[ -d "$X_DIR" ]] & [[ -f "$X_DIR/install.sh" ]]; then
	echo ""
	echo -e "${WHT}█▓▒░░ Installing extra stuff...\n"
	sudo "$X_DIR/install.sh"
	[[ "$(uname -s)" == "Darwin" ]] && mackup -v restore; echo -e "${LCYN}█▓▒░░ ${WHT}Mackup ${NC}-> ${GRN}Done!\n" 
	echo -e "${LCYN}█▓▒░░ ${WHT}Extra stuff ${NC}-> ${GRN}Installed!\n" 
else
	echo "No .extra directory, skipping."
	echo -e "${WHT}█▓▒░░ ${WHT}Extra stuff ${NC}-> ${WHT}Skipped (Directory not found)\n" 
fi

# Install Zplug
echo ""
echo -e "${LCYN}█▓▒░░ ${WHT}Installing ZPlug...\n"
if is-executable zplug; then curl -sL https://raw.githubusercontent.com/zplug/installer/master/installer.zsh | zsh; fi
echo -e "${LCYN}█▓▒░░ ${WHT}ZPlug ${NC}-> ${GRN}Installed!\n" 

# Questions, questions…
echo ""
echo -e "${LCYN}█▓▒░░ ${WHT}One last step…\n"
if [[ "$(uname -s)" == "Darwin" ]]; then
    if ask "Do you want Music Player Daemon?" Y; then
		brew services start mpd
	fi
	if ask "Do you want Transmission Daemon, BitTorrent client?" Y; then
		brew services start transmission
	fi
	if ask "Do you want to change system defaults and dock placement?" Y; then
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
	if ask "Do you want Music Player Daemon?" Y; then
		systemctl --user enable mpd.service
		systemctl --user start mpd.service
	fi
	if ask "Do you want to change default shell to ZSH?" Y; then
	    chsh -s /bin/zsh
	fi
fi
echo ""
echo -e "${LCYN}█▓▒░░ ${GRN}Dotfiles installation completed.\n" 
echo -e "${NC}If it's your first time you execute install.sh, reboot the machine"
echo -e "to see full progress."
echo -e "If you having issues, want to participate my work, please don't hesitate."
echo -e "${WHT}https://github.com/egeesin/dotfiles/issues" 
echo ""
echo -e "${LCYN}Thanks for trying my dotfiles. *_*" 
