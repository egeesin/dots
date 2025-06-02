{username, host, ...}:
let
inherit (import ../../../hosts/${host}/variables.nix) wallpaper ;

in {
  programs.hyprlock = {
    enable = true;
    settings = {
      general = {
        grace = 1;
        fractional_scaling = 2;
        immediate_render = true;
      };

      background = {
        monitor = "";
        # NOTE: use only 1 path
        # path = "${wallpaper}"; # current wallpaper, conflicts with stylix

        # color = "rgb(0,0,0)"; # color will be rendered initially until path is available # conflicts with stylix

        # all these options are taken from hyprland, see https://wiki.hyprland.org/Configuring/Variables/#blur for explanations
        blur_size = 3;
        blur_passes = 2; # 0 disables blurring
        noise = 0.0117;
        contrast = 1.3000; # Vibrant!!!
        brightness = 0.8000;
        vibrancy = 0.2100;
        vibrancy_darkness = 0.0;
      };

      # Date
      label = [
        {
          monitor = "";
          text = "cmd[update:18000000] echo \"<b> \"$(date +'%A, %-d %B')\" </b>\"";
          # color = "rgb(9A5BDD)"; # conflicts with stylix
          font_size = 18;
          font_family = "sans-serif";
          position = "0, -120";
          halign = "center";
          valign = "center";
        }
      # Hour-Time
        {
          monitor = "";
          # text = "cmd[update:1000] echo \"$(date +\"%H\")\"";
          text = "cmd[update:1000] echo \"$(date +\"%I\")\""; #AM/PM
      	  # color = rgba(255, 185, 0, .8)
          # color = "rgb(9A5BDD)"; # conflicts with stylix
          font_size = 240;
          # font_family = "monospace";
          font_family = "sans-serif";
          position = "0, -100";
          halign = "center";
          valign = "top";
        }
      # Minute-Time
        {
          monitor = "";
          text = "cmd[update:1000] echo \"$(date +\"%M\")\"";
          #color = rgba(15, 10, 222, .8)
          color = "rgb(7D4AB4)";
          font_size = "240";
          # font_family = "monospace";
          font_family = "sans-serif";
          position = "0, -450";
          halign = "center";
          valign = "top";
        }
      # Seconds-Time
        {
          monitor = "";
          # text = "cmd[update:1000] echo \"$(date +\"%S\")\""
          text = "cmd[update:1000] echo \"$(date +\"%S %p\")\""; #AM/PM
          # color = "rgb(3B2355)"; # conflicts with stylix
          font_size = 50;
          # font_family = "monospace";
          font_family = "sans-serif";
          position = "0, -450";
          halign = "center";
          valign = "top";
        }

      # USER
        {
          monitor = "";
          text = "  $USER";
          # color = "rgb(9A5BDD)"; # conflicts with stylix
          font_size = 24;
          font_family = "sans-serif";
          position = "0, 200";
          halign = "center";
          valign = "bottom";
        }
      ];

      input-field = {
        monitor = "";
        size = "300, 60";
        outline_thickness = 2;
        dots_size = 0.2; # Scale of input-field height, 0.2 - 0.8
        dots_spacing = 0.2; # Scale of dots' absolute size, 0.0 - 1.0
        dots_center = true;
        # outer_color = "rgb(3B2355)"; # conflicts with stylix
        # inner_color = "rgba(255, 255, 255, 0.1)"; # conflicts with stylix
        # font_color = "rgb(9A5BDD)"; # conflicts with stylix
        capslock_color = "rgb(255,255,255)";
        fade_on_empty = false;
        font_family = "sans-serif";
        placeholder_text = "<span foreground=\"##ffffff99\">🔒 Type Password</span>";
        hide_input = false;
        position = "0, 100";
        halign = "center";
        valign = "bottom";
      };

      # uptime
      # label = {
      #     monitor = "";
      #     text = "cmd[update:60000] echo \"<b> \"$(uptime -p || $Scripts/UptimeNixOS.sh)\" </b>\"";
      #     color = "rgb(9A5BDD)";
      #     font_size = 18;
      #     font_family = "Inter Italic";
      #     position = "0, 0";
      #     halign = "right";
      #     valign = "bottom";
      # };

      # weather edit the scripts for locations
      # weather scripts are located in ~/.config/hypr/UserScripts Weather.sh and/or Weather.py
      # see https://github.com/JaKooLit/Hyprland-Dots/wiki/TIPS#%EF%B8%8F-weather-app-related-for-waybar-and-hyprlock
      # label = {
      #     monitor = "";
      #     text = "cmd[update:3600000] [ -f \"/home/${username}/.cache/.weather_cache\" ] && cat \"$HOME/.cache/.weather_cache\"";
      #     color = "rgb(9A5BDD)";
      #     font_size = 18;
      #     font_family = "Inter Italic";
      #     position = "50, 0";
      #     halign = "left";
      #     valign = "bottom";
      # };
    };
  };
}
