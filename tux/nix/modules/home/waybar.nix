# Based on https://gitlab.com/Zaney/zaneyos/-/blob/main/modules/home/waybar/waybar-simple.nix?ref_type=heads
{
  osConfig,
  config,
  pkgs,
  lib,
  host,
  ...
}: let
  inherit (import ../../hosts/${host}/variables.nix) clock24h startMenu;
  # createBar = waybarConfig: output: position: waybarConfig // { output = output; position = position; };
  # primaryBar = {
    
  # };
  # secondaryBar = {
    
  # }
in
 {
  # Cool multi-monitor waybar config: https://github.com/Cody-W-Tucker/nix-config/blob/6fe28b41301f3532edb44934a811d5427426d263/cody/ui/waybar.nix#L277C1-L281C67
  
  # wayland.windowManager.hyprland.settings.exec-once = [ "${pkgs.waybar}/bin/waybar"];
  # stylix.targets.waybar = {
  #   enableLeftBackColors = false;
  #   enableRightBackColors = false;
  #   enableCenterBackColors = false;
  # };
  programs.waybar = {
    enable = true;
    package = pkgs.waybar.overrideAttrs (oa: {
      mesonFlags = (oa.mesonFlags or []) ++ ["-Dexperimental=true"];
    });
    settings = [
      # monitor1 = createBar primaryBar "DP-1" "bottom";
      # monitor2 = createBar secondaryBar "HDMI-A-1" "bottom";
      {
        mod = "dock";
        exclusive = true;
        gtk-layer-shell = true;
        height = 36;
        # height = 41;
        layer = "bottom";
        margin-bottom = -1;
        passthrough = false;
        position = "bottom";
        fixed-center = false;

        modules-left = [
          "group/boot"
          # "custom/startbutton"
          "hyprland/workspaces"
          "hyprland/submap"
          "wlr/taskbar"
        ];
        modules-center = [ ];
        modules-right = [
          "systemd-failed-units"
          "gamemode"
          "privacy"
          "tray"
          "group/component-stats"
          "group/audio"
          "battery"
          # "group/datetimeV"
          "group/datetime"
          "group/system"
        ];
       "group/datetime" = {
          modules = [
            "clock"
            "custom/weather"
            "clock#date"
          ];
          orientation = "horizontal";
          drawer = {
            transition-duration = 300;
            transition-left-to-right = false;
            children-css = "";
          };
        };
       "group/datetimeV" = {
          modules = [
            "clock#hour"
            "clock#minute"
          ];
          orientation = "vertical";
        };
        "group/component-stats" = {
          # click-to-reveal = true;
          orientation = "inherit";
          modules = [
            "memory"

            "custom/nvidia"
            "temperature"
            "load"
            "cpu"
            "disk"
          ];
          drawer = {
            transition-duration = 300;
            transition-left-to-right = false;
            children-css = "";
          };
        };
        "group/system" = {
          # click-to-reveal = true;
          orientation = "inherit";
          modules = [
            "custom/notification"

            "idle_inhibitor"
            "bluetooth"
            "custom/vpn"
            "network"
            "backlight"
            # "backlight/slider"
            # "custom/contrast"
            "hyprland/language"
          ];
          drawer = {
            transition-duration = 300;
            transition-left-to-right = false;
            children-css = "";
          };
        };
        "group/audio" = {
          # click-to-reveal = true;
          # orientation = "vertical";
          orientation = "inherit";
          modules = [
            "wireplumber"
            "mpris"
            # "custom/progress"
          ];
          drawer = {
            transition-duration = 300;
            transition-left-to-right = false;
            children-css = "";
          };
        };
        "group/boot" = {
          # click-to-reveal = true;
          # orientation = "vertical";
          orientation = "inherit";
          modules = [
            "custom/startbutton"
            "custom/exit"
            "user"
          ];
          drawer = {
            transition-duration = 300;
            transition-left-to-right = true;
            children-css = "";
          };
        };
        "custom/startbutton" = {
          # format = ""; # Nix snowflake logo
          # format = "⬢"; # Just hexagon
          # format = "⌘"; # cmd symbol
          # format = ""; # Apple
          # format = "❄️"; # Snowflake emoji
          # format = "🇹🇷"; # Turkish Flag
          format = "😎"; # Cool sunglasses emoji
          # format = "🃏"; # Joker wildcard emoji
          # format = "🗿"; # Moyai wildcard emoji
          # format = "⚽"; # Soccerball emoji
          # format = "🌍"; # Globe emoji
        
          # on-click = "${launcherMenu}";
          on-click = "${startMenu}";
          tooltip = false;
        };
        "clock" = {
          "timezones" = [
            "Europe/Istanbul"
            "Etc/UTC"
            "America/New_York"
            "America/Los_Angeles"
            "Asia/Tokyo"
          ];
          actions = {
            on-click-backward = "tz_down";
            on-click-forward = "tz_up";
          };
          
          # format = "{:%R\n %d.%m}";
          # format = "{:%d/%m %R}";
          format =
              if clock24h == true
              then ''{:L%H:%M %a}''
              else ''{:L%I:%M %a}'';
          format-alt =
              if clock24h == true
              then ''{:L%H:%M %Z}''
              else ''{:L%I:%M %p %Z}'';

          tooltip-format = "{tz_list}";

          # format-alt = "{:%a %d %b}";
          # format-alt-click = "click-right";
        };
        "clock#date" = {
          format = "{:%d %b}";
          format-alt = "{:%A, %B %d, %Y}";
          # format-alt = "{:%A, %B %d, %Y}";
          actions = {
            on-click-right = "mode";
            on-scroll-down = "shift_down";
            on-scroll-up = "shift_up";
          };
          calendar = {
            mode = "year";
            mode-mon-col = 3;
            on-click-right = "mode";
            on-scroll = 1;
            weeks-pos = "right";
            format = {
              months = "<span color='#${config.lib.stylix.colors.base06}'><b>{}</b></span>";
              days = "<span color='#${config.lib.stylix.colors.base03}'><b>{}</b></span>";
              weeks = "<span color='#${config.lib.stylix.colors.base0B}'><b>W{}</b></span>";
              weekdays = "<span color='#${config.lib.stylix.colors.base13}'><b>{}</b></span>";
              today = "<span color='#${config.lib.stylix.colors.base17}'><b>{}</b></span>";
              # days = "<span color='#ecc6d9'><b>{}</b></span>";
              # months = "<span color='#ffead3'><b>{}</b></span>";
              # today = "<span color='#ff6699'><b><u>{}</u></b></span>";
              # weekdays = "<span color='#ffcc66'><b>{}</b></span>";
              # weeks = "<span color='#99ffdd'><b>W{}</b></span>";
            };
          };
          # tooltip-format = "<tt><small>{calendar}</small></tt>";
          tooltip-format = "<big>{:%A, %d %B %Y }</big>\n<tt><small>{calendar}</small></tt>";
        };
        "clock#hour" = {
          # format = "{:%H}";
          format =
              if clock24h == true
              then ''{:L%H}''
              else ''{:L%I}'';
          tooltip-format = "{:%b %d}";
          interval = 1;
          tooltip = true;
        };
        "clock#minute" = {
          format = "{:%M}";
          tooltip-format = "{:%a}";
          interval = 1;
          tooltip = true;
        };
        network = {
          interval = 30;
          # format-disconnected = "󰌙";
          format-disconnected = "󰤮 ";
          # format-ethernet = " ";
          format-ethernet = "󰈀";
          format-wifi = "{icon}";
          format-icons = [ "󰤯 " "󰤟 " "󰤢 " "󰤢 " "󰤨 " ];
          tooltip-format = "󰈀  {ifname}\nIP: {gwaddr}\nBandwidth: {bandwidthUpBytes}/{bandwidthDownBytes}";
          tooltip-format-wifi = "ESSID: {essid}\nFrequency: {frequency} GHz\nStrength: {signalStrength}\n{bandwidthUpBytes}/{bandwidthDownBytes}%\nIP: {ipaddr}";
          tooltip-format-disconnected =  "Disconnected";
          # on-click = "alacritty -T 'Floating Term nmtui' -e nmtui connect";
          # on-click-right = "rfkill toggle wifi";
        };
        bluetooth = {
        	format = "󰂯";
        	format-connected = "󰂱";
        	format-disabled = "󰂲";
        	format-icons = ["󰤾" "󰤿" "󰥀" "󰥁" "󰥂" "󰥃" "󰥄" "󰥅" "󰥆" "󰥈"];
        	format-off = "󰂲";  
        	format-on = "󰂯";

        	tooltip = "true"; 
        	tooltip-format = "{controller_alias}\t{controller_address}\n\n{num_connections} connected";
        	tooltip-format-disabled = ""; 
        	tooltip-format-off = ""; 
        	tooltip-format-on = "";
        	tooltip-format-connected = "{controller_alias}\t{controller_address}\n\n{num_connections} connected\n\n{device_enumerate}";

        	tooltip-format-enumerate-connected = "{device_alias}\t{device_address}";
        	tooltip-format-enumerate-connected-battery = "{device_alias}\t{device_address}\t{device_battery_percentage}%";
         	on-click-right = "sleep 0.1 && rfkill toggle bluetooth";
        };
        memory = {
          # format = " {percentage}%";
          format = "  {percentage}";
          interval = 2;
          min-length = 3;
          max-length = 10;
          tooltip = true;
          # tooltip-format = "RAM - {used:0.1f}GiB used";
          tooltip-format = "RAM:\nUsed: {used} GiB\nAvailable: {avail} GiB\n\nSwap:\nUsed: {swapUsed} GiB\nAvailable: {swapAvail} GiB";
        };
        disk = {
          format = "󰋊 {percentage_used}";
          interval = 30;
          min-length = 3;
          path = "/";
          tooltip = true;
          tooltip-format = "{used}/{total}";
          # tooltip-format = "Available {free} of {total}";
          unit = "GB";
          states = {
            empty = 25;
            halfway = 50;
          };
        };
        load = {
          "interval" = 1;
          "format" = "{load1} {load5} {load15}";
        };
        cpu = {
          format = " {usage}";
          on-click = "sleep 0.1 && alacritty -T 'Floating Term btop' -e btop";
          interval = 2;
          min-length = 3;
          max-length = 10;
        };
        battery = {
          # bat = "BAT1";
          # adapter = "ACAD";
          tooltip = true;
          tooltip-format = "{timeTo}\nPower: {power} Watt";
          # format = "{icon} {capacity}%";
          format = "{icon} {capacity}";
          format-alt = "{time} {icon}";
          format-charging = "󰂄 {capacity}";
          format-full = " {capacity}";
          format-icons = [ "󰂎" "󰁺" "󰁻" "󰁼" "󰁽" "󰁾" "󰁿" "󰂀" "󰂁" "󰂂" "󰁹" ];
          format-plugged = " {capacity}";
          states = {
            critical = 15;
            good = 80;
            warning = 30;
          };
        };
        "custom/nvidia" = { # Requires nvidia-smi
          exec = "nvidia-smi --query-gpu=utilization.gpu,temperature.gpu --format=csv,nounits,noheader | sed 's/\\([0-9]\\+\\), \\([0-9]\\+\\)/\\1% 🌡️\\2°C/g'";
          # format = "GPU {}";
          format = " {}";
          interval = 2;
          tooltip = false;
        };
        wireplumber = {
          # format = "{icon} {volume}%";
          format = "{icon} {volume}";
          # format-muted = "";
          # format-muted = "";
          format-muted = " {volume}";
          on-click = "sleep 0.1 && helvum";
          on-click-right = "wpctl set-mute @DEFAULT_AUDIO_SINK@ toggle";
          max-volume = 150;
          scroll-step = 5;
          format-icons = [ "" "" "" ];
          # tooltip-format = "Current Volume: {volume}%";
          tooltip-format = "{node_name}: {volume}%";
          
        };
        pulseaudio = {
          # format = "{volume}% {icon}";
          format = "{icon} {volume} {format_source}";
          format-bluetooth = "{volume}{icon} {format_source}";
          format-bluetooth-muted = " {icon} {format_source}";
          format-muted = " {format_source}";
          # format-muted = " ";
          format-source = " {volume}";
          format-source-muted = "";
          format-icons = {
            headphone = "";
            hands-free = "";
            headset = "";
            phone = "";
            portable = "";
            car = "";
            default = [
              ""
              ""
              ""
            ];
          };
          max-volume = 150;
          on-click = "sleep 0.1 && pavucontrol";
          scroll-step = 5;
          tooltip-format = "Current Volume: {volume}%";
        };
        "mpris" = {
          format = "{player_icon} {dynamic}";
          format-paused = "<span foreground='#${config.lib.stylix.colors.base02}'><i>{dynamic}</i></span>";
          dynamic-order = ["title" "artist"];
          dynamic-separator = "<span foreground='#${config.lib.stylix.colors.base03}' weight='heavy'> • </span>";
          tooltip = false; # dynamic separator looks unformatted in tooltip
          "player-icons" =  {
        		"default"= "▶";
        		"mpv" = "🎵";
          };
          "status-icons" = {
        		"paused" =  "⏸";
        	};
          on-scroll-up = "playerctld shift";
          on-scroll-down = "playerctld unshift";
          max-length = 100;
        };
        "custom/progress" = {
          return-type = "json";
          exec = pkgs.writeShellScript "centWay" ''
            while :; do
              echo "{ \"text\" : \"_\" , \"class\" : \"$(playerctl --ignore-player firefox metadata --format 'cent{{ (position / 100) / (mpris:length / 100) * 100 }}' | cut -d. -f1)\" }"
              sleep 1
            done
          '';
        };
        # "image#cover" = {
        #   on-click = "pkill nsxiv || nsxiv /tmp/cover.jpg";
          # on-click-right = "spotify_player like";
          # on-click-middle = scripts.glavaShow;
        #   path = "/tmp/cover.jpg";
        #   size = 31;
        #   signal = 8;
        # };
        "hyprland/submap" = {
          format = "{}";
          max-length = 8;
          tooltip = false;
        };
        "hyprland/language" = {
          # keyboard-name = "at-translated-set-2-keyboard";
          format = "{short}";
          # format = "{}";
          # format-us = "US";
          # format-us-colemak_dh = "US-CDH";
          # format-tr-f = "TR-F"; # Turkish, F 
          # format-tr = "TR-Q"; # Turkish, QWERTY
          # format-tr-alt = "TR-AQ"; # Turkish (Alt-Q)
          # # format-tr-intl = "TR-INT"; # Turkish, (intl., with dead keys) 
          # # format-tr-sundeadkeys = "TR-SUN"; # Turkish, (Sun dead keys) 
          # # format-de-tr = "DE-TR"; # Germany (Turkish)
          # on-click = "commands.keyboardLayoutNext";
          # on-click-right = "commands.keyboardLayoutPrev";
        };
        "hyprland/workspaces" = {
          icon-size = 32;
          on-scroll-down = "hyprctl dispatch workspace r+1";
          on-scroll-up = "hyprctl dispatch workspace r-1";
          # spacing = 16;
          spacing = 12;
          # disable-scroll = true;
          # all-outputs = true;
          # active-only = false;
          format-icons = {
            # "1" = "";
            # "2" = "";
            # "3" = "";
            # "4" = "";
            # "5" = "";
            "1" = " ▴ ";
            "2" = " ⧫ ";
            "3" = " ⬣ ";
            "4" = " ❯ ";
            "5" = " ⋰ ";
            "6" = " ⋱ ";
            "7" = " ❮ ";
            "8" = " ⎔ ";
            "9" = " ◊ ";
            "10" = " ▿ ";
            "urgent" = "";
            "focused" = "";
            "default" = "";
            # "high-priority-named" = ["3" "4" "6" "7"];
          };
          # persistent-workspaces = {
          #    "DP-1" = [3];
          #    "HDMI-A-1" = [8]; 
          # };
        };
        "custom/weather" = {
          "exec" = "$\{HOME}/.dots/bin/waybar/get_weather.sh Golhisar+Turkey";
          "return-type" = "json";
          "format" = "{}";
          "tooltip" = true;
          "interval" = 3600;
        };
        "idle_inhibitor" = {
          format = "{icon}";
          format-icons = {
            activated = "󰛊";
            deactivated = "󰾫";
            # deactivated = " ";
            # activated = " ";
        	};
        	tooltip = false;
        };
        privacy = {
          icon-spacing = 4;
          icon-size = 18;
          transition-duration= 250;
          modules= [
            {
              type= "screenshare";
              tooltip= true;
              tooltip-icon-size= 24;
            }
            {
              type= "audio-out";
              tooltip= true;
              tooltip-icon-size= 24;
            }
            {
              "type" = "audio-in";
              "tooltip" = true;
              "tooltip-icon-size" = 24;
            }
          ];
        };
        "custom/vpn" = {
          format = " VPN";
          exec = "echo '{\"class\": \"connected\"}'";
          exec-if = "test -d /proc/sys/net/ipv4/conf/tun0";
          return-type = "json";
          interval = 5;
        };
        "backlight" = {
          format = "{icon} {percent}";
          interval = 3;
        	format-icons = [ "󰹐 " "󱩎 " "󱩏 " "󱩐 " "󱩑 " "󱩒 " "󱩓 " "󱩔 " "󱩕 " "󱩖 " ];
        	# on-scroll-down = "brightnessctl set 1%- && $HOME/.scripts/progressbar.sh --brightness 'eDP-1'";
        	# on-scroll-up = "brightnessctl set +1% && $HOME/.scripts/progressbar.sh --brightness 'eDP-1'";
        	on-scroll-down = "${lib.getExe pkgs.brightnessctl} set 5%-";
        	on-scroll-up = "${lib.getExe pkgs.brightnessctl} set +5%";
        	tooltip = false;
          # device = "amdgpu_bl1";
        };
        "backlight/slider" = {
          min = 0;
          max = 100;
          orientation = "horizontal";
          # device = "amdgpu_bl1";
        };
        "systemd-failed-units" = {
          hide-on-ok = true; # Do not hide if there is zero failed units.
          # format = "✗ {nr_failed}";
          format = " {nr_failed}";
          # format-ok = "✓";
          format-ok = "󰸞";
          system = true; # Monitor failed systemwide units.
          user = false; # Ignore failed user units.
        };
        "custom/notification" = {
          tooltip = false;
          format = "{icon}";
          # format = "{icon} {}";
          format-icons = {
            notification = " <span foreground='#${config.lib.stylix.colors.base0A}'><sup></sup></span>";
            none = " ";
            dnd-notification = "<span foreground='#${config.lib.stylix.colors.base0D}'> </span><span foreground='#${config.lib.stylix.colors.base0A}'><sup></sup></span>";
            dnd-none = "<span foreground='#${config.lib.stylix.colors.base0D}'> </span>";
            inhibited-notification = " <span foreground='#${config.lib.stylix.colors.base0A}'><sup></sup></span>";
            inhibited-none = " ";
            dnd-inhibited-notification = "<span foreground='#${config.lib.stylix.colors.base0D}'> </span><span foreground='#${config.lib.stylix.colors.base0A}'><sup></sup></span>";
            dnd-inhibited-none = "<span foreground='#${config.lib.stylix.colors.base0D}'> </span>";
          };
          return-type = "json";
          exec-if = "which swaync-client";
          exec = "swaync-client -swb";
          on-click = "sleep 0.1 && swaync-client -t -sw";
          on-click-right = "sleep 0.1 && swaync-client -d -sw";
          escape = true;
        };
        "custom/exit" = {
          tooltip = false;
          format = "{icon}";
          format-icons = " ";
          on-click = "sleep 0.1 && wlogout";
        };
        "user" = {
          "format" = "{user} (up {work_H}h ↑)"; # System uptime hours by day
          # "format" = "{user} (up {work_d} days ↑)"; # System startup days
          "interval" = 60;
          "height" = 30;
          "width" = 30;
          "icon" = true;
        };
        # "custom/contrast" = { # requires ddccontrol
        #   exec = "ddccontrol -r 0x12 dev:/dev/i2c-6 2>/dev/null | awk '/Control 0x12/ { split($3, a, \"/\"); print a[2] }'";
        #   exec-if = "sleep 1";
        #   format = "{icon}{text}%";
        #   format-icons = ["🔆"];
        #   interval = "once";
        #   on-scroll-up = "ddccontrol -r 0x12 -W +10 dev:/dev/i2c-6";
        #   on-scroll-down = "ddccontrol -r 0x12 -W -10 dev:/dev/i2c-6";
        #   on-click = "gddccontrol";
        # };
        temperature = {
          format = "{icon} {temperatureC}°C";
          format-critical = "{icon} {temperatureC}°C";
          critical-threshold = 85;
          # thermal-zone = 2;
          # hwmon-path = "/sys/class/hwmon/hwmon1/temp1_input";
          # hwmon-path-abs = "/sys/devices/platform/coretemp.0/hwmon";
          # input-filename = "temp2_input";
          format-icons = ["" "" "" "" ""];
          interval = 10;
          tooltip = false;
          on-click = "sleep 0.1 && alacritty -T 'Floating Term btop' -e btop";
        };
        tray = {
          icon-size = 18;
          spacing = 5;
          # show-passive-items = true;
          # smooth-scrolling-threshold = 1;
        };
        "wlr/taskbar" = {
          format = "{icon} {title:.17}";
          icon-theme = "Papirus-Dark";
          icon-size = 24;
          ignore-list = [
            # "Alacritty"
          ];
          rewrite = {
            "Alacritty" = "Terminal";
            "Firefox Web Browser" = "Firefox";
            "Foot Server" = "Terminal";
          };
          on-click = "activate";
          on-click-middle = "close";
          spacing = 3;
          tooltip-format = "{title}";
        };
        gamemode = {
          format = "{glyph}";
          format-alt = "{glyph} {count}";
          glyph = "";
          hide-not-running = true;
          use-icon = true;
          icon-name = "input-gaming-symbolic";
          icon-spacing = 4;
          icon-size = 20;
          tooltip = true;
          tooltip-format = "Games running = {count}";
        };
        # More 3rd party modules:
        # https://github.com/Alexays/Waybar/wiki/Module:-Custom:-Third-party
      }
    ];
    # style = concatStrings [ ''
    # style = let col = config.lib.stylix.colors; in lib.mkAfter ''
    style = lib.mkAfter ''

      /*
       * Variables
       */

      /*base background color*/
      @define-color bg_main rgba(25, 25, 25, 0.65);
      @define-color bg_main_tooltip rgba(0, 0, 0, 0.7);

      /*base background color of selections */
      @define-color bg_hover rgba(200, 200, 200, 0.3);
      /*base background color of active elements */
      @define-color bg_active rgba(100, 100, 100, 0.5);

      /*base border color*/
      @define-color border_main rgba(255, 255, 255, 0.2);

      /*text color for entries, views and content in general */
      @define-color content_main white;
      /*text color for entries that are unselected */
      @define-color content_inactive rgba(255, 255, 255, 0.25);

      /*
       * Globals
       */
      * { font-family: ${builtins.concatStringsSep "," (map (font: ''"${font}"'') osConfig.fonts.fontconfig.defaultFonts.sansSerif)}; }
      * {
      	text-shadow: none;
      	box-shadow: none;
        border: none;
        border-radius: 0;
      	font-family: sans-serif;
      	/* font-family: "Inter Nerd Font", "Segoe UI", "Ubuntu"; */
        /* font-weight: 600; */
        /* font-size: 13px; */ /* Stylix already adds this */
        /* font-size: 12px; */
      }

      window#waybar {
        padding-left: 5px;
        padding-right: 5px;
        /*
        padding-top: 5px;
        padding-bottom: 5px;
        */
        background: @base01;
        /* background: @bg_main; */
        border-top: 1px solid @border_main;
        color: @content_main;
      }

      tooltip {
        background: @bg_main_tooltip;
        border-radius: 5px;
        border-width: 1px;
        border-style: solid;
        border-color: @border_main;
      }
      tooltip label{ color: @content_main; }

      /*
       * Fonts
       */
      #cpu,
      #disk,
      #memory,
      #load,
      #custom-notification,
      #custom-exit,
      #temperature,
      #custom-nvidia,
      #pulseaudio,
      #wireplumber,
      #systemd-failed-units,
      #network,
      #bluetooth,
      #contrast {
        font-family: monospace;
      }
      #custom-startbutton {
      	font-family: "Twitter Color Emoji";
      	/* font-family: "Commit Mono"; */
        font-size: 24px;
      }

      /*
       * Geometry
       */
      #custom-notification,
      #custom-exit,
      #wireplumber,
      #clock,
      #battery,
      #workspaces button,
      #pulseaudio,
      #wireplumber,
      #language,
      #custom-contrast,
      #custom-nvidia,
      #temperature,
      #backlight,
      #network,
      #idle_inhibitor,
      #gamemode,
      #privacy,
      #bluetooth,
      #load {
        padding-left:5px;
        padding-right:5px;
        /*
        padding-top: 5px;
        padding-bottom: 5px;
        */
      }
      #tray{
        margin-left: 5px;
        margin-right: 5px;
        /*
        margin-top: 5px;
        margin-bottom: 5px;
        */
      }
      #tray > widget {
        padding-left: 3px;
        padding-right: 3px;
        /*
        padding-top: 3px;
        padding-bottom: 3px;
        */
      }
      #window {
        border-radius: 10px;
        margin-left: 20px;
        margin-right: 20px;
        /*
        margin-top: 20px;
        margin-bottom: 20px;
        */
      }
      #workspaces {
      	margin-right: 1.5px;
      	margin-left: 1.5px;
        /*
        margin-top: 1.5px;
        margin-bottom: 1.5px;
        */
      }
      #taskbar button {
      	min-width: 130px;
      	margin-left: 2px;
      	margin-right: 2px;
        /*
        margin-top: 2px;
        margin-bottom: 2px;
        */
        padding-left: 8px;
        padding-right: 8px;
        /*
        padding-top: 8px;
        padding-bottom: 8px;
        */
      }
      #custom-startbutton {
      	padding-left: 12px;
      	padding-right: 12px;
        /*
        padding-top: 12px;
        padding-bottom: 12px;
        */
      }

      #backlight-slider {
        padding-left: 5px;
        padding-left: 5px;
        min-width: 80px;
        min-height: 5px;
      }
      #backlight-slider slider {
        min-height: 0px;
        min-width: 0px;
        opacity: 0;
        background-image: none;
        border: none;
        box-shadow: none;
      }
      #backlight-slider through {
        min-width: 80px;
        border-radius: 5px;
        background-color: @base03;
        min-height: 5px;
      }
      #backlight-slider highlight {
        min-width: 80px;
        min-height: 5px;
        border-radius: 5px;
        background-color: @base13;
        color: @base0E;
      }

      /*
       * Transitions
       */
      #custom-exit,
      #custom-startbutton,
      #workspaces button,
      #taskbar button,
      #temperature,
      #tray > widget,
      #pulseaudio,
      #wireplumber,
      #contrast,
      #clock {
      	transition: all 0.25s cubic-bezier(0.165, 0.84, 0.44, 1);
      }

      /*
       * Colors
       */
      #pulseaudio:hover,
      #wireplumber:hover,
      #tray > widget:hover,
      #custom-notification:hover,
      #custom-exit:hover{
       	background: @bg_hover;
      }

      #workspaces button.active {
      	color: @content_main;
      	border-bottom: 3px solid white;
      }
      #workspaces button.focused { color: @bg_active; }
      #workspaces button.urgent {
      	background:  rgba(255, 200, 0, 0.35);
      	border-bottom: 3px dashed @warning_color;
      	color: @warning_color;
      }
      #custom-startbutton:hover,
      #workspaces button:hover,
      #taskbar button:hover {
        background: @bg_hover;
      	color: @content_main;
      }

      #workspaces { color: transparent; }
      #workspaces button { color: @content_inactive; }
      #workspaces button.empty { color: @base03; }
      #workspaces button.visible { color: @base0D; }
      #workspaces button.active { color: @base0A; }
      #workspaces button.urgent { color: @base0F; }
      #cpu.moderate{ color: @base0E; }
      #cpu.critical { color: @base08; }
      #tray > .passive { border-bottom: none; }
      #tray > .active { border-bottom: 3px solid white; }
      #tray > .needs-attention { border-bottom: 3px solid @warning_color; }
      #disk.empty { color: @base08; }
      /*#disk.halfway { }*/
      #network.disconnected { color: @base03; }
      /*#network.wifi, #network.ethernet { color: @base0D; }*/

      #clock {
        font-weight: 600;
      }

      #taskbar button {
      	border-bottom: 3px solid rgba(255, 255, 255, 0.3);
        font-weight: 400;
      }
      #taskbar button.active {
        border-bottom: 3px solid white;
        background: @bg_active;
      }
      #taskbar button:hover { border-bottom: 3px solid white; }

      #temperature.critical {
      	color: @warning_color;
      	/* font-size: initial; */
      	/* border-bottom: 3px dashed @warning_color; */
      }
 
      #tray menu menuitem:hover {
        background-color: @base02;
        color: @base0E;
      }
      #tray menu *:hover {
        background-color: @base01;
        color: inherit;
      }
      
      #tray > widget:hover { background: @bg_hover; }
      #tray > .passive { -gtk-icon-effect: dim; }
      #wireplumber.muted { color: @base03; }
      #idle_inhibitor.activated { color: @base0D; }
      #idle_inhibitor.deactivated { color: @base03; }
     
      #battery.warning { color: @base08; }
      #battery.critical {
        animation-name: blink;
        animation-duration: 1s;
        animation-timing-function: ease-out;
        animation-iteration-count: infinite;
        animation-direction: alternate;
      }
      @keyframes blink {
        to {
        color: @base01;
        }
      }
      '';
  };
}
