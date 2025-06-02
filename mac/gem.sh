#!/bin/bash
echo
echo "▓▒░ Installing Ruby gems for macOS..."

# shellcheck source=../system/env
. "$DOT_DIR/system/env"
# shellcheck source=../system/function
. "$DOT_DIR/system/function"
# shellcheck source=../system/path
. "$DOT_DIR/system/path" # Path for Ruby

if ! is_executable ruby; then
	if is_executable asdf; then
		echo
		echo "▓▒░ Ruby is missing, installing..."
		asdf install ruby
	else
		echo
		echo "ERR: asdf Version Manager couldn't installed, skipping Ruby installation..."
		return 1
	fi
	# if is_executable brew; then
	# echo
	# echo "▓▒░ Ruby is missing, installing..."
	# 	brew install ruby
	# fi
else
	echo
	echo "ERR: Ruby couldn't installed, skipping..."
	return 1
fi

echo
echo "▓▒░ Ruby is ready, installing gems..."

#--- For macOS
apps=(
	neovim
	# tmuxinator
	# jekyll
	# sass
	# twterm
)

sudo gem install "${apps[@]}"
echo
echo "█▓▒░░ Ruby Gems -> Taken!"
