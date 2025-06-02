{
  username,
  profile,
  host,
  ...
}: {
  programs.bash = {
    enableCompletion = true; 
    enable = true;
    shellAliases =
      # let
      #   flakeDir = "/home/${username}/.dots/tux/nix";
      # in {
      {
      # rb = "sudo nixos-rebuild switch --flake ${flakeDir}#${profile}";
      rb = "nh os switch --hostname ${profile}";
      # upd = "nix flake update --flake ${flakeDir}#${profile}";
      # upg = "sudo nixos-rebuild switch --upgrade --flake ${flakeDir}#${profile}";
      upg = "nh os switch --hostname ${profile} --update";

      # hms = "home-manager switch --flake ${flakeDir}#${profile}";
      hms = "nh home switch -c ${username}@${host}";

      # conf = "$EDITOR ${flakeDir}/modules/core/default.nix";
      # hmconf = "$EDITOR ${flakeDir}/modules/home/default.nix";
      # pkgs = "$EDITOR ${flakeDir}/modules/core/packages.nix";

      lsgen = "sudo nix-env -p /nix/var/nix/profiles/system --list-generations";
      rmgen = "sudo nix-collect-garbage -d";
      # rmgen = "nix-collect-garbage --delete-old && sudo nix-collect-garbage -d && sudo /run/current-system/bin/switch-to-configuration boot";

      # Found it from here: https://discourse.nixos.org/t/how-to-generate-nix-source-from-json/28633/8
      # https://nix.dev/manual/nix/2.28/language/builtins.html#builtins-fromJSON
      # Requires nixfmt-rfc-style
      # $1 should be absolute path
      json2nix = "nix-instantiate --eval -E 'builtins.fromJSON (builtins.readFile $1)' | nixfmt > $2";
      toml2nix = "nix-instantiate --eval -E 'builtins.fromTOML (builtins.readFile $1)' | nixfmt > $2";

      cat = "bat";
      man = "batman";
      ls = "eza --icons --group-directories-first -1";
      ll = "eza --icons -lh --group-directories-first -1 --no-user --long";
      la = "eza --icons -lah --group-directories-first -1";
      tree = "eza --icons --tree --group-directories-first";

      # ll = "ls -l";
      # se = "sudoedit";
      # ff = "fastfetch";
    };
    bashrcExtra = ''
      # Custom bashrc additions
      export PATH=$HOME/.local/bin:$PATH
    '';
  };
}
