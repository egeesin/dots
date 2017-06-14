# Install Caskroom

brew tap caskroom/cask
brew install brew-cask
brew tap caskroom/versions

# Install packages

apps=(
	appcleaner
	dropbox
	duet
	fontforge
	google-chrome-canary
	glimmerblocker
	handbrake
	karabiner-elements
	mamp
	minecraft
	poedit
	screens-connect
	scroll-reverser
	sitesucker
	sketch
	soundflower
	spectacle
	sublime-text
	tunnelbear
	the-unarchiver
	virtualbox
	vivaldi
	vlc
	xquartz
)

brew cask install "${apps[@]}"

# Quick Look Plugins (https://github.com/sindresorhus/quick-look-plugins)
brew cask install qlcolorcode qlstephen qlmarkdown quicklook-json qlprettypatch quicklook-csv betterzipql qlimagesize webpquicklook quicklookase quicklook-pat qlvideo suspicious-package

# Link Hammerspoon config
#[ -d ~/.hammerspoon ] || ln -sfv "$DOTFILES_DIR/etc/hammerspoon/" ~/.hammerspoon
