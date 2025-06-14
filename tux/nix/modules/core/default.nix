{inputs, ...}: {
  imports = [
    ./boot.nix
    ./greetd.nix
    ./hardware.nix
    ./network.nix
    ./nh.nix
    ./packages.nix
    ./printing.nix
    ./security.nix
    ./services.nix
    ./starship.nix
    ./gaming.nix
    ./syncthing.nix
    ./system.nix
    ./user.nix
    ./virtualisation.nix
    ./xserver.nix
    ./xdg.nix
    ./flatpak.nix # depends on xdg
    ./theming.nix
  ];
}
