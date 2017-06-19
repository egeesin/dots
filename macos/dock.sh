#!/usr/bin/env bash
dockutil --no-restart --remove all
dockutil --no-restart --add '' --type spacer --section apps
dockutil --no-restart --add "/Applications/Launchpad.app"
dockutil --no-restart --add "/Applications/iTunes.app"
dockutil --no-restart --add "/Applications/Photos.app"
dockutil --no-restart --add "/Applications/iBooks.app"
dockutil --no-restart --add "/Applications/Clear.app"
dockutil --no-restart --add "/Applications/Safari.app"
dockutil --no-restart --add '' --type spacer --section apps
dockutil --no-restart --add "/Applications/Calendar.app"
dockutil --no-restart --add "/Applications/Contacts.app"
dockutil --no-restart --add "/Applications/Mail.app"
dockutil --no-restart --add "/Applications/FaceTime.app"
dockutil --no-restart --add "/Applications/Messages.app"
dockutil --no-restart --add '' --type spacer --section apps
dockutil --no-restart --add "/Applications/iTerm.app"
dockutil --no-restart --add "/Applications/Vivaldi.app"
dockutil --no-restart --add '' --type spacer --section apps
dockutil --no-restart --add "/Applications/Google Chrome Canary.app"
dockutil --no-restart --add "/Applications/Sublime Text.app"
dockutil --no-restart --add '' --type spacer --section apps
dockutil --no-restart --add "/Applications/Image Capture.app"
dockutil --no-restart --add "/Applications/Preview.app"
dockutil --no-restart --add "/Applications/Affinity Photo.app"
dockutil --no-restart --add "/Applications/Affinity Designer.app"
dockutil --no-restart --add "/Applications/Sketch.app"
dockutil --no-restart --add '' --type spacer --section apps
dockutil --no-restart --add "/Applications/Ulysses.app"
dockutil --no-restart --add "/Applications/Scapple.app"
dockutil --no-restart --add '' --type spacer --section apps
dockutil --no-restart --add "/Applications/Mission Control.app"
dockutil --no-restart --add "/Applications/System Preferences.app"
dockutil --no-restart --add '~/Documents' --view grid --display stack --sort name --allhomes
dockutil --no-restart --add '~/Downloads' --view grid --display stack --sort dateadded --allhomes
dockutil --no-restart --add '~/Pictures/Screenshots' --view fan --display stack --sort datecreated --allhomes
dockutil --no-restart --add '' --type spacer --section others

killall Dock
