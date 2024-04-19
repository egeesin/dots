#!/bin/bash
echo
echo "▓▒░ Installing other bundles from main sources..."

# shellcheck source=../system/env
. "$DOT_DIR/system/env" # $currentos, $archbits, $DOT_DIR $X_DIR etc.
# shellcheck source=../system/function
. "$DOT_DIR/system/function" # is_executable, ask, print_platform etc.
# shellcheck source=../system/path
. "$DOT_DIR/system/path" # $GOPATH, Homebrew cellar paths

TEMPDIR=$(mktemp -d 2>/dev/null || mktemp -d -t 'TEMPDIR')
pushd "$TEMPDIR" || return 1

# Ranger Devicons plugin | Add icons to ranger
# if [[ ! -f ~/.config/ranger/devicons.py ]]; then
# 	git clone https://github.com/alexanderjeurissen/ranger_devicons.git
# 	cd ranger_devicons || exit
# 	make install
# 	cd - || exit
# 	mv ranger_devicons/ $DUMP_HISTORY
# fi

#
#----------- Sources for Arch Linux
#
if [[ $currentos == "Arch Linux" ]]; then
	# XinY | Simple command line tool for unit conversions
	if ! is_executable xiny; then
		if ask "Install xiny, CLI unit converter?" N; then
			echo "▓▒░ Installing xiny..."
			sudo wget https://github.com/bcicen/xiny/releases/download/v0.3.1/xiny-0.3.1-linux-amd64 -O /usr/local/bin/xiny
			sudo chmod +x /usr/local/bin/xiny
			echo "█▓▒░░ Done!"
			echo
		fi
	fi
fi

#
#----------- Sources for macOS
#
if [[ $currentos == "Darwin" ]]; then

	# # Jacket | Torrent tracker database
	# curl -L https://github.com/Jackett/Jackett/releases/download/v0.17.562/Jackett.Binaries.macOS.tar.gz | tar xz
	# ./Jacket/install_service_macos
	# # to uninstall: ./Jacket/install_service_macos
	# # to stop the service: launchctl unload ~/Library/LaunchAgents/org.user.Jackett.plist
	# # to start the service launchctl load ~/Library/LaunchAgents/org.user.Jackett.plist
	# echo "IMPORTANT: Don't forget to copy/paste API (from http://localhost:9117) at '~/Library/Application Support/qBittorrent/nova3/engines/jackett.json'"

	# XinY | Simple command line tool for unit conversions
	if ! is_executable xiny; then
		if ask "Install xiny, CLI unit converter?" N; then
			echo "█▓▒░░ Installing xiny..."
			sudo curl -Lo /usr/local/bin/xiny https://github.com/bcicen/xiny/releases/download/v0.3.1/xiny-0.3.1-darwin-amd64
			sudo chmod +x /usr/local/bin/xiny
			echo "█▓▒░░ Done!"
			echo
		fi
	fi

	# CLI-Visualizer | An Mac alternative for cava which doesn't work
	# on any system except Linux | deps: ncurses, fftw
	if ! is_executable vis; then
		if ask "Install cli-visualizer?" Y; then
			echo "█▓▒░░ Installing cli-visualizer..."
			git clone https://github.com/dpayne/cli-visualizer
			cd cli-visualizer || return
			./install.sh
			cd - || return
			mv cli-visualizer/ "$DUMP_HISTORY"
			echo "█▓▒░░ Done!"
			echo
		fi
	fi

	# pass-import
	# if ! is_executable /usr/local/pass-import; then
	# 	if ask "Install pass-import?" N; then
	# 		echo "█▓▒░░ Installing pass-import..."
	# 		git clone https://github.com/roddhjav/pass-import/
	# 		cd pass-import || return
	# 		sudo make install PREFIX=/usr/local
	# 		cd - || return
	# 		mv pass-import/ "$DUMP_HISTORY"
	# 		echo "█▓▒░░ Done!"
	# 		echo
	# 	fi
	# fi

	# Wego
	# if ! is_executable wego; then
	# 	if ask "Install wego?" N; then
	# 		echo "█▓▒░░ Installing wego..."
	# 		go get -u github.com/schachmat/wego
	# 		echo "█▓▒░░ Done!"
	# 	fi
	# fi

	# Combustion, the Tranmsission Material Theme
	# curl -O https://github.com/Secretmapper/combustion/archive/v0.6.4.tar.gz
	# tar xvzf combustion-0.6.4.tar.gz
	# mv combustion-0.6.4

	# imgcat for iTerm2
	# dep: iterm2.9 - ranger
	# Note: Don't forget to add this line to ranger config -> set preview_images true
	#                                                         set preview_images_method iterm2
	# if [[ ! -f ~/.dots/bin/imgcat ]]; then
	# 	if ask "Install imgcat, image viewer for iTerm?" Y; then
	# 		wget -O ~/.dots/bin/imgcat https://raw.githubusercontent.com/gnachman/iTerm2/master/tests/imgcat
	# 	fi
	# fi
fi
popd || return 1
echo "█▓▒░░ Packages from other sources -> Done!"
