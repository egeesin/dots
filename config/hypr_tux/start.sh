#!/usr/bin/env bash

# Bar, wallpaper

# https://nixos.wiki/wiki/Gammastep
# /usr/lib/geoclue-2.0/demos/agent & gammastep
hyprpaper &
waybar &
# agsv1 &
# eww daemon && eww -c ~/.config/eww/bar/ open bar

# Core components (auth, lock screen, notification daemon)
nm-applet --indicator &
gnome-keyring-daemon --start --components=secrets &
hypridle &
dbus-update-activation-environment --systemd WAYLAND_DISPLAY XDG_CURRENT_DESKTOP & 
# hyprpm reload

# dunst
