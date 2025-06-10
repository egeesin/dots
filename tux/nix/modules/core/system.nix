{
pkgs,
# host,
...}: {
    nix = {
      settings = {
        experimental-features = [
          "nix-command"
          "flakes"
        ];
        download-buffer-size = 250000000;
        auto-optimise-store = true;
        builders-use-substitutes = true;
        substituters = [
          "https://hyprland.cachix.org"
          # "https://nix-gaming.cachix.org"
        ];
        trusted-substituters = [
          "https://hyprland.cachix.org"
          "https://nix-gaming.cachix.org"
        ];
        trusted-public-keys = [
          "hyprland.cachix.org-1:a7pgxzMz7+chwVL3/pzj6jIBMioiJM7ypFP8PwtkuGc="
          "nix-gaming.cachix.org-1:nbjlureqMbRAxR1gJ/f3hxemL9svXaZF/Ees8vCUUs4="
        ];
      };
      # commented out in order to avoid conflict with nh settings
      # gc = {
      #   automatic = true;
      #   dates = "weekly";
      #   options = "--delete-older-than 30d";
      # };
    };
    programs.nix-ld.enable = true;
    # programs.nix-ld.libraries = with pkgs; [
    # ]

    # Set your time zone.
    time.hardwareClockInLocalTime = true;
    # $ timedatectl
    time.timeZone = "Europe/Istanbul";
    # Select internationalisation properties.
    i18n = {
      defaultLocale = "en_US.UTF-8";
      extraLocaleSettings = {
        LC_ADDRESS = "en_US.UTF-8";
        LC_IDENTIFICATION = "en_US.UTF-8";
        LC_MEASUREMENT = "tr_TR.UTF-8";
        LC_MONETARY = "en_US.UTF-8";
        LC_NAME = "en_US.UTF-8";
        LC_NUMERIC = "tr_TR.UTF-8";
        LC_PAPER = "tr_TR.UTF-8";
        LC_TELEPHONE = "tr_TR.UTF-8";
        LC_TIME = "tr_TR.UTF-8";
      };
    };
    console = {
    #   # See font options: https://adeverteuil.github.io/linux-console-fonts-screenshots/
      font = "LatArCyrHeb-19";
    #   colors = [
    #     "002b36"
    #     "dc322f"
    #     "859900"
    #     "b58900"
    #     "268bd2"
    #     "d33682"
    #     "2aa198"
    #     "eee8d5"
    #     "002b36"
    #     "cb4b16"
    #     "586e75"
    #     "657b83"
    #     "839496"
    #     "6c71c4"
    #     "93a1a1"
    #     "fdf6e3"
    #   ];
    #   #   keyMap = "us";
      useXkbConfig = true; # use xkb.options in tty.
    }; 
    environment.variables = {
      FLAKE="/home/ege/.dots/tux/nix/"; # TODO: Include flake dir to variable
      # POLKIT_BIN = "${pkgs.polkit_gnome}/libexec/polkit-gnome-authentication-agent-1";
      POLKIT_BIN = "${pkgs.plasma5Packages.polkit-kde-agent}/libexec/polkit-kde-authentication-agent-1";
    };

    # This value determines the NixOS release from which the default
    # settings for stateful data, like file locations and database versions
    # on your system were taken. It‘s perfectly fine and recommended to leave
    # this value at the release version of the first install of this system.
    # Before changing this value read the documentation for this option
    # (e.g. man configuration.nix or on https://nixos.org/nixos/options.html).
    system.stateVersion = "24.11"; # Did you read the comment?
  }
