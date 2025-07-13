{
# host,
...}:
# let
  # inherit (import ../../../hosts/${host}/var.nix);
# in {
{
  imports = [
    ./land.nix
    ./plugin.nix
    ./shell.nix
    ./bind.nix
    ./window.nix
    ./lock.nix
    ./idle.nix
    # animChoice
    ./anim.nix
    # ./paper.nix # conflicts with stylix enabled
  ];
}
