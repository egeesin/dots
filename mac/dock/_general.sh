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
$CMD "/Applications/qBittorrent.app"
$CMD "/Applications/Calendar.app"
$CMD "/Applications/Stickies.app"
$CMD "/Applications/Scapple.app"
$CMD "/Applications/Obsidian.app"
$CMD "/Applications/Bitwarden.app"
$CMD "/Applications/Authy Desktop.app"
# $CMD "/Applications/1Password.app"
# $CMD "/Applications/Maps.app"
$SPACER
$CMD "/Applications/Discord.app"
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
# $CMD "/Applications/Adobe Photoshop CC 2020/Adobe Photoshop 2020.app"
# $CMD "/Applications/Adobe Illustrator CC 2020/Adobe Illustrator 2020.app"
# $CMD "/Applications/Adobe InDesign CC 2020/Adobe InDesign 2020.app"
$CMD "/Applications/Affinity Designer.app"
$CMD "/Applications/Affinity Photo.app"
$CMD "/Applications/Aseprite v.1.2.27/Aseprite.app"
$CMD "/Applications/PureRef.app"
# $CMD "/Applications/Affinity Publisher.app"
$CMD "/Applications/Image Capture.app"
$CMD "/System/Applications/Utilities/Digital Color Meter.app"
$CMD "/Applications/ImageOptim.app"
# $CMD "/Applications/Utilities/Vectoraster.app"
# $CMD "/Applications/Utilities/Patternodes.app"
$SPACER
$CMD "/Applications/Music.app"
# $CMD "/Applications/iTunes.app"
$CMD "/Applications/QuickTime Player.app"
$CMD "/System/Applications/Utilities/Audio MIDI Setup.app"
$CMD "/Applications/djay Pro AI.app"
$CMD "/Applications/HandBrake.app"
$CMD "/Applications/Glyphs 3.app"
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
$CMD "/Users/ege/webdev/webdev-preview.app"
$CMD "/Applications/Sublime Text.app"
$CMD "/Applications/Transmit.app"
$CMD "/Applications/Utilities/Activity Monitor.app"
$CMD "/Applications/GrandPerspective.app"
# $CMD "/Applications/Utilities/Console.app"
$CMD "/Applications/AppCleaner.app"
$CMD "/Applications/VNC Viewer.app"
$CMD "/Applications/Preview.app"
# $CMD "/Applications/Glyphs Mini.app"
# $SPACER
# $CMD "/Applications/PolyMC.app"
# $CMD "/Applications/MultiMC.app"
# $CMD "/Applications/Steam.app"
# $CMD "/Applications/Steam Link.app"
$CMD "/Applications/System Preferences.app"
$CMD "/Applications/MiddleClick.app"
$CMD "$HOME/Downloads" --view grid --display stack --sort dateadded --allhomes
$CMD "$HOME/Library/CloudStorage/Dropbox/shared-between-all-devices" --view grid --display stack --sort dateadded --allhomes
$CMD "$HOME/Documents" --view grid --display stack --sort name --allhomes
SSPATH="$HOME/Pictures/Screenshots"
[ ! -d "$SSPATH" ] && mkdir -p "$SSPATH"
$CMD "$SSPATH" --view fan --display stack --sort datemodified --allhomes
$CMD '' --type spacer --section others
killall Dock
echo "Dock preset chosen: General"
