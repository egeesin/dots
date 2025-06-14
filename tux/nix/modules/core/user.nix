{
  pkgs,
  pkgs-unstable,
  inputs,
  username,
  host,
  profile,
  ...
}: let
  inherit (import ../../hosts/${host}/variables.nix) gitUsername;
in {
  imports = [inputs.home-manager.nixosModules.home-manager];
  home-manager = {
    useUserPackages = true;
    # useGlobalPkgs = true;
    useGlobalPkgs = false;
    backupFileExtension = "hm-backup";
    extraSpecialArgs = {
      inherit inputs username host profile pkgs pkgs-unstable;
    };
    users.${username} = {
      imports = [ ./../home ];
      home = {
        username = "${username}";
        homeDirectory = "/home/${username}";
        stateVersion = "24.11";
      };
      # Let home Manager install and manage itself.
      programs.home-manager.enable = true;
    };
    
  };
  users.mutableUsers = true;
  # Define a user account. Don't forget to set a password with ‘passwd’.
  users.users.${username} = {
    isNormalUser = true;
    description = "${gitUsername}";
    
    extraGroups = [
      "networkmanager"
      "wheel"
      "input"
      "adbusers"
      "docker"
      "scanner"
      "gamemode"
      "video"
      "render"
      "i2c"
    ]; # Enable ‘sudo’ for the user.
    # shell = pkgs.fish;
    ignoreShellProgramCheck = true;
    # packages = with pkgs; [
    #   tree
    # ];
  };
  # users.defaultUserShell = pkgs.fish;
  nix.settings.allowed-users = ["${username}"];
}
