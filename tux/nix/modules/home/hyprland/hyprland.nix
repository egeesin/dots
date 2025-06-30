{
  inputs,
  host,
  config,
  lib,
  pkgs,
  pkgs-unstable,
  ...
}: let
  inherit
    (import ../../../hosts/${host}/variables.nix)
    # browser
    # editor
    extraMonitorSettings
    # startMenu
    # keyboardLayout
    # keyboardVariant
    # keyboardOptions
    # wallpaper
    ;
in {
  home.packages = (with pkgs; [
    wl-clipboard # Copy/paste utilities
    hyprpaper # Wallpaper utility
    hyprsunset # hyprsunset -t 3000 https://wiki.hyprland.org/Hypr-Ecosystem/hyprsunset/
    # grim # Grab images from Wayland compositor (replaced with grim-hyprland)
    (pkgs.writeShellScriptBin "grim" ''
      exec -a $0 ${inputs.grim-hyprland.packages.${pkgs.system}.default}/bin/grim "$@"
    '')
    wf-recorder # a utility program for screen recording of wlroots-based compositors | Usage: https://github.com/ammen99/wf-recorder#usage
    (pkgs.writeShellScriptBin "recorder-start" ''
        notify-send -t 5000 "Started recording (Press Mod+Shift+ESC to stop.)" && wf-recorder -g "$(slurp)" -a -f $(xdg-user-dir PICTURES)/Screenshots/$(date +"%Y-%m-%d_%Hh%Mm%Ss")-recording.mp4
    '')
    (pkgs.writeShellScriptBin "recorder-end" ''
      killall -s SIGINT wf-recorder
      notify-send -t 5000 "Stopped recording"
    '')
    slurp # Select a region
    # peek # Simple animated GIF screen recorder with an easy to use interface # Doesn't support Wayland natively, need GDK_BACKEND=x11 instead
    kooha # Elegantly record your screen
    wev # for testing and getting key names
    ydotool # Generic Linux command-line automation tool (no X!)

    walker # Wayland-native application runner
    # ulauncher # Fast application launcher for Linux, written in Python, using GTK

    nwg-dock-hyprland # GTK3-based dock for Hyprland
    # nwg-menu # menu start plugin for nwg-panel https://github.com/nwg-piotr/nwg-menu
    # nwg-displays # Output management utility for Sway and Hyprland
    # nwg-shell-config

    hyprpolkitagent # A polkit authentication agent written in QT/QML
    hyprland-qtutils  # needed for banners and ANR messages
    # kando # Cross-Platform Pie Menu
    # wlclock # Digital analog clock for Wayland desktops
    waycorner # Hot corners for wayland
  ]) ++ (with pkgs-unstable; [
    nwg-drawer # Application drawer for WLRoots based compositors like Sway, Hyprland
    satty # Screenshot annotation tool
  ]);
  # Place Files Inside Home Directory
  # home.file = {
  #   "Pictures/Wallpapers" = {
  #     source = ../../../wallpapers;
  #     recursive = true;
  #   };
  #   ".face.icon".source = ./face.jpg;
  #   ".config/face.jpg".source = ./face.jpg;
  # };
  #

  imports = [
    inputs.hyprland.homeManagerModules.default
  ];
  systemd.user.targets.hyprland-session.Unit.Wants = [
    "xdg-desktop-autostart.target"
  ];
  wayland.windowManager.hyprland = {
    enable = true;
    package = null;
    portalPackage = null;
    systemd = {
      enable = true; # if UWSM enabled, disable this
      enableXdgAutostart = true;
      variables = ["--all"];
    };
    xwayland = {
      enable = true;
      # hidpi = true;
    };
    settings = {
      debug = {
        disable_logs = true;
        # damage_tracking = 0;
        # Electron apps like Discord in Wayland (with Nvidia) sometimes flickers.
        # https://github.com/hyprwm/Hyprland/issues/6701#issuecomment-2198646262 
      }; 
      # "$mainMod" = "SUPER"; # Sets "Windows" key as main modifier
      # experimental.xx_color_management_v4 = true;
      # experimental.wide_color_gamut = true;
      monitor = [
        # ",preferred,0x0,1.0"
        "DP-1,preferred,0x0,1.0"
        "HDMI-A-1,1920x1080@60.0,1920x0,1.0,transform,1"
        "Unknown-1,disabled" # https://wiki.hyprland.org/FAQ/#workspaces-or-clients-are-disappearing-or-monitor-related-dispatchers-cause-crashes
      ];
      cursor = {
        sync_gsettings_theme = false;
        no_warps = true;
        # no_hardware_cursors = 2; # change to 1 if want to disable
        no_hardware_cursors = true; # WLR_NO_HARDWARE_CURSORS
        # warp_back_after_non_mouse_input = true;
        default_monitor = "DP-1";
        enable_hyprcursor = false;
      };
      # xwayland = {
      #   force_zero_scaling = true;
      # };
      workspace = [
        "1,defaultName:▴,persistent:true,monitor:DP-1"
        "2,defaultName:⧫,persistent:true,monitor:DP-1"
        "3,defaultName:⬣,persistent:true,monitor:DP-1,default:true"
        "4,defaultName:❯,persistent:true,monitor:DP-1"
        "5,defaultName:⋰,persistent:true,monitor:DP-1"
        "6,defaultName:⋱,persistent:true,monitor:HDMI-A-1"
        "7,defaultName:❮,persistent:true,monitor:HDMI-A-1"
        "8,defaultName:⎔,persistent:true,monitor:HDMI-A-1,default:true"
        "9,defaultName:◊,persistent:true,monitor:HDMI-A-1"
        "10,defaultName:▿,persistent:true,monitor:HDMI-A-1"
      ];
      # https://wiki.hyprland.org/Configuring/Variables/#input
      general = {
        gaps_in = 4;
        gaps_out = "10,20,10,20"; # Top/bottom 10, left/right 20
        # float_gaps = 4;
        border_size = 2;
        resize_on_border = true;
        extend_border_grab_area = 8;
        snap = {
          enabled = true;
          window_gap = 4;
          monitor_gap = 4;
          # respect_gaps = true;
        };

        # Stylix is enabled here: https://github.com/nix-community/stylix/blob/d73d8f6a4834716496bf8930a492b115cc3d7d17/modules/hyprland/hm.nix#L26
        # Applies base03 as inactive and base0D as active color

        # "col.inactive_border" = lib.mkForce "rgba(031C1Faa) rgba(031E20aa) 60deg"; # conflicts with stylix

        # "col.active_border" = "rgba(FFBA63ee) rgba(e1998eee) 60deg"; # conflicts with stylix
    
        # "col.active_border" = rgba(33ccffee) rgba(00ff99ee) 45deg
        # "col.inactive_border" = rgba(595959aa)
        # "col.active_border" = rgba(1998eeee) rgba(e1998eee) 60deg
        # "col.inactive_border" = rgba(595959aa) rgba(000000aa) 60deg
         
        # "col.active_border" = "rgba(FFBA63ee) rgba(e1998eee) 60deg"; # conflicts with stylix
        # "col.inactive_border" = "rgba(031C1Faa) rgba(031E20aa) 60deg"; # conflicts with stylix


        # Set to true enable resizing windows by clicking and dragging on borders and gaps

        # Please see https://wiki.hyprland.org/Configuring/Tearing/ before you turn this on
        allow_tearing = false;

        layout = "dwindle";
        # layout = master
      };
      # group = {
      # };
      # groupbar = {
      # };
      # https://wiki.hyprland.org/Configuring/Variables/#variable-types for info about colors
      misc = {
        disable_autoreload = false;
        # background_color = lib.mkForce "0x2C5C4A"; # Stylix uses base09 here
        # Enable Adaptive Sync
        # 0 - off
        # 1 - on
        # 2 - fullscreen only
        # 3 - fullscreen with video or game content type [0/1/2/3]
        vrr = 3;
        force_default_wallpaper = 1; # No hypr chan!
        disable_hyprland_logo = true; # If true disables the random hyprland logo / anime girl background. :(
        middle_click_paste = false; # Disabling this might not work in every environment.
        # font_family = Sans;
      };
      # See https://wiki.hyprland.org/Configuring/Dwindle-Layout/ for more
      dwindle = {
        pseudotile = true; # Master switch for pseudotiling. Enabling is bound to mainMod + P in the keybinds section below
        preserve_split = true; # You probably want this
      };
      decoration = {
        # border_part_of_window = false;
        rounding = 12;
        rounding_power = 8.0;

        # Change transparency of focused and unfocused windows
        active_opacity = 1.0;
        inactive_opacity = 1.0;

        shadow = {
          enabled = true;
          range = 300; 
          render_power = 4;
          # color = "rgba(031E20ff)";

          # color = rgba(1a1a1aaf)
          offset = "0 40";
          scale = 0.9;

          # range = 150 
          # render_power = 4
          # offset = 0 20
          # scale = 0.92
          # color = rgba(1998eeaf)

          # range = 4
          # render_power = 3
          # color = rgba(1a1a1aee)
        };

        # https://wiki.hyprland.org/Configuring/Variables/#blur
        blur = {
          enabled = true;
          size = 3;
          passes = 1;
          vibrancy = 0.1696;
        };
      };
      
      render = {
        explicit_sync = 1; # change to 1 to disable
        explicit_sync_kms = 1;
        direct_scanout = 0;
      };

      master = {
        new_status = "master";
        new_on_top = 1;
        mfact = 0.5;
      };

      # SUPPORT HYPRLAND https://hyprland.org/support/
      ecosystem = {
        no_update_news = true;
        no_donation_nag = true;
      };

      device = [
        # {
          # name = "steelseries-steelseries-prime";
          # sensitivity = -0.25;
        # }
        {
          name = "razer-razer-ornata-v2";
          middle_button_emulation = 0;
        }
      ];

      env = [
        "NIXOS_OZONE_WL, 1" # for any ozone-based browser & electron apps to run on wayland
        "MOZ_ENABLE_WAYLAND, 1" # for firefox to run on wayland
        "MOZ_WEBRENDER,1"
        "ELECTRON_OZONE_PLATFORM_HINT,auto"
        "XDG_SESSION_TYPE, wayland"
        "XDG_CURRENT_DESKTOP, Hyprland"
        "XDG_SESSION_DESKTOP, Hyprland"
        "CLUTTER_BACKEND, wayland"
        "_JAVA_AWT_WM_NONREPARENTING,1"
        "QT_WAYLAND_DISABLE_WINDOWDECORATION, 1"
        "QT_QPA_PLATFORM=wayland;xcb"
        "SDL_VIDEODRIVER, x11" # Games might require this
        "GDK_BACKEND, wayland, x11"

        "GDM_BACKEND, nvidia-drm"
        "__GLX_VENDOR_LIBRARY_NAME,nvidia"
 
        "DISABLE_QT5_COMPAT,0"

        # "GDK_SCALE,1"
        # "QT_SCALE_FACTOR,1"
        # "QT_AUTO_SCREEN_SCALE_FACTOR, 1"

        # "WLR_DRM_DEVICES,/dev/dri/card0:/dev/dri/card1"
        # "AQ_DRM_DEVICES,/dev/dri/card0:/dev/dri/card1"
      ];
      exec-once = [
        # "uwsm finalize"
        "${pkgs.wl-clipboard}/bin/wl-paste --type text --watch cliphist store" # Stores only text data
        "${pkgs.wl-clipboard}/bin/wl-paste --type image --watch cliphist store" # Stores only image data
        "dbus-update-activation-environment --all --systemd WAYLAND_DISPLAY XDG_CURRENT_DESKTOP"
        "systemctl --user import-environment WAYLAND_DISPLAY XDG_CURRENT_DESKTOP"
        "systemctl --user start hyprpolkitagent" # https://wiki.hyprland.org/Hypr-Ecosystem/hyprpolkitagent/#usage
        "gnome-keyring-daemon --start --components=secrets"
        # "export SSH_AUTH_SOCK"
        "$POLKIT_BIN"
        "${pkgs.hyprpaper}/bin/hyprpaper init"
        # "syshud"
        "[pin] waybar"
        # "[pin] nwg-dock-hyprland -r -i 35 -ml 12 -mr 12 -mb 12 -nolauncher -x -l bottom"
        # "[pin] nwg-dock-hyprland -a 'start' -p 'left' -c 'nwggrid' -d -f -i 36 -lp start -o 'DP-1' -w 10"
        "[workspace current silent] swaync"
        "[workspace current silent] nwg-drawer -r -c 8 -nofs"
        # "[workspace current silent] kando"
        # "[workspace current silent] nm-applet --indicator"
        # "${pkgs.hyprsunset}"
        "[workspace current silent] hypridle"
        "[workspace 1 silent] dolphin"
        # "[workspace 1 silent] io.elementary.files"
        "[workspace 2 silent] fooyin"
        "[workspace 3 silent] zen-beta --name zen-beta "
        "[workspace 7 silent] obsidian"
        "[workspace 8 silent] vesktop"
        "[workspace 8 silent] beeper --no-sandbox --disable-gpu"
        "[workspace 9 silent] thunderbird --name thunderbird"
        # "[workspace 9 silent] geary"
        "[workspace 9 silent] io.gitlab.news_flash.NewsFlash"
        "[workspace 10 silent] qbittorrent"
      ];

      # exec = [
        # "systemctl --user restart hyprpaper"
        # "systemctl --user restart waybar"
        # "systemctl --user restart kanshi" # Auto monitor config for hotswapping monitors
        # https://github.com/caffeine01/dotfiles/blob/main/hosts/envy/home/services/kanshi.nix
        # "systemctl --user restart iio-hyprland"  # Rotation detection for monitors/touch displays
        # https://github.com/caffeine01/dotfiles/blob/main/hosts/envy/home/services/iio-hyprland.nix
        # "systemctl --user restart wlsunset"
      # ];
 
    };
    extraConfig = ''
      ${extraMonitorSettings}
   '';
  };
  xdg.configFile = with config.lib.stylix.colors.withHashtag; {
    "nwg-drawer/drawer.css".text = lib.mkDefault ''
        window {
          color: ${base06};
          background-color: ${base00};
        }
        button {
          color: ${base04};
          background-color: ${base00};
        }
        button:hover {
          color: ${base04};
          background-color: ${base01};
        }
    '';
  };
}
