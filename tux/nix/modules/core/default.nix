{inputs, ...}: {
  imports = [
    ./boot.nix
    ./fonts.nix
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
    # inputs.minesddm.nixosModules.default
    inputs.minegrub-theme.nixosModules.default
    inputs.stylix.nixosModules.stylix
    ./theming.nix
  ];
  nixpkgs.overlays = [
   inputs.dolphin-overlay.overlays.default
   inputs.fancontrol-gui.overlays.default
  ];
}
