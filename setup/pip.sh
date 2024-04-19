#!/bin/bash
echo
echo "▓▒░ Installing packages from Python Package Index..."

# shellcheck source=../system/env
. "$DOT_DIR/system/env"
# shellcheck source=../system/function
. "$DOT_DIR/system/function"
# shellcheck source=../system/path
. "$DOT_DIR/system/path"

# if ! is_executable pip; then
# 	echo "ERR: pip missing, exiting."
# 	echo "█▓▒░░ Bundle Installation with pip -> Failed"
# 	return 1
# fi

#----------- For both OSes
packages=(
	Cython --install-option'=''--no-cython-compile'
	Pillow
	gTTS
	tesserocr
	BeautifulSoup4
	virtualenv
	# gallery-dl
	# pockyt
	# isitup
	vl
)
[[ "$currentos" == "Darwin" ]] && pip install "${packages[@]}"
[[ "$currentos" == "Arch Linux" ]] && sudo pip install "${packages[@]}"

packages_three=(
	requests
	docopt
)

[[ "$currentos" == "Darwin" ]] && pip3 install "${packages_three[@]}"
[[ "$currentos" == "Arch Linux" ]] && sudo pip3 install "${packages[@]}"

#----------- For macOS
packages_mac=(
	urlscan

	# bukuserver deps
	# flask
	# flask_api
	# flask_bootstrap
	# flask_paginate
	# flask_wtf
	#/bukuserver deps

	# mopidy-notifier
	# Mopidy-Spotify-Tunigo
)
packages_three_mac=(
	stig # Transmission TUI
	tmuxp # tmux session manager (also f*ck tmuxinator)
	pywal # Color palette generator from wallpaper
	pynvim # Python integration for NeoVim
	pyopenssl
	pyxdg
	# git+https://github.com/rachmadaniHaryono/we-get
	# git+https://github.com/egeesin/curseradio
)
if [ "$currentos" == "Darwin" ]; then
	pip install "${packages_mac[@]}"
	pip3 install "${packages_three_mac[@]}"
	# sudo pip3 install glances[action,browser,cloud,cpuinfo,chart,docker,export,folders,gpu,ip,raid,snmp,web,wifi]
fi
echo "█▓▒░░ Package Bundles from Python Package Index -> Installed!"
