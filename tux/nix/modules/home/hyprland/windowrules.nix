{...}: {
  wayland.windowManager.hyprland.settings = {
    windowrulev2 = [
      # Type `hyprctl clients` to get all window class, title or status info.
      "tag +file-manager, class:^([Tt]hunar|org.gnome.Nautilus|[Pp]cmanfm-qt|org.kde.dolphin)$"
      "tag +terminal, class:^(com.mitchellh.ghostty|org.wezfurlong.wezterm|Alacritty|kitty|kitty-dropterm)$"
      "tag +browser, class:^(Brave-browser(-beta|-dev|-unstable)?)$"
      "tag +browser, class:^([Ff]irefox|org.mozilla.firefox|[Ff]irefox-esr|[Zz]en})$"
      "tag +browser, class:^([Gg]oogle-chrome(-beta|-dev|-unstable)?)$"
      "tag +browser, class:^([Cc]hromium)$"
      "tag +browser, class:^([Tt]horium-browser|[Cc]achy-browser)$"
      "tag +projects, class:^(codium|codium-url-handler|VSCodium|[Kk]ate)$"
      "tag +projects, class:^(VSCode|code-url-handler)$"
      "tag +im, class:^([Dd]iscord|[Ww]ebCord|[Vv]esktop|[Ff]ractal|[Bb]eeper)$"
      "tag +im, class:^([Ff]erdium)$"
      "tag +im, class:^([Ww]hatsapp-for-linux)$"
      "tag +im, class:^(org.telegram.desktop|io.github.tdesktop_x64.TDesktop)$"
      "tag +im, class:^(teams-for-linux)$"
      "tag +games, class:^(gamescope)$"
      "tag +games, class:^(steam_app_\d+)$"
      "tag +gamestore, class:^([Ss]team)$"
      "tag +gamestore, title:^([Ll]utris)$"
      "tag +gamestore, class:^(com.heroicgameslauncher.hgl)$"
      "tag +settings, class:^(gnome-disks|wihotspot(-gui)?)$"
      "tag +settings, class:^([Rr]ofi)$"
      "tag +settings, class:^(file-roller|org.gnome.FileRoller)$"
      "tag +settings, class:^(nm-applet|nm-connection-editor|blueman-manager)$"
      "tag +settings, class:^(pavucontrol|org.pulseaudio.pavucontrol|com.saivert.pwvucontrol)$"
      "tag +settings, class:^(nwg-look|qt5ct|qt6ct|[Yy]ad)$"
      "tag +settings, class:(xdg-desktop-portal-gtk)"
      "tag +settings, class:(.blueman-manager-wrapped)"
      "tag +settings, class:(nwg-displays)"
      "move 72% 7%,title:^(Picture-in-Picture)$"
      "center, class:^([Ff]erdium)$"
       "float, class:^([Ww]aypaper)$"
      "center, class:^(pavucontrol|org.pulseaudio.pavucontrol|com.saivert.pwvucontrol)$"
      "center, class:([Tt]hunar), title:negative:(.*[Tt]hunar.*)"
      "center, title:^(Authentication Required)$"
      # "idleinhibit fullscreen, class:^(*)$" # this throws error somehow
      # "idleinhibit fullscreen, title:^(*)$" # this throws error somehow
      "idleinhibit fullscreen, fullscreen:1"
      "float, tag:settings*"
      "float, class:^([Ff]erdium)$"
      "float, title:^(Picture-in-Picture)$"
      "float, class:^(mpv|com.github.rafostar.Clapper)$"
      "float, title:^(Authentication Required)$"
      "float, class:(codium|codium-url-handler|VSCodium), title:negative:(.*codium.*|.*VSCodium.*)"
      "float, class:^(com.heroicgameslauncher.hgl)$, title:negative:(Heroic Games Launcher)"
      "float, class:^([Ss]team)$, title:negative:^([Ss]team)$"
      "float, class:([Tt]hunar), title:negative:(.*[Tt]hunar.*)"
      "float, initialTitle:(Add Folder to Workspace)"
      "float, initialTitle:(Open Files)"
      "float, initialTitle:(wants to save)"
      "size 70% 60%, initialTitle:(Open Files)"
      "size 70% 60%, initialTitle:(Add Folder to Workspace)"
      "size 70% 70%, tag:settings*"
      "size 60% 70%, class:^([Ff]erdium)$"
      # "opacity 1.0 1.0, tag:browser*"
      # "opacity 0.9 0.8, tag:projects*"
      # "opacity 0.94 0.86, tag:im*"
      # "opacity 0.9 0.8, tag:file-manager*"
      # "opacity 0.8 0.7, tag:terminal*"
      # "opacity 0.8 0.7, tag:settings*"
      # "opacity 0.8 0.7, class:^(gedit|org.gnome.TextEditor|mousepad)$"
      # "opacity 0.9 0.8, class:^(seahorse)$ # gnome-keyring gui"
      # "opacity 0.95 0.75, title:^(Picture-in-Picture)$"
      "pin, title:^(Picture-in-Picture)$"
      "keepaspectratio, title:^(Picture-in-Picture)$"
      "noblur, tag:games*"
      "fullscreen, tag:games*"

      # Ulauncher closes instantly as soon mouse cursor moves
      # outside of the bar. This fixes it.
      "stayfocused,class:^(ulauncher)$"
      "float, class:^(ulauncher)$"
      "noblur, class:^(ulauncher)$"
      "noborder, class:^(ulauncher)$"
      "noshadow, class:^(ulauncher)$"

      # Ignore maximize requests from apps. You'll probably like this.
      "suppressevent maximize, class:.*"

      # Fix some dragging issues with XWayland
      "nofocus,class:^$,title:^$,xwayland:1,floating:1,fullscreen:0,pinned:0"

      # Make corners more rounded if window is pinned
      "rounding 24, pinned:1, fullscreen:0, xwayland:0"
      # Translucent PiP
      # "opacity 0.8 0.8,title:^(Picture-in-Picture)$"

      # Floating and always on top Firefox PiP
      # https://github.com/hyprwm/Hyprland/issues/2942
      "size 640 360, title:(Picture-in-Picture)"
      "pin, title:^(Picture-in-Picture)$"
      "move 1906 14, title:(Picture-in-Picture)"
      "float, title:^(Picture-in-Picture)$"
      "float, initialTitle:^(Discord Popout)$"

      # Differentiate XWayland windows
      "bordercolor rgb(ff757f), xwayland:1"

      "float, class:^(steam_app_)$"

      # Float windows I'd get rid of from window quickly and
      # I don't want it to mess with my tiling windows.
      # windowrule = fullscreen, woomer

      "float,initialtitle:^(Open File)$ "
      "float,initialTitle:^(Open File)$"
      "float,title:^(Save As)$"
      "float,title:^(Confirm to replace files)$"
      "float,title:^(File Operation Progress)$"
      "float,class:^(xdg-desktop-portal-gtk)$"

      "float,class:^(com.interversehq.qView)$"
      "float,title:^(floating)$"
      "float,class:^(steam)$,initialTitle:^(Friends List)$"
      "float,class:^(org.kde.ark)$"
      "float,class:^(org.kde.kcalc)$"
      "float,class:^(org.kde.dolphin)$"
      "size 800 600,class:^(org.kde.dolphin)$"
      "float,class:^(org.kde.dolphin)$,title:^(Progress Dialog — Dolphin)$"
      "size 673 109:^(org.kde.dolphin)$,title:^(Progress Dialog — Dolphin)$"
      "size 560 240:^(org.kde.dolphin)$,title:^(File Already Exists — Dolphin)$"
      "float,class:^(org.kde.dolphin)$,title:^(Copying — Dolphin)$"
      "float,class:^(vlc)$"
      "float,class:^(nwg-look)$"
      "float,class:^(qt5ct)$"
      "float,class:^(qt6ct)$"
      "float,class:^(thunderbird)$,initialTitle:^(Calendar Reminders)$"
      "float,class:^(org.prismlauncher.PrismLauncher)$"
      "float,class:^(dev-kostromdan-mods-crash_assistant-app-class_loading-Boot)$"

      # "noborder, focus:0"
      # "noshadow, focus:0"
      "noshadow, focus:0, floating: 0"

      # "Smart gaps" / "No gaps when only"
      # uncomment all if you wish to use that.
      "bordersize 0, floating:0, plugin:hyprbars:nobar, onworkspace:w[tv1]"
      "rounding 0, floating:0, plugin:hyprbars:nobar, onworkspace:w[tv1]"
      "bordersize 0, floating:0, plugin:hyprbars:nobar, onworkspace:f[1]"
      "rounding 0, floating:0, plugin:hyprbars:nobar, onworkspace:f[1]"
    ];
    workspace = [
    #   # Note: Won't work while hyprbars enabled
      "w[tv1]s[false], gapsout:0, gapsin:0"
      "f[1]s[false], gapsout:0, gapsin:0"
    ];
    windowrule = [
      # set bordercolor to green if window's client fullscreen state is 1(maximize) (internal state can be anything)
      # "bordercolor rgb(00FF00), fullscreenstate:* 1"

      # Disable animation or blur for specific windows
      # "noanim, hyprpicker"
      # "noanim, selection"
      "noanim, title:woomer"

      "noblur, title:ulauncher"

      # Setup for Kando
      "noblur, class:kando"
      "opaque, class:kando"
      "size 100% 100%, class:kando"
      "noborder, class:kando"
      "noanim, class:kando"
      "float, class:kando"
      "pin, class:kando"
    ];
    layerrule = [
      "blur, waybar" # Add blur to waybar
      "blur, nwg-drawer"
      "blurpopups, waybar" # Blur waybar popups too!
      "ignorealpha 0.2, waybar" # Make it so transparent parts are ignored

      "blur,notifications"
      "ignorezero,notifications"
      "blur,swaync-notification-window"
      "ignorezero,swaync-notification-window"
      "blur,swaync-control-center"
      "ignorezero,swaync-control-center"
      "blur,logout_dialog"

      # Shimeji https://codeberg.org/thatonecalculator/spamton-linux-shimeji
      # "float, class:com-group_finity-mascot-Main"
      # "noblur, class:com-group_finity-mascot-Main"
      # "nofocus, class:com-group_finity-mascot-Main"
      # "noshadow, class:com-group_finity-mascot-Main"
      # "noborder, class:com-group_finity-mascot-Main"
    ];


    # Hide instead of kill Steam.
    # if [ "$(hyprctl activewindow -j | jq -r ".class")" = "Steam" ]; then
    #     ydotool getactivewindow windowunmap
    # else
    #     hyprctl dispatch killactive ""
    # fi
  };
}
