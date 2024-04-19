#!/usr/bin/env bash
SOURCE="https://github.com/egeesin/dots"
TARBALL="$SOURCE/tarball/master"
TARGET="$HOME/.dots"
TAR_CMD="tar -xzv -C $TARGET --strip-components=1 --exclude='{.gitignore}'"

if [ -x "`command -v git`" ]; then
	CMD="git clone $SOURCE $TARGET"
elif [ -x "`command -v curl`" ]; then
	CMD="curl -#L $TARBALL | $TAR_CMD"
elif [ -x "`command -v wget`" ]; then
	CMD="wget --no-check-certificate -O -"
fi

if [ -z "$CMD" ]; then
	echo "No git, curl or wget available. Aborting."
else
	echo "Installing dotfiles..."
	mkdir -p "$TARGET"
	eval "$CMD"
	# . "$TARGET/install.sh"
fi
