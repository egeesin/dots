#!/bin/bash
# Usage: link.sh linklist.txt
echo
echo "▓▒░ Symlinking configs..."

DOT_DIR="$( cd "$(dirname "${BASH_SOURCE[0]}" )" && pwd )"

. "$DOT_DIR/system/env" # $currentos, $archbits, $DOT_DIR $X_DIR etc.
# shellcheck source=system/function
. "$DOT_DIR/system/function" # is_executable, ask, print_platform etc.
# shellcheck source=system/path
. "$DOT_DIR/system/path" # Homebrew cellar paths

SYMLINKS="$DOT_DIR/linklist.txt"

# Prepare mpd related files beforehand
# touch "$HOME/.config/mpd/mpd{.db,.log,.pid,state}" >/dev/null 2>&1

READLINK=$(command -v greadlink || command -v readlink )
# if [ "$(uname -s)" = "Darwin" ]; then
# 	READLINK=$(command -v greadlink)
# elif [ "$(uname -s)" = "Linux" ]; then
# 	READLINK=$(command -v readlink)
# fi

while read -r line; do
	link=$HOME'/'$line
	file=$DOT_DIR'/config/'$line

	[[ "$line" =~ ^#\  ]] && continue	

	if [[ "$line" = *" "* ]]; then
		# link=$HOME"/"$(echo "$line" | awk '{print $2}')
		link=$HOME"/"$(echo "$line" | tr -s ' ' | cut -d' ' -f2-)
		file=$DOT_DIR"/config/"$(echo "$line" | awk '{print $1}')
	fi

	doLink=true
	doMove=false

	if [ ! -f "$link" ] && [ -d "$link" ] && [ "$($READLINK -f "$link")" = "$link" ]; then
		doMove=true
	fi

	if [ -f "$link" ] && [ ! -d "$link" ] && [ "$($READLINK -f "$link")" = "$link" ]; then
		doMove=true
	fi

	# if file is contains "_tux" or "_mac" don't link it yet
	if echo "$file" | grep -qE '_(tux|mac)$'; then
		doLink=false
	fi

	# if file is contains "_mac" link it if you're on Mac.
	if [ "$(uname -s)" = "Darwin" ] && echo "$file" | grep -qE '_mac$'; then
		doLink=true
	fi

	# if file is contains "_tux" link it if you're on GNU/Linux.
	if [ "$(uname -s)" = "Linux" ] && echo "$file" | grep -qE '_tux$'; then
		doLink=true
	fi

	if [ "$($READLINK -f "$link")" = "$file" ]; then
		doLink=false
	fi

	if [ "$doLink" = true ]; then
		echo "$link" not linked, linking now to "$file"
	fi

	if [ "$doMove" = true ]; then
		echo "file exists, creating ""$link"".old"
		mv "$link" "$link"".old"
	fi

	if [ "$doLink" = true ]; then
		mkdir -p "$(dirname "$link")"
		ln -sfv "$file" "$link"
	fi
done < "$SYMLINKS"

# Firefox CSS links
# Note: The profile directory name must end with .defualt or .default-release
# MACFFP="$(find ~/Library/Application*/Firefox/Profiles/*.default-release -prune)"
# TUXFFP="$(find ~/.mozilla/firefox/*.default-release -prune)"

# if [ "$(uname -s)" = "Darwin" ]; then
# 	echo
# 	echo "Note: If you're on Firefox 69+, don't forget to enable:"
# 	echo "toolkit.legacyUserProfileCustomizations.stylesheets"
# 	echo "in about:config"
# 	echo
# 	mkdir -p "$MACFFP"/chrome
# 	[ ! -L "$MACFFP/chrome/userChrome.css" ] && ln -sfv "$DOT_DIR"/config/firefoxcss_mac "$MACFFP/chrome/userChrome.css"
# 	[ ! -L "$MACFFP/user.js" ] && ln -sfv "$DOT_DIR"/config/firefoxuser "$MACFFP/user.js"
# fi
# if [ "$(uname -s)" = "Linux" ]; then
# 	echo
# 	echo "Note: If you're on Firefox 69+, don't forget to enable:"
# 	echo "toolkit.legacyUserProfileCustomizations.stylesheets"
# 	echo "in about:config"
# 	echo
# 	mkdir -p "$TUXFFP"/chrome
# 	[ ! -L "$TUXFFP/chrome/userChrome.css" ] && ln -sfv "$DOT_DIR"/config/firefoxcss_tux "$TUXFFP/chrome/userChrome.css"
# 	[ ! -L "$MACFFP/user.js" ] && ln -sfv "$DOT_DIR"/config/firefoxuser "$MACFFP/user.js"
# fi

# CFGEXCEP=2 # firefox_css configs
# TOTALCFGCOUNT=$(echo "$(find "$DOT_DIR"/config ! -path "$DOT_DIR"/config -maxdepth 1 ! -name ".DS_Store" | wc -l)" - $CFGEXCEP | bc -l)
# LNKCOUNT=$(wc -l < "$SYMLINKS")
# MACCFGCOUNT=$(grep -c '_mac' "$SYMLINKS")
# TUXCFGCOUNT=$(grep -c '_tux' "$SYMLINKS")$

# echo
# if [[ $currentos == "Darwin" ]]; then
# 	echo -e "${GRN}█▓▒░░ ${WHT}Total $MACCFGCOUNT ${NC}configs symlinked to Mac home directory."
# elif [[ $currentos == "Arch Linux" ]]; then
# 	echo -e "${GRN}█▓▒░░ ${WHT}Total $TUXCFGCOUNT ${NC}configs symlinked to GNU/Linux home directory."
# fi
echo
echo "█▓▒░░ Configurations -> Linked!"
echo
# echo "Note: In Sublime Text 3, in order to config work,"
# echo "install Package Control first then choose a color scheme."
# echo "shift+cmd+P > 'Install Package Control'"
