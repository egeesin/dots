{host, pkgs, ...}: let
  inherit
    (import ../../../hosts/${host}/variables.nix)
    # browser
    fileManager
    terminal
    terminalfloating
    launcherMenu
    startMenu
    ;
  hyprgamemode = pkgs.writeShellScriptBin "hyprgamemode" ''
    #!/bin/sh
    HYPRGAMEMODE=$(hyprctl getoption animations:enabled | awk 'NR==1{print $2}')
    if [ "$HYPRGAMEMODE" = 1 ] ; then
        hyprctl --batch "\
            keyword animations:enabled 0;\
            keyword decoration:shadow:enabled 0;\
            keyword decoration:blur:enabled 0;\
            keyword general:gaps_in 0;\
            keyword general:gaps_out 0;\
            keyword decoration:rounding 0"
        exit
    fi
    hyprctl reload
  '';
in {
  wayland.windowManager.hyprland = {
    settings = {
      # binds = {
          # pass_mouse_when_bound = true;
      # };
      bindr = [
        # Press dnd release modifier key to open launcher menu
        "SUPER, SUPER_L, exec, ${launcherMenu}"
        ];
      bind = [
        # Example binds, see https://wiki.hyprland.org/Configuring/Binds/ for more
        "SUPER SHIFT, return, exec, ${terminal}"
        "SUPER, return, exec, ${terminalfloating}"
        "SUPER CTRL, W, killactive,"
        "alt, F4, killactive," # Classic.
        "SUPER SHIFT, Q, exit,"
        "CTRL ALT, DELETE, exit," # Another classic.
        # "SUPER SHIFT, Q, uwsm stop,"
        # "CTRL ALT, DELETE, uwsm stop,"
        "SUPER, E, exec, ${fileManager}"
        "SUPER, S, togglefloating,"
        "SUPER, C, centerwindow,"
        "SUPER CTRL,S,workspaceopt, allfloat" # Toggle all windows to be all float
        "SUPER, space, exec, ${startMenu}" # Launch start menu
        "SUPER, F, fullscreen,"
        "SUPER, F11, fullscreen," # And another classic.
        # "SUPER SHIFT, P, pseudo," # dwindle
        "SUPER, P, pin, "
        "SUPER SHIFT, space, togglesplit," # dwindle

        # Move focus with mainMod + arrow keys;
        "SUPER, H, movefocus, l"
        "SUPER, L, movefocus, r"
        "SUPER, K, movefocus, u"
        "SUPER, J, movefocus, d"

        "SUPER SHIFT, H, movewindow, l"
        "SUPER SHIFT, L, movewindow, r"
        "SUPER SHIFT, K, movewindow, u"
        "SUPER SHIFT, J, movewindow, d "

        # Switch workspaces with mainMod + [0-9];
        "SUPER, 1, workspace, 1"
        "SUPER, 2, workspace, 2"
        "SUPER, 3, workspace, 3"
        "SUPER, 4, workspace, 4"
        "SUPER, 5, workspace, 5"
        "SUPER, 6, workspace, 6"
        "SUPER, 7, workspace, 7"
        "SUPER, 8, workspace, 8"
        "SUPER, 9, workspace, 9"
        "SUPER, 0, workspace, 10"

        # Scroll through existing workspaces with mainMod + scroll
        "SUPER, mouse_down, workspace, e-1"
        "SUPER, mouse_up, workspace, e+1"

        "SUPER SHIFT, mouse_down, movetoworkspace, e-1"
        "SUPER SHIFT, mouse_up, movetoworkspace, e+1"
        # "SUPER SHIFT, mouse_down, movetoworkspacesilent, e+1"
        # "SUPER SHIFT, mouse_up, movetoworkspacesilent, e-1"

        # Move to next/prev workspace with mod+side buttons
        # "SUPER, mouse:276, workspace, e+1"
        # "SUPER, mouse:275, workspace, e-1"
        
        # Move active window to a workspace without switching with mainMod + SHIFT + [0-9];
        "SUPER SHIFT, 1, movetoworkspacesilent, 1"
        "SUPER SHIFT, 2, movetoworkspacesilent, 2"
        "SUPER SHIFT, 3, movetoworkspacesilent, 3"
        "SUPER SHIFT, 4, movetoworkspacesilent, 4"
        "SUPER SHIFT, 5, movetoworkspacesilent, 5"
        "SUPER SHIFT, 6, movetoworkspacesilent, 6"
        "SUPER SHIFT, 7, movetoworkspacesilent, 7"
        "SUPER SHIFT, 8, movetoworkspacesilent, 8"
        "SUPER SHIFT, 9, movetoworkspacesilent, 9"
        "SUPER SHIFT, 0, movetoworkspacesilent, 10"

        "SUPER, tab, focusurgentorlast,"
        # "SUPER, tab, workspace, e+1"
        "SUPER SHIFT, tab, workspace, e-1"

        # to switch between windows in a floating workspace
        # bind = SUPER, Tab, cyclenext,           # change focus to another window
        # bind = SUPER, Tab, bringactivetotop,    # bring it to the top

        # Example special workspace (scratchpad)
        # bind = SUPER, S, togglespecialworkspace, magic
        # bind = SUPER SHIFT, S, movetoworkspace, special:magic

        # "SUPER, N, exec, swaync-client -rs"
        "SUPER, N, exec, swaync-client -t"

        # Screenshot Keybinds (requires grim, slurpy, satty, wl-clipboard)
        ",Print,exec,grim $(xdg-user-dir PICTURES)/Screenshots/$(date +'%Y%m%d%H%M%S_1.png') && notify-send 'Screenshot saved'"
        "SUPER SHIFT, S, exec, grim -g \"$(slurp)\" - | wl-copy"
        # "SUPER, Print, exec, grim -g \"$(slurp)\" - | wl-copy"
        "SUPER,Print,exec,grim -g \"$(slurp -o -r -c '##ff0000ff')\" -t ppm - | satty --filename - --fullscreen --output-filename $(xdg-user-dir PICTURES)/Screenshots/satty-$(date '+%Y%m%d-%H:%M:%S').png"
        # "SUPER SHIFT,Print,exec,grim -g \"$(slurp -o -r -c '##ff0000ff')\" -t ppm - | satty --filename - --fullscreen --output-filename $(xdg-user-dir PICTURES)/Screenshots/satty-$(date '+%Y%m%d-%H:%M:%S').png"

        # Tsoding's zoom tool that works in Wayland
        "SUPER, Z, exec, ${pkgs.woomer}/bin/woomer"

        # Color picker that copies hex code (requires hyperpicker)
        "SUPER SHIFT, C, exec, ${pkgs.hyprpicker}/bin/hyprpicker -an"

        # Global Keybinds (https://wiki.hyprland.org/Configuring/Binds/#global-keybinds)
        "SUPER, F10, pass, class:^(com.obsproject.Studio)$"
        "CTRL SHIFT, M, pass, class:^(discord)$" # not working

        # Toggle custom game mode that disables all animations/effects of Hyprland
        # "$SUPER, F1, exec, ~/.dots/bin/hypr/hyprgamemode.sh"
        # "SUPER, G, exec, ~/.dots/bin/hypr/hyprgamemode.sh"
        # "SUPER, G, exec, ${gamemode}/bin/gamemode"
        "SUPER, G, exec, ${hyprgamemode}/bin/hyprgamemode"
       
        "SUPER CTRL, L, exec, ${pkgs.hyprlock}/bin/hyprlock"
        "SUPER CTRL, space, global, kando:example-menu"
        # "SUPER CTRL, space, global, kando -m example-menu"

        # Another cool config for adding description/category to keybind helper
        # https://github.com/HyDE-Project/HyDE/blob/master/Configs/.config/hypr/keybindings.conf
 
        # "SUPER,Return,exec,${terminal}"
        # "SUPER,W,exec,${browser}"
        # "SUPER,K,exec,list-keybinds"
        # "SUPER SHIFT,Return,exec,rofi-launcher"
        # "SUPER SHIFT,W,exec,web-search"
        # "SUPER ALT,W,exec,wallsetter"
        # "SUPER,Y,exec,kitty -e yazi"

        # "SUPER,D,exec,discord"
        # "SUPER,O,exec,obs"
        # "SUPER,G,exec,gimp"
        # "SUPER,T,exec,pypr toggle term"
        # "SUPER,M,exec,pavucontrol"
 
        # "SUPER,V,exec, cliphist list | rofi -dmenu | cliphist decode | wl-copy"
        # "SUPER SHIFT,SPACE,movetoworkspace,special"
      ];

      binde = [
        # Built-in Zoom Keybinds
        "SUPER ALT, 0, exec, hyprctl -q keyword cursor:zoom_factor 1"
        "SUPER ALT, equal, exec, hyprctl -q keyword cursor:zoom_factor $(hyprctl getoption cursor:zoom_factor | awk '/^float.*/ {print $2 * 1.1}')"
        "SUPER ALT, minus, exec, hyprctl -q keyword cursor:zoom_factor $(hyprctl getoption cursor:zoom_factor | awk '/^float.*/ {print $2 * 0.9}')"
      ];

      bindel = [
        # Volume Adjustment Keybinds (requires wireplumber)
        ",XF86AudioRaiseVolume, exec, wpctl set-volume @DEFAULT_AUDIO_SINK@ 5%+"
        ",XF86AudioLowerVolume, exec, wpctl set-volume @DEFAULT_AUDIO_SINK@ 5%-"
        ",XF86AudioMute, exec, wpctl set-mute @DEFAULT_AUDIO_SINK@ toggle"
        ",XF86AudioMicMute, exec, wpctl set-mute @DEFAULT_AUDIO_SOURCE@ toggle"

        # Brightness Adjustment Keybinds (requires brightnessctl)
        ",XF86MonBrightnessUp, exec, brightnessctl s 10%+"
        ",XF86MonBrightnessDown, exec, brightnessctl s 10%-"
      ];

      bindl = [
        # Media Keybinds (requires playerctl)
        # bindeo = , XF86AudioNext, exec, playerctl position +5 
        # For some reason, o (longPress) flag not working.
        ", XF86AudioNext, exec, playerctl next"
        ", XF86AudioPause, exec, playerctl play-pause"
        ", XF86AudioPlay, exec, playerctl play-pause"
        ", XF86AudioPrev, exec, playerctl previous"
      ];

      bindm = [ # Tip: Use wev to get keycodes of mouse buttons.
        # Move/resize windows with mainMod + LMB/RMB and dragging
        "SUPER, mouse:272, movewindow" # Move window
        "SUPER, mouse:273, resizewindow" # Resize window regardless of proportion
        "SUPER SHIFT, mouse:273, resizewindow 1" # Resize window proportionally
      ];

    };
    extraConfig = ''
      # Resize Controls
    
      # will switch to a submap called resize
      bind = SUPER, R, submap, resize;

      # will start a submap called "resize"
      submap = resize;

      # sets repeatable binds for resizing the active window
      binde = , L, resizeactive, 60 0
      binde = , H, resizeactive, -60 0
      binde = , K, resizeactive, 0 -60
      binde = , J, resizeactive, 0 60

      # use reset to go back to the global submap
      bind =, escape, submap, reset

      # will reset the submap, which will return to the global submap
      submap = reset;
    '';
  };
  
}
