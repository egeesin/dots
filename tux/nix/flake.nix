# Pitfall: Don't sudo nix flake update. If you did without sudo and having permission errors, do:
# $ sudo chown ege:users /home/ege/.dots/tux/nix/flake.lock
# and try again.

# System or user level rebuild commands
# $ sudo nixos-rebuild switch --flake ~/.dots/tux/nix#nvidia
# $ nix flake update --flake ~/.dots/tux/nix#nvidia
# $ home-manager switch --flake ~/.dots/tux/nix#nvidia # Works unless home-manager is a module.
 
# List all generations:
# $ sudo nix-env --list-generations --profile /nix/var/nix/profiles/system
 
# Set a default generation:
# $ sudo nix-env --profile /nix/var/nix/profiles/system --switch-generation X

# Remove specified generation:
# $ sudo nix-env --profile /nix/var/nix/profiles/system --delete -generation X Y Z

{
  description = "My system configuration";
  inputs = {
    # nixpkgs.url = "git+https://github.com/NixOS/nixpkgs?shallow=1&ref=nixos-24.11";
    nixpkgs.url = "git+https://github.com/NixOS/nixpkgs?shallow=1&ref=nixos-25.05";
    nixpkgs-unstable.url = "git+https://github.com/NixOS/nixpkgs?shallow=1&ref=nixos-unstable";
    # nix-darwin = {
    #   url = "github:LnL7/nix-darwin";
    #   inputs.nixpkgs.follows = "nixpkgs";
    # };
    # nix-on-droid = {
    #   url = "github:nix-community/nix-on-droid/release-24.05";
    #   inputs.nixpkgs.follows = "nixpkgs";
    # };
    fancontrol-gui.url = "github:JaysFreaky/fancontrol-gui";

    # nix-index-database = {
    #   url = github:nix-community/nix-index-database;
    #   inputs.nixpkgs.follows = "nixpkgs";
    # };

    # nix-index = {
    #   url = github:gvolpe/nix-index;
    #   inputs.nix-index-database.follows = "nix-index-database";
    #   inputs.nixpkgs.follows = "nixpkgs";
    # };

    # Fast nix search client
    # nix-search = {
    #   url = github:diamondburned/nix-search;
    #   inputs.nixpkgs.follows = "nixpkgs";
    # };

    # Nix linter
    # fenix = {
    #   url = github:nix-community/fenix;
    #   inputs.nixpkgs.follows = "nixpkgs";
    # };

    # statix = {
    #   url = github:nerdypepper/statix;
    #   inputs.fenix.follows = "fenix";
    #   inputs.nixpkgs.follows = "nixpkgs";
    # };
    #
    # nwg-drawer = {
    #   url = "github:caffeine01/nwg-drawer?ref=nix";
    #   inputs.nixpkgs.follows = "nixpkgs";
    #   inputs.systems.url = "github:nix-systems/default-linux";
    # };
     
    nix-software-center.url = "github:snowfallorg/nix-software-center";
    nixos-conf-editor.url = "github:snowfallorg/nixos-conf-editor";

    home-manager = {
      # url = "github:nix-community/home-manager/release-24.11";
      url = "github:nix-community/home-manager/release-25.05";
      # url = "github:nix-community/home-manager/"; # unstable
      inputs.nixpkgs.follows = "nixpkgs";
    };

    dolphin-overlay.url = "github:rumboon/dolphin-overlay";

    minegrub-theme.url = "github:Lxtharia/minegrub-theme";
    # plymouth-minecraft-theme.url = "github:nikp123/minecraft-plymouth-theme"; # Yeah, the naming order is inconsistent...
    # minesddm = {
    #   url = "github:Davi-S/sddm-theme-minesddm";
    #   inputs.nixpkgs.follows = "nixpkgs";
    # };

    # affinity-nix.url = "github:mrshmllow/affinity-nix";
    # It's better to install this manually (nix run/nix store) as it doesn't
    # handle the installation automatically 

    # Official plugins for Hyprland
    # https://github.com/hyprwm/hyprland-plugins
    hyprland = {
      type = "git";
      url = "https://github.com/hyprwm/Hyprland";
      submodules = true;
      # inputs.nixpkgs.follows = "nixpkgs";
    };
    # hyprland-plugins = { # I'm using hyprlandPlugins from nixpkgs instead
    #   url = "github:hyprwm/hyprland-plugins";
    #   inputs.hyprland.follows = "hyprland";
    # };
    # hyprkool = {
    #   url = "github:thrombe/hyprkool";
    #   inputs.hyprland.follows = "hyprland";
    # };
    # hypr-dynamic-cursors = {
    #   url = "github:VirtCode/hypr-dynamic-cursors";
    #   inputs.hyprland.follows = "hyprland";
    # };
    # Hyprspace = {
    #   url = "github:KZDKM/Hyprspace";
    #   inputs.hyprland.follows = "hyprland"; # Hyprspace uses latest Hyprland. We declare this to keep them in sync.
    # };

    # Stylix is a theming framework for NixOS, Home Manager, nix-darwin, and
    # Nix-on-Droid that applies color schemes, wallpapers, and fonts to a wide
    # range of applications.
    stylix.url = "github:danth/stylix/release-25.05";
    # apple-fonts.url = "github:Lyndeno/apple-fonts.nix";
    # nix-cursors = {
    #   url = "github:LilleAila/nix-cursors";
    #   inputs.nixpkgs.follows = "nixpkgs";
    # };

    # Community nixpkg for Zen Browser
    # https://scribe.rip/@notquitethereyet_/installing-zen-browser-on-nixos-%EF%B8%8F-7ae541f5533f
    zen-browser = {
      url = "github:0xc000022070/zen-browser-flake";
      inputs.nixpkgs.follows = "nixpkgs"; 
    };
    # kando.url = "github:TomaSajt/nixpkgs/kando"; # not the newest but it's 1.8 also already exist in 25.05/unstable nixpkg
  };

  outputs = { self, nixpkgs, nixpkgs-unstable, ... } @ inputs:
    let 
      system = "x86_64-linux";
      # system = "aarch64-darwin";
      host = "ege-nix";
      profile = "nvidia";
      username = "ege";
      pkgs-unstable = import nixpkgs-unstable {
        inherit system;
        config.allowUnfree = true;
      };
      in {
      nixosConfigurations = {
        amd = nixpkgs.lib.nixosSystem {
          inherit system;
          specialArgs = { inherit inputs username host profile pkgs-unstable; };
          modules = [./profiles/amd];
        };
        nvidia = nixpkgs.lib.nixosSystem {
          inherit system;
          specialArgs = { inherit inputs username host profile pkgs-unstable; };
          modules = [./profiles/nvidia];
        };
        vm = nixpkgs.lib.nixosSystem {
          inherit system;
          specialArgs = { inherit inputs username host profile pkgs-unstable; };
          modules = [./profiles/vm];
        };
      };
      # homeConfigurations."macbook" = home-manager.lib.homeManagerConfiguration {
      #   pkgs = import nixpkgs {
      #     system = "aarch64-darwin";
      #     config = {
      #       allowUnfree = true;
      #     };
      #   };
      #   modules = [ ./profiles/mac ];
      # };
      # homeConfigurations."windows" = mkHomeConfigurations {
      #   host = hosts.wsl;
      #   nixpkgs = inputs.nixpkgs-stable;
      #   home-manager = inputs.home-manager-stable;
      # };
    };
}
