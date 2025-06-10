{
  inputs,
  host,
  config,
  # lib,
  pkgs,
  pkgs-unstable,
  ...
}: let
  # pluginsAsNixpkgs = pkgs.hyprlandPlugins;
  pluginsAsFlake = inputs.hyprland-plugins.packages.${pkgs.system}; # From flake
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
    slurp # Select a region
    satty # Screenshot annotation tool
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
    inputs.hyprshell.homeModules.hyprshell
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
      
    plugins =
      # https://github.com/hyprwm/hyprland-plugins#plugin-list
      # https://github.com/hyprland-community/awesome-hyprland
    # (with pluginsAsNixpkgs; [
    # ]) ++ (with pluginsAsFlake; [
    (with pluginsAsFlake; [ # Had to move all plugins from nixpkgs to flake source as hyprland (as flake) complains about mismatch versions of plugins
      hyprbars # adds window bar
      csgo-vulkan-fix # force apps to a fake resolution without them realizing it.
      # hyprwinwrap # Desktop environment background (wayland equivalent of xwinwrap, alternative to mpvwallpaper)
      xtra-dispatchers # adds some additional dispatchers
      # hyprscrolling # adds scrolling layout like niri (WIP) https://github.com/dawsers/hyprscroller # Can't build this atm for some reason
    ]) ++ [
      # inputs.hyprkool.packages.${pkgs.system}.default # Replicates the feel of KDE activities/desktop grid layout https://github.com/thrombe/hyprkool#example-configs
      inputs.hypr-dynamic-cursors.packages.${pkgs.system}.hypr-dynamic-cursors
      # inputs.Hyprspace.packages.${pkgs.system}.Hyprspace # macOS/KDE like mission control thingy https://github.com/KZDKM/Hyprspace#configuration
    ];

    settings = {
      debug = {
        disable_logs = false;
        # damage_tracking = 0;
        # Electron apps like Discord in Wayland (with Nvidia) sometimes flickers.
        # https://github.com/hyprwm/Hyprland/issues/6701#issuecomment-2198646262 
      }; 
      # "$mainMod" = "SUPER"; # Sets "Windows" key as main modifier
      # experimental.xx_color_management_v4 = true;
      # experimental.wide_color_gamut = true;
      plugin = {
        # hyprscrolling = {
        #   "fullscreen_on_one_column" = false; 
        # };
        dynamic-cursors = {
          # https://github.com/VirtCode/hypr-dynamic-cursors#configuration
          # mode = "rotate";
          # mode = "stretch";
          mode = "tilt";
          shake = {
            threshold = 10; # default 6, might be an issue for some games like minecraft
            enabled = false;
            nearest = true;
            effects = true;
          };
          # Should be good for SVG-based cursor themes and higher-res displays
          # https://github.com/VirtCode/hypr-dynamic-cursors#hyprcursor
          # hyprcursor = {
          #   nearest = true;
          #   enabled = true;
          #   resolution = -1;
          #   fallback = "clientside";
          # };
          shaperule = [
            "text, rotate:offset: 90" # apply a 90deg offset in rotate mod to the text shape
            "grab, stretch, stretch:limit:2000" # use stretch mode when grabbing, and set limit low
            # "clientside, none" # don't show any effects on clientside cursors
          ]; 
        };
        hyprbars = {
          bar_height = 20;
          bar_blur = true;
          bar_color = "rgb(${config.lib.stylix.colors.base00})";
          "col.text" = "rgb(${config.lib.stylix.colors.base03})";
          bar_padding = 8;
          bar_button_padding = 8;
          bar_title_enabled = true;
          bar_text_align = "left";
          bar_part_of_window = true;
          bar_precedence_over_border = true;
          icon_on_hover = true;
          # bar_text_font = "Jetbrains Mono";
          hyprbars-button = [
            "rgb(${config.lib.stylix.colors.base00}), 22, 󰖭, hyprctl dispatch killactive, rgb(${config.lib.stylix.colors.base03})"
            "rgb(${config.lib.stylix.colors.base00}), 18, 󰕔, hyprctl dispatch togglefloating, rgb(${config.lib.stylix.colors.base03})"
            "rgb(${config.lib.stylix.colors.base00}), 18, 󰘖, hyprctl dispatch fullscreen, rgb(${config.lib.stylix.colors.base03})"
          ];
        };
        "csgo-vulkan-fix" = {
          # https://github.com/hyprwm/hyprland-plugins/tree/main/csgo-vulkan-fix
          res_w = 1920;
          res_h = 1080;
          class = "cs2"; # not a regex! has to match initial_class exactly
          fix_mouse = true; # whether to fix the mouse position. a select few apps might be wonky with this.
        }; 
      };
      # https://github.com/mageowl/nix-config/blob/15b0a97759f82dfdee4dc2b74a209a171f6e38fa/modules/home/programs/hyprland/waycorner.nix#L10
      # waycorner = {
      #   enable = true;
      #   bottomRight = {
      #     enable = true;
      #     onEnter = ["wlogout"];
      #     # onEnter = ["systemctl" "sleep"];
      #   };
      #   bottomLeft = {
      #     enable = true;
      #     onEnter = [ startMenu ];
      #   };
      #   topRight = {
      #     enable = true;
      #     onEnter = ["swaync-client" "-t" "-sw"];
      #   };
      # };
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
        "[workspace current silent] ${pkgs.wl-clipboard}/bin/wl-paste --type text --watch cliphist store" # Stores only text data
        "[workspace current silent] ${pkgs.wl-clipboard}/bin/wl-paste --type image --watch cliphist store" # Stores only image data
        "[workspace current silent] dbus-update-activation-environment --all --systemd WAYLAND_DISPLAY XDG_CURRENT_DESKTOP"
        "[workspace current silent] systemctl --user import-environment WAYLAND_DISPLAY XDG_CURRENT_DESKTOP"
        "[workspace current silent] systemctl --user start hyprpolkitagent" # https://wiki.hyprland.org/Hypr-Ecosystem/hyprpolkitagent/#usage
        "[workspace current silent] gnome-keyring-daemon --start --components=secrets"
        # "export SSH_AUTH_SOCK"
        "[workspace current silent] $POLKIT_BIN"
        "${pkgs.hyprpaper}/bin/hyprpaper init"
        # "syshud"
        "[pin] waybar"
        # "[pin] nwg-dock-hyprland -r -i 35 -ml 12 -mr 12 -mb 12 -nolauncher -x -l bottom"
        # "[pin] nwg-dock-hyprland -a 'start' -p 'left' -c 'nwggrid' -d -f -i 36 -lp start -o 'DP-1' -w 10"
        "[workspace current silent] swaync"
        # "[workspace current silent] kando"
        # "[workspace current silent] nm-applet --indicator"
        # "${pkgs.hyprsunset}"
        "[workspace current silent] hypridle"
        # "[workspace current silent] zen"
        "[workspace current silent] hyprshell run &"
        "[workspace current silent] vesktop"
        "[workspace current silent] beeper --disable-gpu"
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
  programs.hyprshell = {
    enable = true;
    systemd.args = "-v";
    settings = {
      launcher = {
        max_items = 6;
        plugins.websearch = {
          enable = true;
          engines = [{
              name = "Unduck";
              url = "https://unduck.link?q=%s";
              key = "d";
          }];
        };
      };
      # window.switcher.enable = false;
    };
  };
}
