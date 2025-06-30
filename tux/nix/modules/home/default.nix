{
  pkgs,
  inputs,
  ...
}: {
  nixpkgs.config.allowUnfree = true; 
  imports = [
    ./bash.nix
    ./bat.nix
    ./btop.nix
    ./direnv.nix
    ./helix.nix
    ./nix-index.nix
    # ./xdg.nix # Adds preconfigured read-only mime file
    ./alacritty.nix
    ./darkman.nix
    ./mpv.nix
    ./vcs.nix
    ./hyprland
    ./starship.nix
    ./swaync.nix
    ./udiskie.nix
    ./virtmanager.nix
    ./easyeffects.nix
    ./wlogout
    # waybarChoice
    ./waybar.nix
    # ./yazi
    # ./zoxide.nix
    # ./zsh
    ./theming.nix
  ];

  # Home manager option search
  # https://home-manager-options.extranix.com/
  # 
  # Home manager wiki
  # https://nixos.wiki/wiki/Home_Manager
  home.sessionPath = [
    "$HOME/.dots/bin/"
  ];
  home.sessionVariables = {
    GTK_USE_PORTAL = 1;
    EDITOR = "hx"; # helix
    BROWSER = "zen-beta";
    TERMINAL = "alacritty";
  };

  xdg.configFile = {
    "television/nix_channels.toml".text = ''
    [[cable_channel]]
    name = "nixpkgs"
    source_command = "nix-search-tv print"
    preview_command = "nix-search-tv preview {}"
    '';
  };
 
  home.packages = with pkgs; [
    inputs.zen-browser.packages."${system}".beta
    # inputs.nix-software-center.packages.${system}.nix-software-center
    # inputs.nixos-conf-editor.packages.${system}.nixos-conf-editor
    inputs.tuime.defaultPackage.${system}
  ];
}
