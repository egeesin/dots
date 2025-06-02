#!/bin/zsh
echo
echo "▓▒░ Installing global Node modules..."
# shellcheck source=../system/env
. "$DOT_DIR/system/env" # Setting environments necessary for asdf version manager $currentos, $archbits, $X_DIR etc.
# shellcheck source=../system/function
. "$DOT_DIR/system/function" # is_executable, ask, print_platform etc.

# if ! is_executable nvm; then
# if ! command -v fnm &> /dev/null
if ! command -v asdf &> /dev/null
then
	echo
	echo "▓▒░ Installing asdf Version Manager..."

	if [ "$currentos" = "Darwin" ]; then
		# brew install fnm || brew reinstall fnm
		brew install asdf || brew reinstall asdf # Make sure coreutils, curl and git installed before
		# . "$DOT_DIR/system/nvm"

		# Install NodeJS Plugin of asdf
		# deps: gpg gawk
		asdf plugin add nodejs https://github.com/asdf-vm/asdf-nodejs.git

	elif [ "$currentos" = "Arch Linux" ]; then
		if is_executable yay; then
			yay -a -S asdf-vm
		else
			echo "ERR: AUR helper isn't installed, skipping version manager installation..."
			return 1
		fi
		# . /usr/share/nvm/init-nvm.sh
	fi
	# [ ! "$(nvm use v10.6.10)" ] && nvm install --latest-npm -s 10.16.0 --with-intl=full-icu --download=all
	# [ ! "$(nvm use node)" ] && nvm install node --with-intl=full-icu --download=all
	# TODO: exact fnm alternative to this
	# [ ! "$(fnm use lts-latest)" ] && fnm install --lts
	# fnm install lts-latest
	# fnm use lts-latest

	# Install NodeJS Plugin of asdf
	# deps for macOS: gpg gawk
	asdf plugin add nodejs https://github.com/asdf-vm/asdf-nodejs.git
	asdf install nodejs latest
	asdf global nodejs latest
fi
# if ! is_executable fnm; then
	# echo
	# echo "▓▒░ Installing Node Version Manager..."

	# if [ "$currentos" = "Darwin" ]; then
		# brew install nvm
		# BREW_PREFIX_NVM=$(brew --prefix nvm)
		# export BREW_PREFIX_NVM
		# set_config "BREW_PREFIX_NVM" "$BREW_PREFIX_NVM" "$DOT_CACHE" >/dev/null 2>&1
		# shellcheck source=../system/nvm
		# curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.37.2/install.sh | bash
		# . "$DOT_DIR/system/nvm"

	# elif [ "$currentos" = "Arch Linux" ]; then
		# if is_executable yay; then
		# 	yay -a -S nvm
		# else
		# 	echo "ERR: AUR helper isn't installed, skipping Node module installation..."
		# 	return 1
		# fi
		# . /usr/share/nvm/init-nvm.sh
	# fi
	# [ ! "$(nvm use v10.6.10)" ] && nvm install --latest-npm -s 10.16.0 --with-intl=full-icu --download=all
	# [ ! "$(nvm use node)" ] && nvm install node --with-intl=full-icu --download=all



	# nvm cache clean
# fi

echo
echo "▓▒░ Node.js and version manager ready, installing Node modules globally..."

# deasciifier
apps=(
battery-level
# birthday
blessed
blessed-contrib
hget
hjson

# iponmap
# mapscii
# moeda

node-notifier
# npm-check-updates # pnpm can update package.json versions

pageres-cli

# peerflix
# torrentflix

# css-checker
gzip-size-cli
glyphhanger
bash-language-server
# diff-so-fancy
neovim
vscode-langservers-extracted
eslint
stylelint-lsp

# yarn
)
# if command -v npm &> /dev/null
# then
# 	npm i -g npm@latest
# 	npm upgrade
# 	npm i -g "${apps[@]}"
# 	# for x in "${apps[@]}"; do echo "$x" && npm i -g --no-audit --no-fund "$x"; done
# 	npm audit fix
#
# 	if [ "$currentos" = "Darwin" ]; then
# 		npm i -g git+https://github.com/ramitos/jsctags.git
# 	fi
# 	echo "█▓▒░░ Node modules -> Installed globally!"
# else
# 	echo "ERR: NPM cannot be found, try reinstalling fpm and node."
# 	return 0
# fi
#

if command -v pnpm &> /dev/null
then
	[ "$currentos" = "Darwin" ] && brew install pnpm
	[ "$currentos" = "Arch Linux" ] && sudo pacman -S pnpm
	# pnpm add -g pnpm@latest
	# pnpm upgrade
	pnpm add -g "${apps[@]}"
	# for x in "${apps[@]}"; do echo "$x" && npm i -g --no-audit --no-fund "$x"; done
	# pnpm audit --fix

	if [ "$currentos" = "Darwin" ]; then
		pnpm add -g git:ramitos/jsctags
	fi
	echo "█▓▒░░ Node modules -> Installed globally!"
else
	echo "ERR: PNPM cannot be found, try reinstalling 'asdf'."
	return 0
fi

