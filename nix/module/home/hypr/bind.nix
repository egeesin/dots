{
host,
pkgs,
config,
# lib,
osConfig,
 ...}: let
  inherit
    (import ../../../host/${host}/var.nix)
    # browser
    fileManager
    terminal
    # launcherMenu
    startMenu
    ;
  showdesktop = pkgs.writeShellScriptBin "showdesktop" ''
#!/bin/env sh

TMP_FILE="$XDG_RUNTIME_DIR/hyprland-show-desktop"

CURRENT_WORKSPACE=$(hyprctl monitors -j | jq '.[] | .activeWorkspace | .name' | sed 's/"//g')

if [ -s "$TMP_FILE-$CURRENT_WORKSPACE" ]; then
  readarray -d $'\n' -t ADDRESS_ARRAY <<< $(< "$TMP_FILE-$CURRENT_WORKSPACE")

  for address in "''${ADDRESS_ARRAY[@]}"
  do
    CMDS+="dispatch movetoworkspacesilent name:$CURRENT_WORKSPACE,address:$address;"
  done

  hyprctl --batch "$CMDS"

  rm "$TMP_FILE-$CURRENT_WORKSPACE"
else
  HIDDEN_WINDOWS=$(hyprctl clients -j | jq --arg CW "$CURRENT_WORKSPACE" '.[] | select (.workspace .name == $CW) | .address')

  readarray -d $'\n' -t ADDRESS_ARRAY <<< $HIDDEN_WINDOWS

  for address in "''${ADDRESS_ARRAY[@]}"
  do
    address=$(sed 's/"//g' <<< $address )

    if [[ -n address ]]; then
      TMP_ADDRESS+="$address\n"
    fi

    CMDS+="dispatch movetoworkspacesilent special:desktop,address:$address;"
  done

  hyprctl --batch "$CMDS"

  echo -e "$TMP_ADDRESS" | sed -e '/^$/d' > "$TMP_FILE-$CURRENT_WORKSPACE"
