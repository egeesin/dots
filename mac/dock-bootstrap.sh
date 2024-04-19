#!/bin/bash

echo
# shellcheck source=../system/env
. "$DOT_DIR/system/env" # $currentos, $archbits etc.
# shellcheck source=../system/function
. "$DOT_DIR/system/function" # is_executable, ask, print_platform etc.

# enable highlight hover effect for the grid view of a stack (dock)
defaults write com.apple.dock mouse-over-hilite-stack -bool true

# set the icon size
defaults write com.apple.dock tilesize -int 48

# change dock location
defaults write com.apple.dock orientation bottom

# disable magnification
defaults write com.apple.dock magnification -bool true

# change minimize/maximize window effect
defaults write com.apple.dock mineffect -string "scale"

# minimize windows into their application’s icon
defaults write com.apple.dock minimize-to-application -bool true

# enable spring loading for all dock items
defaults write com.apple.dock enable-spring-load-actions-on-all-items -bool true

# show indicator lights for open applications in the dock
defaults write com.apple.dock show-process-indicators -bool true

# wipe all (default) app icons from the dock
# this is only really useful when setting up a new mac, or if you don’t use
# the dock to launch apps.
defaults write com.apple.dock persistent-apps -array

# show only open applications in the dock
#defaults write com.apple.dock static-only -bool true

# don’t animate opening applications from the dock
defaults write com.apple.dock launchanim -bool false

# speed up mission control animations
defaults write com.apple.dock expose-animation-duration -float 0.1

# don’t group windows by application in mission control
# (i.e. use the old exposé behavior instead)
defaults write com.apple.dock expose-group-by-app -bool false

# disable dashboard
defaults write com.apple.dashboard mcx-disabled -bool true

# don’t show dashboard as a space
defaults write com.apple.dock dashboard-in-overlay -bool true

# don’t automatically rearrange spaces based on most recent use
defaults write com.apple.dock mru-spaces -bool false

# remove the auto-hiding dock delay
defaults write com.apple.dock autohide-delay -float 0
# remove the animation when hiding/showing the dock
defaults write com.apple.dock autohide-time-modifier -float 0

# automatically hide and show the dock
defaults write com.apple.dock autohide -bool true

# make dock icons of hidden applications translucent
defaults write com.apple.dock showhidden -bool true

# hide recent applications in dock
defaults write com.apple.dock show-recents -bool false

# disable show/hide transition
defaults write com.apple.dock springboard-show-duration -int 0
defaults write com.apple.dock springboard-hide-duration -int 0

# disable the launchpad gesture (pinch with thumb and three fingers)
#defaults write com.apple.dock showlaunchpadgestureenabled -int 0

# reset launchpad, but keep the desktop wallpaper intact
find "${home}/library/application support/dock" -name "*-*.db" -maxdepth 1 -delete

# # Add iOS & Watch Simulator to Launchpad
# sudo ln -sf "/Applications/Xcode.app/Contents/Developer/Applications/Simulator.app" "/Applications/Simulator.app"
# sudo ln -sf "/Applications/Xcode.app/Contents/Developer/Applications/Simulator (Watch).app" "/Applications/Simulator (Watch).app"

# Add a spacer to the left side of the Dock (where the applications are)
defaults write com.apple.dock persistent-apps -array-add '{tile-data={}; tile-type="spacer-tile";}'
# Add a spacer to the right side of the Dock (where the Trash is)
defaults write com.apple.dock persistent-others -array-add '{tile-data={}; tile-type="spacer-tile";}'

# Hot corners
# Possible values:
#  0: no-op
#  2: Mission Control
#  3: Show application windows
#  4: Desktop
#  5: Start screen saver
#  6: Disable screen saver
#  7: Dashboard
# 10: Put display to sleep
# 11: Launchpad
# 12: Notification Center

# Top left screen corner → Mission Control
defaults write com.apple.dock wvous-tl-corner -int 2
defaults write com.apple.dock wvous-tl-modifier -int 0

# Top right screen corner → Open Notification Center
defaults write com.apple.dock wvous-tr-corner -int 12
defaults write com.apple.dock wvous-tr-modifier -int 0

# Bottom right screen corner → Start screen saver
defaults write com.apple.dock wvous-br-corner -int 5
defaults write com.apple.dock wvous-br-modifier -int 0

# Bottom left screen corner → Desktop
defaults write com.apple.dock wvous-bl-corner -int 4
defaults write com.apple.dock wvous-bl-modifier -int 0

killall Dock
echo
echo "█▓▒░░ Dock -> Done!"
echo "Note: Some app icons may disappear in Launchpad and Dock"
echo "but returns to normal after reboot."
