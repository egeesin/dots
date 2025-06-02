{
  inputs,
  host,
  osConfig,
  # config,
  # lib,
  pkgs,
  # pkgs-unstable,
  ...
}: let
  # pluginsAsNixpkgs = pkgs.hyprlandPlugins;
  # pluginsAsFlake = inputs.hyprland-plugins.packages.${pkgs.system}; # From flake
  hyprlandPackage = inputs.hyprland.packages.${pkgs.system}.default;
  inherit
    (import ../../../hosts/${host}/variables.nix)
    # browser
    # editor
    extraMonitorSettings
    # keyboardLayout
    # keyboardVariant
    # keyboardOptions
    # wallpaper
    ;
in {
  home.packages = (with pkgs; [
    wl-clipboard
    hyprpaper
    hyprsunset # https://wiki.hyprland.org/Hypr-Ecosystem/hyprsunset/
    grim
    slurp
    satty

    # nwg-menu # https://github.com/nwg-piotr/nwg-menu
    # nwg-displays # Output management utility for Sway and Hyprland
    # nwg-shell-config
    nwg-dock-hyprland # GTK3-based dock for Hyprland

    ydotool # Generic Linux command-line automation tool (no X!)
    hyprpolkitagent # A polkit authentication agent written in QT/QML
    hyprland-qtutils  # needed for banners and ANR messages / only available on 25.05 or unstable atm
    kando # Cross-Platform Pie Menu
  # ]) ++ (with pkgs-unstable; [
  ]);
  systemd.user.targets.hyprland-session.Unit.Wants = [
    "xdg-desktop-autostart.target"
  ];
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
  wayland.windowManager.hyprland = {
    enable = true;
    package = hyprlandPackage;
    portalPackage = inputs.hyprland.packages.${pkgs.system}.xdg-desktop-portal-hyprland;
    # package = pkgs.hyprland;
    # package = inputs.hyprland.packages.${pkgs.stdenv.hostPlatform.system}.hyprland;
    systemd = {
      enable = true; # if UWSM enabled, disable this
      enableXdgAutostart = true;
      variables = ["--all"];
    };
    xwayland.enable = true;
    # plugins = (with pluginsAsNixpkgs; [
    #   # https://github.com/hyprwm/hyprland-plugins#plugin-list
    #   # https://github.com/hyprland-community/awesome-hyprland
    #   hyprbars # adds window bar
    #   csgo-vulkan-fix # force apps to a fake resolution without them realizing it.
    #   hyprwinwrap # Desktop environment background (wayland equivalent of xwinwrap, alternative to mpvwallpaper)
    #   # hyprscroller # adds scrolling layout like niri (WIP) # Available as nixpkgs https://github.com/dawsers/hyprscroller
    # ]) ++ (with pluginsAsFlake; [
    #   hyprscrolling # adds scrolling layout like niri (WIP) # Available as flake

    # ]) ++ (with pkgs; [
    #   waycorner # Hot corners for Wayland
       
    # ]) ++ [
    #   # hyprkool-plugin # replicate the feel of kde activities and desktop grid layout
    #   inputs.hyprkool.packages.${pkgs.system}.default
    #   inputs.hypr-dynamic-cursors.packages.${pkgs.system}.hypr-dynamic-cursors # From flake
    #   inputs.Hyprspace.packages.${pkgs.system}.Hyprspace # macOS/KDE like mission control thingy # from flake
    # ];

    settings = {
      # "$mainMod" = "SUPER"; # Sets "Windows" key as main modifier
      # experimental.xx_color_management_v4 = true;
      # experimental.wide_color_gamut = true;
        monitor = [
        # ",preferred,0x0,1.0"
        "DP-1,preferred,0x0,1.0"
        "HDMI-A-1,1920x1080@60.0,1920x0,1.0,transform,1"
      ];
      cursor = {
        sync_gsettings_theme = true;
        no_warps = true;
        # no_hardware_cursors = 2; # change to 1 if want to disable
        # warp_back_after_non_mouse_input = true;
        default_monitor = "DP-1";
        enable_hyprcursor = true;
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
      debug = {
        disable_logs = false;
        # damage_tracking = 0;
        # Electron apps like Discord in Wayland (with Nvidia) sometimes flickers.
        # https://github.com/hyprwm/Hyprland/issues/6701#issuecomment-2198646262 
    }; 

      # https://wiki.hyprland.org/Configuring/Variables/#input
      input = {
        kb_layout = "${osConfig.services.xserver.xkb.layout}";
        kb_variant = "${osConfig.services.xserver.xkb.variant}";
        kb_options = "${osConfig.services.xserver.xkb.options}";
        # kb_layout = "${keyboardLayout}";
        # kb_variant = "${keyboardVariant}";
        # kb_options = "${keyboardOptions}";
        # kb_rules =
        repeat_rate = 40;
        repeat_delay = 300;
        force_no_accel = 1;
        
        numlock_by_default = true;
        follow_mouse = 1;
        sensitivity = 0; # -1.0 - 1.0, 0 means no modification.
        touchpad = {
          # natural_scroll = true;
          # disable_while_typing = true;
          # scroll_factor = 0.8;
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
      general = {
        gaps_in = 5;
        gaps_out = 20;

        border_size = 2;
    
        # "col.active_border" = rgba(33ccffee) rgba(00ff99ee) 45deg
        # "col.inactive_border" = rgba(595959aa)
        # "col.active_border" = rgba(1998eeee) rgba(e1998eee) 60deg
        # "col.inactive_border" = rgba(595959aa) rgba(000000aa) 60deg
         
        # "col.active_border" = "rgba(FFBA63ee) rgba(e1998eee) 60deg"; # conflicts with stylix
        # "col.inactive_border" = "rgba(031C1Faa) rgba(031E20aa) 60deg"; # conflicts with stylix


        # Set to true enable resizing windows by clicking and dragging on borders and gaps
        resize_on_border = true;

        # Please see https://wiki.hyprland.org/Configuring/Tearing/ before you turn this on
        allow_tearing = false;

        layout = "dwindle";
        # layout = master
      };
      # https://wiki.hyprland.org/Configuring/Variables/#variable-types for info about colors
      misc = {
        # background_color = "0x2C5C4A"; # conflicts with stylix
        vrr = 1; # Enable Adaptive Sync  0 - off, 1 - on, 2 - fullscreen only, 3 - fullscreen with video or game content type [0/1/2/3]
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
        rounding = 10;

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
        {
          name = "steelseries-steelseries-prime";
          sensitivity = -0.25;
        }
        {
          name = "razer-razer-ornata-v2";
          repeat_rate = 40;
          repeat_delay = 300;
          middle_button_emulation = 0;
        }
      ];

      env = [
        "NIXOS_OZONE_WL, 1"
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
        "MOZ_ENABLE_WAYLAND, 1"

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
        "[workspace current silent] ${pkgs.wl-clipboard}/bin/wl-paste --type text --watch cliphist store" # Stores only text data
        "[workspace current silent] ${pkgs.wl-clipboard}/bin/wl-paste --type image --watch cliphist store" # Stores only image data
        "[workspace current silent] dbus-update-activation-environment --all --systemd WAYLAND_DISPLAY XDG_CURRENT_DESKTOP"
        "[workspace current silent] systemctl --user import-environment WAYLAND_DISPLAY XDG_CURRENT_DESKTOP"
        "[workspace current silent] systemctl --user start hyprpolkitagent"
        "[workspace current silent] gnome-keyring-daemon --start --components=secrets"
        "export SSH_AUTH_SOCK"
        "[workspace current silent] $POLKIT_BIN"
        "${pkgs.hyprpaper}/bin/hyprpaper init"
        # "syshud"
        "[pin] waybar"
        # "[pin] nwg-dock-hyprland -r -i 35 -ml 12 -mr 12 -mb 12 -nolauncher -x -l bottom"
        # "[pin] nwg-dock-hyprland -a 'start' -p 'left' -c 'nwggrid' -d -f -i 36 -lp start -o 'DP-1' -w 10"
        "[workspace current silent] swaync"
        "[workspace current silent] kando"
        # "[workspace current silent] nm-applet --indicator"
        # "${pkgs.hyprsunset}"
        "[workspace current silent] hypridle"
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
}