fi
  '';
  hyprgamemode = pkgs.writeShellScriptBin "hyprgamemode" ''
    #!/bin/env sh
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
      # "$mod" = "SUPER";
      "$mod" = "Mod4";
      input = {
        kb_layout = "${osConfig.services.xserver.xkb.layout}";
        kb_variant = "${osConfig.services.xserver.xkb.variant}";
        kb_options = "${osConfig.services.xserver.xkb.options}";
        # kb_rules =
        repeat_rate = 40;
        repeat_delay = 300;
        force_no_accel = 1; # Disable mouse acceleration.
        scroll_points = "0.2 0.0 0.5 1 1.2 1.5";

        numlock_by_default = true;
        follow_mouse = 1;
        # sensitivity = 0; # -1.0 - 1.0, 0 means no modification.
        touchpad = {
          # natural_scroll = true;
          # disable_while_typing = true;
          # scroll_factor = 0.8;
          # tap-to-click = false;
          # middle_button_emulation = false
          disable_while_typing = 0;
          natural_scroll = false;
        };
        # Some configs for Kando to behave
        # having only floating windows in the special workspace will not block focusing windows in the regular workspace.
        special_fallthrough = true;
        # focus will shift to the window under the cursor.
        focus_on_close = 1; # already default
      };
      gestures = {
        workspace_swipe = false;
        # workspace_swipe = 1;
        # workspace_swipe_fingers = 3;
        # workspace_swipe_distance = 500;
        # workspace_swipe_invert = 1;
        # workspace_swipe_min_speed_to_force = 30;
        # workspace_swipe_cancel_ratio = 0.5;
        # workspace_swipe_create_new = 1;
        # workspace_swipe_forever = 1;
      };
      # binds = {
          # pass_mouse_when_bound = true;
      # };
      # bindr = [
      #   # Press dnd release modifier key to open launcher menu
      #   "$mod, SUPER_L, exec, ${launcherMenu}"
      #   ];
      bind = [
        # Example binds, see https://wiki.hyprland.org/Configuring/Binds/ for more
        "$mod+SHIFT, return, exec, ${terminal}"
        "$mod, return, exec, [float] ${terminal}"
        "$mod+CTRL, W, killactive,"
        "ALT, F4, killactive," # Classic.
        "$mod+SHIFT, Q, exit,"
        # "CTRL+ALT, DELETE, exit," # Another classic.
        "$mod+SHIFT+CTRL, L, exec, wlogout,"
        # "$mod+SHIFT, Q, uwsm stop,"
        # "CTRL+ALT, DELETE, uwsm stop,"
        "$mod, E, exec, ${fileManager}"
        "$mod, S, togglefloating,"
        "$mod, C, centerwindow,"
        "$mod+CTRL,S,workspaceopt, allfloat" # Toggle all windows to be all float
        "$mod, space, exec, ${startMenu}" # Launch start menu
        "$mod, F, fullscreen,"
        "$mod, F11, fullscreen," # And another classic.
        # "$mod SHIFT, P, pseudo," # dwindle
        "$mod, P, pin, "
        "$mod+SHIFT, space, togglesplit," # dwindle

        # Move focus with mainMod + arrow keys;
        "$mod, H, movefocus, l"
        "$mod, L, movefocus, r"
        "$mod, K, movefocus, u"
        "$mod, J, movefocus, d"

        "$mod+SHIFT, H, movewindow, l"
        "$mod+SHIFT, L, movewindow, r"
        "$mod+SHIFT, K, movewindow, u"
        "$mod+SHIFT, J, movewindow, d "

        # Switch workspaces with mainMod + [0-9];
        "$mod, 1, workspace, 1"
        "$mod, 2, workspace, 2"
        "$mod, 3, workspace, 3"
        "$mod, 4, workspace, 4"
        "$mod, 5, workspace, 5"
        "$mod, 6, workspace, 6"
        "$mod, 7, workspace, 7"
        "$mod, 8, workspace, 8"
        "$mod, 9, workspace, 9"
        "$mod, 0, workspace, 10"

        # Scroll through existing workspaces with mainMod + scroll
        "$mod, mouse_down, workspace, e-1"
        "$mod, mouse_up, workspace, e+1"

        "$mod+SHIFT, mouse_down, movetoworkspace, e-1"
        "$mod+SHIFT, mouse_up, movetoworkspace, e+1"
        # "$mod SHIFT, mouse_down, movetoworkspacesilent, e+1"
        # "$mod SHIFT, mouse_up, movetoworkspacesilent, e-1"

        # Move to next/prev workspace with mod+side buttons
        # "$mod, mouse:276, workspace, e+1"
        # "$mod, mouse:275, workspace, e-1"

        # Move active window to a workspace without switching with mainMod + SHIFT + [0-9];
        "$mod+SHIFT, 1, movetoworkspacesilent, 1"
        "$mod+SHIFT, 2, movetoworkspacesilent, 2"
        "$mod+SHIFT, 3, movetoworkspacesilent, 3"
        "$mod+SHIFT, 4, movetoworkspacesilent, 4"
        "$mod+SHIFT, 5, movetoworkspacesilent, 5"
        "$mod+SHIFT, 6, movetoworkspacesilent, 6"
        "$mod+SHIFT, 7, movetoworkspacesilent, 7"
        "$mod+SHIFT, 8, movetoworkspacesilent, 8"
        "$mod+SHIFT, 9, movetoworkspacesilent, 9"
        "$mod+SHIFT, 0, movetoworkspacesilent, 10"

        "$mod, tab, focusurgentorlast,"
        "$mod+SHIFT, tab, workspace, e-1"
        # "$mod, tab, workspace, e+1"

        # to switch between windows in a floating workspace
        # bind = $mod, Tab, cyclenext,           # change focus to another window
        # bind = $mod, Tab, bringactivetotop,    # bring it to the top

        # Example special workspace (scratchpad)
        # bind = $mod, S, togglespecialworkspace, magic
        # bind = $mod SHIFT, S, movetoworkspace, special:magic

        # Minimize windows using special workspaces
        "$mod, M, togglespecialworkspace, magic"
        "$mod, M, movetoworkspace, +0"
        "$mod, M, togglespecialworkspace, magic"
        "$mod, M, movetoworkspace, special:magic"
        "$mod, M, togglespecialworkspace, magic"

        # "$mod, N, exec, swaync-client -rs"
        "$mod, N, exec, swaync-client -t"

        # Screenshot Keybinds (requires grim, slurpy, satty, wl-clipboard)
        # Save to clipboard and default screenshot path
        "$mod+SHIFT, S, exec, IMG=$(xdg-user-dir PICTURES)/Screenshots/$(date '+%Y-%m-%d_%Hh%Mm%Ss').png && grim -g \"$(slurp)\" $IMG && wl-copy < $IMG && notify-send 'Selection saved to clipboard and directory.'"
        # "$mod+SHIFT, S, exec, grim -g \"$(slurp)\" - | wl-copy && notify-send 'Selection saved to clipboard'"

        # Save to clipboard and default screenshot path
        "$mod,Print,exec,grim -g \"$(slurp -o -r -c '##${config.lib.stylix.colors.base0D}ff')\" -t ppm - | satty --filename - --fullscreen --output-filename $(xdg-user-dir PICTURES)/Screenshots/$(date '+%Y-%m-%d_%Hh%Mm%Ss')_edited.png"
        ",Print,exec,grim $(xdg-user-dir PICTURES)/Screenshots/$(date '+%Y-%m-%d_%Hh%Mm%Ss')_full.png && notify-send 'Full screenshot saved!'"
        # "$mod, Print, exec, grim -g \"$(slurp)\" - | wl-copy"
        "$mod+SHIFT+CTRL, S, exec, grim -w \"$(hyprctl activewindow -j | jq -r '.address')\" $(xdg-user-dir PICTURES)/Screenshots/$(date '+%Y-%m-%d_%Hh%Mm%Ss')_window.png && notify-send 'Screenshot of active window is saved!'"
        # "$mod SHIFT,Print,exec,grim -g \"$(slurp -o -r -c '##ff0000ff')\" -t ppm - | satty --filename - --fullscreen --output-filename $(xdg-user-dir PICTURES)/Screenshots/satty-$(date '+%Y%m%d-%H:%M:%S').png"

        "$mod+SHIFT, R, exec, recorder-start"
        "$mod+SHIFT, escape, exec, recorder-end"

        # Tsoding's zoom tool that works in Wayland
        "$mod, Z, exec, [workspace current] ${pkgs.woomer}/bin/woomer"

        # Color picker that copies hex code (requires hyperpicker)
        "$mod SHIFT, C, exec, [pin] ${pkgs.hyprpicker}/bin/hyprpicker -an"

        # Global Keybinds (https://wiki.hyprland.org/Configuring/Binds/#global-keybinds)
        # $ hyprctl globalshortcuts # To list all global shortcuts.
        "$mod, F10, pass, class:^(com.obsproject.Studio)$"
        # "$mod, F10, sendshortcut, SUPER, F4, class:^(com\.obsproject\.Studio)$"
        "CTRL+SHIFT, M, pass, class:^(discord)$" # not working
        # ", mouse:276, pass, class:^(TeamSpeak 3)$" # Passes Mouse5 to TeamSpeak if you push to talk

        # Toggle custom game mode that disables all animations/effects of Hyprland
        # "$$mod, F1, exec, ~/.dots/bin/hypr/hyprgamemode.sh"
        # "$mod, G, exec, ~/.dots/bin/hypr/hyprgamemode.sh"
        # "$mod, G, exec, ${gamemode}/bin/gamemode"
        "$mod, G, exec, ${hyprgamemode}/bin/hyprgamemode"
        "$mod, D, exec, ${showdesktop}/bin/showdesktop"

        "$mod+CTRL, L, exec, ${pkgs.hyprlock}/bin/hyprlock"
        "$mod+CTRL, space, global, kando:example-menu"
        # "$mod CTRL, space, global, kando -m example-menu"

        # Another cool config for adding description/category to keybind helper
        # https://github.com/HyDE-Project/HyDE/blob/master/Configs/.config/hypr/keybindings.conf

        # "$mod,Return,exec,${terminal}"
        # "$mod,W,exec,${browser}"
        # "$mod,K,exec,list-keybinds"
        # "$mod SHIFT,Return,exec,rofi-launcher"
        # "$mod SHIFT,W,exec,web-search"
        # "$mod ALT,W,exec,wallsetter"
        # "$mod,Y,exec,kitty -e yazi"

        # "$mod,D,exec,discord"
        # "$mod,O,exec,obs"
        # "$mod,G,exec,gimp"
        # "$mod,T,exec,pypr toggle term"
        # "$mod,M,exec,pavucontrol"

        # "$mod,V,exec, cliphist list | rofi -dmenu | cliphist decode | wl-copy"
        # "$mod SHIFT,SPACE,movetoworkspace,special"
      ];

      # binde = [
      #   # Built-in Zoom Keybinds
      #   "$mod ALT, 0, exec, hyprctl -q keyword cursor:zoom_factor 1"
      #   "$mod ALT, equal, exec, hyprctl -q keyword cursor:zoom_factor $(hyprctl getoption cursor:zoom_factor | awk '/^float.*/ {print $2 * 1.1}')"
      #   "$mod ALT, minus, exec, hyprctl -q keyword cursor:zoom_factor $(hyprctl getoption cursor:zoom_factor | awk '/^float.*/ {print $2 * 0.9}')"
      # ];

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
        "$mod, mouse:272, movewindow" # Move window
        "$mod, mouse:273, resizewindow" # Resize window regardless of proportion
        "$mod+SHIFT, mouse:273, resizewindow 1" # Resize window proportionally
      ];

    };
    extraConfig = ''
      # Resize Controls

      # will switch to a submap called resize
      bind = $mod, R, submap, resize

      # will start a submap called "resize"
      submap = resize

      # sets repeatable binds for resizing the active window
      binde = , L, resizeactive, 60 0
      binde = , H, resizeactive, -60 0
      binde = , K, resizeactive, 0 -60
      binde = , J, resizeactive, 0 60

      # use reset to go back to the global submap
      bind =, escape, submap, reset

      # will reset the submap, which will return to the global submap
      submap = reset
    '';
  };

}
