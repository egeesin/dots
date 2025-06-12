{
# host,
...}:
# let
  # inherit (import ../../../hosts/${host}/variables.nix);
# in {
{
  imports = [
    ./hyprland.nix
    ./plugins.nix
    ./hyprshell.nix
    ./binds.nix
    ./windowrules.nix
    ./hyprlock.nix
    ./hypridle.nix
    # animChoice
    ./animations.nix
    # ./hyprpaper.nix # conflicts with stylix enabled
  ];
}
