#!/bin/zsh
# ^ In macOS Catalina, the shell must change to Z Shell and must be tested in Arch Linux.
DOT_DIR="$( cd "$(dirname "${BASH_SOURCE[0]}" )" && pwd )"

# shellcheck source=system/env
. "$DOT_DIR/system/env" # $currentos, $archbits, $DOT_DIR $X_DIR etc.
# shellcheck source=system/function
. "$DOT_DIR/system/function" # is_executable, ask, print_platform etc.
# shellcheck source=system/path
. "$DOT_DIR/system/path" # Homebrew cellar paths

# LRED='\033[1;31m'
LBLU='\033[1;34m'
GRN='\034[0;32m'
# ORG='\033[0;33m'
LCYN='\033[0;36m'
WHT='\033[1;37m'
NC='\033[0m'

#————————[0] Intro
#
echo -e "${LBLU}"
echo '          88'
echo '          88              ,d'
echo '          88              88'
echo '  ,adPPYb,88  ,adP8Yba, MM88MMM ,adPPYba,'
echo ' a8"    `Y88 a888888888a  88    I8[    ""'
echo ' 8b       88 88888888888  88     `"Y8ba,'
echo ' "8a,   ,d88 "888888888"  88,   aa    ]8I'
echo '  `"8bbdP"Y8  `"Yb8dP"    "Y888 `"YbbdP"'
echo -e "${NC}"
print_platform

#————————[1] Preparation
#
if is_executable git && [ -d "$DOT_DIR/.git" ]; then
	echo
	echo -e "${LCYN}▓▒░ ${WHT}Checking updates from GitHub...${NC}"
	git --work-tree="$DOT_DIR" --git-dir="$DOT_DIR/.git" pull origin master;
fi

#————————[2] Install Package Bundles
#
echo
if ask "> Install package bundles?" Y; then

#——— For every OS
	# shellcheck source=setup/nodejs.sh
	. "$DOT_DIR/setup/nodejs.sh"
	# shellcheck source=setup/pip.sh
	. "$DOT_DIR/setup/pip.sh"
	# shellcheck source=setup/git.sh
	. "$DOT_DIR/setup/git.sh"

#——— For macOS
	if [[ $currentos = "Darwin" ]]; then
		# shellcheck source=mac/brew.sh
		. "$DOT_DIR/mac/brew.sh"
		# shellcheck source=mac/gem.sh
		. "$DOT_DIR/mac/gem.sh"

#——— For Arch Linux
	elif [[ $currentos == "Arch Linux" ]]; then
		# shellcheck source=tux/arch.sh
		. "$DOT_DIR/tux/arch.sh"

#——— For NixOS
	elif [ -n "$(grep -i nixos < /etc/os-release)" ]; then
		echo "Verified this is NixOS."
		echo "-----"
	fi

#——— For WSL
	# if grep -qE "(Microsoft|WSL)" /proc/version

	# fi
fi

#————————[3] Symlink All Configs
#
if ask "> Symlink all configurations?" Y; then
	echo
	# shellcheck source=./link.sh
	. "$DOT_DIR/link.sh"
fi

#————————[4] ~/.extra
#
if [[ -d "$X_DIR" ]]; then
	if ask "> ~/.extra found, install it?" N; then
		X_CHOSEN=1
		. "$X_DIR/install.sh"
	fi
# else
# 	echo "▓▒░ No .extra directory found. Skipping."
fi

#————————[5] Post Installation
#
echo
echo -e "${LCYN}▓▒░ ${WHT}Daemon Questions...${NC}"

if [[ $currentos = "Darwin" ]]; then

	if ask "> Enable Music Player Daemon)" N; then
		brew services start mpd
		echo "█▓▒░░ mpd enabled!"
	fi

	# if ask "> Enable and start Transmission daemon, BitTorrent client?" Y; then
	# 	brew services start transmission-cli
	# 	echo "█▓▒░░ Transmission enabled!"
	# fi

	# if ask "Enable Yabai, tiling window manager and skhd? (Recommended if you're fine with bspwm, i3wm)" N; then
	# 	echo "In order to Yabai and skhd to work, System Integrity Protection must disabled.
	# 	brew services start yabai
	# 	brew services start skhd
	# fi

	if ask "> Rewrite macOS settings and set apps to dock?" N; then
		# shellcheck source=mac/defaults.sh
		. "$DOT_DIR/mac/defaults.sh"

		# Reset Launchpad
		defaults write com.apple.dock ResetLaunchPad -bool true

		# shellcheck source=mac/dock-bootstrap.sh
		. "$DOT_DIR/mac/dock-bootstrap.sh"
		. "$DOT_DIR/mac/dock/_general.sh"
	fi

	chmod go-w '/usr/local/share'

elif [[ $currentos == "Arch Linux" ]]; then
	if ask "> Enable Music Player Daemon?" Y; then
		systemctl --user enable mpd.service
		systemctl --user start mpd.service
		echo "█▓▒░░ mpd enabled!"
	fi
fi

if ask "> Set Z Shell as default shell and install ZPlug?" Y; then
	# if ! is_executable zplug; then
	echo
	echo -e "${LCYN}▓▒░ ${WHT}Installing ZPlug...${NC}"
	curl -sL https://raw.githubusercontent.com/zplug/installer/master/installer.zsh | zsh
	# else
	# 	echo "ZPlug already installed."
	# fi
	echo -e "${LCYN}█▓▒░░ ${WHT}ZPlug ${NC}-> ${GRN}Done!${NC}"

	# chsh -s /bin/zsh
	chsh -s "$(grep /zsh$ /etc/shells | tail -1)" && echo -e "${LCYN}█▓▒░░ ${WHT}Z Shell ${NC}-> ${GRN}Default Shell!${NC}"
	# If error occurs, log in as root then type chsh -s /bin/bash USERNAME.
fi

#————————[6] Outro
#
[ "$X_CHOSEN" = 1 ] && ALSO=" Extra and" || ALSO=""
echo
echo -e "${LCYN}█▓▒░░${GRN}$ALSO Dots setup done!"
echo
echo -e " ${NC}If this is the first run, reboot the machine"
echo " to see full effect."
echo
echo " If you having issues, want to help,"
echo " please feel free to open issue, send PR:"
echo
echo -e "${WHT}https://github.com/egeesin/dots/issues${NC}"
echo
echo -e "${LCYN}Thank you for using dots. *_*${NC}"
