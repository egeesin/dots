{
  username,
  profile,
  host,
  ...
}: {
  home.sessionPath = [
    "$HOME/.dots/bin/"
  ];
  home.sessionVariables = {
    GTK_USE_PORTAL = 1;
    EDITOR = "hx"; # helix
    BROWSER = "zen-beta";
    TERMINAL = "alacritty";
  };
  # programs.bash = {
  programs = rec {
	bash = {
	  enableCompletion = true;
	  enable = "${if pkgs.stdenv.isDarwin then "false" else "true"}";
	  shellAliases =
        # let
        #   flakeDir = "/home/${username}/.dots/nix";
        # in {
        {
        rb = "nh os switch -H ${profile}";
        upd = "nh os switch --update -H ${profile}";
        hms = "nh home switch -c ${username}@${host}";

        # rb = "darwin-rebuild switch --flake ${flakeDir}#${profile}";
        # upg = "darwin-rebuild switch --upgrade --flake ${flakeDir}#${profile}";

        # rb = "sudo nixos-rebuild switch --flake ${flakeDir}#${profile}";
        # upd = "nix flake update --flake ${flakeDir}#${profile}";
        # upg = "sudo nixos-rebuild switch --upgrade --flake ${flakeDir}#${profile}";
        # hms = "home-manager switch --flake ${flakeDir}#${profile}";

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
      shellInit = ''
        # Custom bashrc additions
        export PATH=$HOME/.local/bin:$PATH
      '';
	}
    zsh = {
      enableCompletion = true;
   	  enable = "${if pkgs.stdenv.isDarwin then "true" else "false"}";
      shellAliases = bash.shellAliases;
      shellInit = bash.shellInit;
    };
  };

  programs.starship = {
    enable = false;
    package = pkgs.starship;
  };
  programs.bat = {
    enable = true;
    config = {
      pager = "less -FR";
    };
    extraPackages = with pkgs.bat-extras; [
      batman # Read system manual pages (man) using bat as the manual page formatter.
      batpipe # A less (and bat) preprocessor for viewing more types of files in the terminal.
      batgrep
      prettybat # Pretty-print source code and highlight it with bat.
      batdiff # Diff a file against the current git index, or display the diff between two files.
      batwatch # Watch for changes in one or more files, and print them with bat.
    ];
  };
  programs.direnv = {
    enable = true;
    nix-direnv.enable = true;
  };
  imports = [
    inputs.nix-index-database.hmModules.nix-index
  ];
  programs.nix-index.enable = true;
  programs.nix-index-database.comma.enable = true;
  xdg.configFile = {
    "television/nix_channels.toml".text = ''
    [[cable_channel]]
    name = "nixpkgs"
    source_command = "nix-search-tv print"
    preview_command = "nix-search-tv preview {}"
    '';
  };
  programs.btop = {
    enable = true;
    package = pkgs.btop.override {
      rocmSupport = true;
      cudaSupport = true;
    };
    settings = {
      vim_keys = true;
      rounded_corners = true;
      proc_tree = true;
      show_gpu_info = "on";
      show_uptime = true;
      show_coretemp = true;
      cpu_sensor = "auto";
      show_disks = true;
      only_physical = true;
      io_mode = true;
      io_graph_combined = false;
    };
  };

}
