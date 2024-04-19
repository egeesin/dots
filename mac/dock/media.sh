#!/bin/bash
echo
echo "▓▒░ Placing apps on dock..."

# if ! is_executable dockutil; then
# 	echo "ERR: dockutil missing or not on macOS, exiting..."
# 	echo
# 	echo "█▓▒░░ Dock -> Failed."
# 	return 1
# fi

CMD="dockutil --no-restart --add"
SPACER="dockutil --no-restart --add ('') --type spacer --section apps"

dockutil --no-restart --remove all
$CMD "/Applications/Launchpad.app"
$SPACER
$CMD "/Applications/Firefox.app"
$CMD "/Applications/Safari.app"
$CMD "/Applications/qBittorrent.app"
$CMD "/Applications/Calendar.app"
$CMD "/Applications/Obsidian.app"
$SPACER
$CMD "/Applications/IINA.app"
# $CMD "/Applications/VLC.app"
# $CMD "/Applications/OBS.app"
$CMD "/Applications/Music.app"
# $CMD "/Applications/Spotify.app"
# $CMD "/Applications/iTunes.app"
$CMD "/Applications/QuickTime Player.app"
# $CMD "/Applications/Photos.app"
$CMD "/Applications/djay Pro AI.app"
$CMD "/Applications/Mp3tag.app"
$CMD "/Applications/HandBrake.app"
$SPACER
$CMD "/Applications/Alacritty.app"
$CMD "/Applications/Preview.app"
# $SPACER
$CMD "/Applications/System Preferences.app"
$CMD "$HOME/Downloads" --view grid --display stack --sort dateadded --allhomes
SSPATH="$HOME/Pictures/Screenshots"
[ ! -d "$SSPATH" ] && mkdir -p "$SSPATH"
$CMD "$SSPATH" --view fan --display stack --sort datemodified --allhomes
$CMD '' --type spacer --section others
killall Dock
echo "Dock preset chosen: Media"
