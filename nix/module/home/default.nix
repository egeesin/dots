{
  pkgs,
  inputs,
  ...
}: {
  nixpkgs.config.allowUnfree = true;
  imports = [
    ./shell.nix
    # ./yazi
    # ./zoxide.nix
    ./texteditor.nix
    ./terminal.nix
    ./mediaplayer.nix
    ./vcs.nix
    # waybarChoice
    ./theming.nix
  ];
  lib.mkIf pkgs.stdenv.targetPlatform.isDarwin = {
    inputs.mac-app-util.homeManagerModules.default
  };
  lib.mkIf pkgs.stdenv.targetPlatform.isLinux = {
    imports = [
      ./hypr
      # ./desktop.nix # Adds preconfigured read-only mime file
      ./swaync.nix
      ./udiskie.nix
      ./logoutmenu
      ./audio.nix
      # ./virtmanager.nix
      ./bar.nix
    ];
  };

  # Home manager option search
  # https://home-manager-options.extranix.com/
  #
  # Home manager wiki
  # https://nixos.wiki/wiki/Home_Manager
  home.packages = with pkgs; [
    inputs.zen-browser.packages."${system}".beta
    # inputs.nix-software-center.packages.${system}.nix-software-center
    # inputs.nixos-conf-editor.packages.${system}.nixos-conf-editor
    inputs.tuime.defaultPackage.${system}
  ];
}
