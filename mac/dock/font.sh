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
# $CMD "/Applications/Photos.app"
# $SPACER
# $CMD "/Applications/Adobe Photoshop CC 2020/Adobe Photoshop 2020.app"
# $CMD "/Applications/Adobe Illustrator CC 2020/Adobe Illustrator 2020.app"
# $CMD "/Applications/Adobe InDesign CC 2020/Adobe InDesign 2020.app"
$CMD "/Applications/Affinity Designer.app"
$CMD "/Applications/PureRef.app"
# $CMD "/Applications/Affinity Publisher.app"
$CMD "/System/Applications/Utilities/Digital Color Meter.app"
# $CMD "/Applications/Utilities/Vectoraster.app"
# $CMD "/Applications/Utilities/Patternodes.app"
$SPACER
$CMD "/Applications/Glyphs 3.app"
# $CMD "/Applications/Glyphs Mini.app"
$CMD "/Applications/Font Book.app"
$CMD "/Applications/UnicodeChecker.app"
$CMD "/Applications/DevCleaner.app"
$SPACER
# $CMD "/Applications/IINA.app"
# $CMD "/Applications/VLC.app"
# $CMD "/Applications/Spotify.app"
# $CMD "/Applications/OBS.app"
# $CMD "/Applications/Adobe Premiere CC 2020/Adobe Premiere 2020.app"
# $CMD "/Applications/Adobe After Effects CC 2020/Adobe After Effects 2020.app"
$CMD "/Applications/Alacritty.app"
$CMD "/Applications/Sublime Text.app"
# $CMD "/Applications/Transmit.app"
$CMD "/Applications/Preview.app"
# $SPACER
$CMD "/Applications/System Preferences.app"
$CMD "/Applications/MiddleClick.app"
$CMD "$HOME/Downloads" --view grid --display stack --sort dateadded --allhomes
$CMD "$HOME/Library/CloudStorage/Dropbox/shared-between-all-devices" --view grid --display stack --sort dateadded --allhomes
SSPATH="$HOME/Pictures/Screenshots"
[ ! -d "$SSPATH" ] && mkdir -p "$SSPATH"
$CMD "$SSPATH" --view fan --display stack --sort datemodified --allhomes
$CMD '' --type spacer --section others
killall Dock
echo "Dock preset chosen: Font"
