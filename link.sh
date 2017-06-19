#!/usr/bin/env bash
DOTFILES_DIR="$HOME/.dotfiles"

touch "$HOME/.config/mpd/mpd.db"
touch "$HOME/.config/mpd/mpd.log"
touch "$HOME/.config/mpd/mpd.pid"
touch "$HOME/.config/mpd/mpdstate"

READLINK=$(which greadlink || which readlink)

cat "$DOTFILES_DIR/symlinks" | while read -r line; do
	link=$HOME'/'$line
	file=$DOTFILES_DIR'/config/'$line

	if [[ "$line" = *" "* ]]; then
		link=$HOME"/"$(echo "$line" | awk '{print $2}')
		file=$DOTFILES_DIR'/config/'$(echo "$line" | awk '{print $1}')
	fi	

	doLink=true
	doMove=false

	if [[ ! -f "$link" ]] && [[ -d "$link" ]] && [[ "$($READLINK -f $link)" = "$link" ]]; then
		doMove=true
	fi

	if [[ -f "$link" ]] && [[ ! -d "$link" ]] && [[ "$($READLINK -f $link)" = "$link" ]]; then
		doMove=true
	fi
	
	# if file is contains "_tux" or "_mac" don't link it yet
	if echo $file | grep -qE '_(tux|mac)$'; then
		doLink=false
	fi

	# if file is contains "_mac" link it if you're on Mac.
	if [[ "$(uname -s)" = "Darwin" ]] && echo $file | grep -qE '_mac$'; then
		doLink=true
	fi

	# if file is contains "_tux" link it if you're on GNU/Linux.
	if [[ "$(uname -s)" = "Linux" ]] && echo $file | grep -qE '_tux$'; then
		doLink=true
	fi

	if [[ "$($READLINK -f "$link")" = "$file" ]]; then
		doLink=false
	fi

	if [[ "$doLink" = true ]]; then
		echo "$link"" not linked, linking now to ""$file"
	fi

	if [[ "$doMove" = true ]]; then
		echo "file exists, creating ""$link"".old"
		mv "$link" "$link"".old"
	fi

	if [[ "$doLink" = true ]]; then
		mkdir -p "$(dirname "$link")"
		ln -sfv "$file" "$link"
	fi
done
