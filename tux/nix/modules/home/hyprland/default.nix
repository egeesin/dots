{
# host,
...}:
# let
  # inherit (import ../../../hosts/${host}/variables.nix);
# in {
{
  imports = [
    ./hyprland.nix
    ./binds.nix
    ./windowrules.nix
    ./hyprlock.nix
    ./hypridle.nix
    # animChoice
    ./animations.nix
    # ./hyprpaper.nix # conflicts with stylix enabled
  ];
}
