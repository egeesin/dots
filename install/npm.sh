if [[ "$(uname -s)" == "Darwin" ]]; then
	brew install nvm
	export BREW_PREFIX_NVM=$(brew --prefix nvm)
	set-config "BREW_PREFIX_NVM" "$BREW_PREFIX_NVM" "$DOT_CACHE"
	. "${DOTFILES_DIR}/system/nvm.macos"
elif [[ "$(uname -s)" == "Linux" ]]; then
	pacaur -a -S nvm
	. /usr/share/nvm/init-nvm.sh
fi
nvm install 6

apps=(
1password2pass
battery-level
birthday
bitly-client
blessed
blessed-contrib
caniuse-cmd
diff-so-fancy
empty-trash-cli
google-font-installer
hget
mapscii
mediumcli
moeda
node-notifier
open-color
pageres-cli
release-it
subdownloader
torrentflix
trash-cli
ttystudio
wallpaper-cli
wat
wopr
)

npm i -g npm@latest
npm i -g "${apps[@]}"

if [[ "$(uname -s)" == "Darwin" ]]; then
	npm i -g how2 svgo tldr
fi
