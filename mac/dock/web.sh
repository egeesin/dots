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
$CMD "/Applications/Mail.app"
$CMD "/Applications/Calendar.app"
$CMD "/Applications/Stickies.app"
$CMD "/Applications/Obsidian.app"
$SPACER
$CMD "/Applications/Signal.app"
$CMD "/Applications/Messages.app"
$CMD "/Applications/zoom.us.app"
$SPACER
# $CMD "/Applications/Books.app"
# $CMD "/Applications/Reeder.app"
# $CMD "/Applications/NetNewsWire.app"
# $CMD "/Applications/Tweetbot.app"
# $CMD '' --type spacer --section apps
# $CMD "/Applications/Photos.app"
# $SPACER
$CMD "/Applications/Affinity Designer.app"
$CMD "/System/Applications/Utilities/Digital Color Meter.app"
$CMD "/Applications/ImageOptim.app"
$SPACER
$CMD "/Applications/DevCleaner.app"
$SPACER
$CMD "/Applications/Alacritty.app"
$CMD "/Users/ege/webdev/webdev-preview.app"
$CMD "/Applications/Sublime Text.app"
$CMD "/Applications/Tower.app"
$CMD "/Applications/Transmit.app"
$CMD "/Applications/VNC Viewer.app"
$CMD "/Applications/System Preferences.app"
$CMD "/Applications/MiddleClick.app"
$CMD "$HOME/Downloads" --view grid --display stack --sort dateadded --allhomes
$CMD "$HOME/Library/CloudStorage/Dropbox/shared-between-all-devices" --view grid --display stack --sort dateadded --allhomes
$CMD "$HOME/webdev" --view grid --display stack --sort name --allhomes
SSPATH="$HOME/Pictures/Screenshots"
[ ! -d "$SSPATH" ] && mkdir -p "$SSPATH"
$CMD "$SSPATH" --view fan --display stack --sort datemodified --allhomes
$CMD '' --type spacer --section others

killall Dock
echo "Dock preset chosen: Web"
