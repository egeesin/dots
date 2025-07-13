{username, ...}: {
  # wiki.nixos.org/wiki/Syncthing
  services.syncthing = {
    enable = true;
    user = "${username}";
    group = "users";
    dataDir = "/home/${username}";
    configDir = "/home/${username}/.config/syncthing";
    openDefaultPorts = true; # https://localhost:8384/
    settings.gui = {
      user = "ege";
      password = "eggmegg";
    };
    settings = {
      devices = {
       "ege-galaxy" = { id = "C772BIA-MFVPNIB-F3PZ7BP-VH4WAKH-ZYMJHQC-EOXEAL2-MRL6ZKK-JLKT4QF"; };
      };
      folders = {
        "default" = {
          path = "/mnt/ege-win/Users/ege_e/Sync";
          devices = [ "ege-galaxy" ]; 
          # ignorePerms = false;
        };
        "sm-a556e_gwnq-photos" = {
          path = "~/Pictures/Android\ Camera";
          devices = [ "ege-galaxy" ]; 
          # ignorePerms = false;
        };
      };
    };
  };
}
