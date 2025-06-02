{host, ...}: let
  inherit (import ../../../hosts/${host}/variables.nix);
in {
  imports = [
    ./hyprland.nix
    ./hypridle.nix
    # animChoice
    ./animations.nix
    ./binds.nix
    ./hyprlock.nix
    # ./hyprpaper.nix # conflicts with stylix enabled
    ./windowrules.nix
  ];
}
