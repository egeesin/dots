# { username, ... }
{ lib, host, ... }
: let
  inherit (import ../../../host/${host}/var.nix) wallpaper;
in {
  services.hyprpaper = {
    enable = true;
    settings = {
      # https://wiki.hyprland.org/Hypr-Ecosystem/hyprpaper/
      preload = wallpaper;
      wallpaper = [
        "DP-1, ${wallpaper}"
        "HDMI-A-1, ${wallpaper}"
      ];
    };
  };
}
