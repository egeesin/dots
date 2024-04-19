#!/bin/bash
echo
echo "▓▒░ Placing apps on dock..."

CMD="dockutil --no-restart --add"
SPACER="dockutil --no-restart --add ('') --type spacer --section apps"

dockutil --no-restart --remove all
$CMD "/Applications/Launchpad.app"
$SPACER
$CMD "/Applications/Firefox.app"
$CMD "/Applications/Mail.app"
$CMD "/Applications/Stickies.app"
$CMD "/Applications/Obsidian.app"
$CMD "/Applications/Authy Desktop.app"
# $CMD "/Applications/1Password.app"
# $CMD "/Applications/Maps.app"
$SPACER
$CMD "/Applications/Discord.app"
$SPACER
# $CMD "/Applications/Affinity Designer.app"
# $CMD "/Applications/Affinity Photo.app"
# $CMD "/Applications/Aseprite v.1.2.27/Aseprite.app"
# $CMD "/Applications/Utilities/Vectoraster.app"
# $CMD "/Applications/Utilities/Patternodes.app"
# $SPACER
# $CMD "/Applications/Music.app"
# $CMD "/Applications/iTunes.app"
# $CMD "/Applications/QuickTime Player.app"
# $SPACER
# $CMD "/Applications/IINA.app"
# $CMD "/Applications/VLC.app"
# $CMD "/Applications/Spotify.app"
# $CMD "/Applications/OBS.app"
$CMD "/Applications/AppCleaner.app"
$CMD "/Applications/VNC Viewer.app"
# $SPACER
$CMD "/Applications/PolyMC.app"
# $CMD "/Applications/MultiMC.app"
$CMD "/Applications/Steam.app"
$CMD "/Applications/Steam Link.app"
$CMD "/Applications/System Preferences.app"
$CMD "$HOME/Downloads" --view grid --display stack --sort dateadded --allhomes
SSPATH="$HOME/Pictures/Screenshots"
[ ! -d "$SSPATH" ] && mkdir -p "$SSPATH"
$CMD "$SSPATH" --view fan --display stack --sort datemodified --allhomes
$CMD '' --type spacer --section others
killall Dock
echo "Dock preset chosen: Gaming"
