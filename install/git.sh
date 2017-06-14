# git.sh - github.com/egeesin

# Ranger Devicons plugin
if [[ ! -f ~/.config/ranger/devicons.py ]]; then
	git clone https://github.com/alexanderjeurissen/ranger_devicons.git
	cd ranger_devicons
	make install
	cd -
fi

if [[ "$(uname -s)" == "Darwin" ]]; then

	# CLI-Visualizer
	# deps: ncurses, fftw
	if [[ ! -x "vis" ]]; then
		git clone https://github.com/dpayne/cli-visualizer
		cd cli-visualizer
		./install.sh
		cd -
	fi

	# pass-import
	if [[ ! -x "pass-import" ]]; then
		git clone https://github.com/roddhjav/pass-import/
		cd pass-import
		sudo make PREFIX=/usr/local install
		cd -
	fi

	# Slacker
	if [[ ! -x "slacker" ]]; then
		git clone https://github.com/TidalLabs/Slacker.git
    	cd Slacker
    	sudo make PREFIX=/usr/local install
    	cd -
	fi

	#
	# Important Note: Before installing go apps, set GOPATH first!
	#
	
	# Wego 
	if [[ ! -x "wego" ]]; then
		go get -u github.com/schachmat/wego
	fi

	# Discorder
	if [[ ! -x "discorder" ]]; then
		go get -u github.com/jonas747/discorder/cmd/discorder
	fi

	# imgcat for iTerm2
	# dep: iterm2.9 - ranger
	# Note: Don't forget to add this line to ranger config -> set preview_images true
	#												    	  set preview_images_method iterm2
	[[ ! -f ~/.dotfiles/bin/imgcat ]] && wget -O ~/.dotfiles/bin/imgcat https://raw.githubusercontent.com/gnachman/iTerm2/master/tests/imgcat

fi
