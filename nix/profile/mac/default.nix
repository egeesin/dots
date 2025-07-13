{ pkgs, lib, inputs }: {
  imports = [
    ../../host/${host}
    ../../module/driver
    # ../../module/core
    ../../module/core/package.nix
    ../../module/core/user.nix
  ];
  # Enable/Disable GPU Drivers
  # drivers.amdgpu.enable = false;
  # drivers.nvidia.enable = false;
  # vm.guest-services.enable = false;

  environment.systemPackages = with pkgs; [
  	git
    lazygit
 	helix
   	direnv
    sshs
    nushell
    carapace
    atuin # https://docs.atuin.sh/#quickstart

  ];
  nix.gc = {
  	automatic = true;
  };

  services.nix-daemon.enable = true;
  # nix.useDaemon = true;

  # Necessary for using flakes on this system.
  nix.settings.experimental-features = "nix-command flakes";

  networking.hostName = "${host}";
  programs.zsh.enable = true; # default shell since catalina

  # Enable alternative shell support in nix-darwin.
  # programs.fish.enable = true;

  # Set Git commit hash for darwin-version.
  system.configurationRevision = self.rev or self.dirtyRev or null;

  # The platform the configuration will be used on.
  nixpkgs.hostPlatform = "x86_64-darwin"; # Intel
  # nixpkgs.hostPlatform = "aarch64-darwin"; # Apple Silicon

  # security.pam.enableSudoTouchIdAuth = true;

  # system.activationScripts.extraActivation.text = ''
  #     # there's no going back from Apple Silicon
  #     softwareupdate --install-rosetta --agree-to-license
  # '';

  # nix-homebrew = {
  #   enable = true;
  #   taps = {
  #     "homebrew/homebrew-core" = homebrew-core;
  #     "homebrew/homebrew-cask" = homebrew-cask;
  #     "homebrew/homebrew-bundle" = homebrew-bundle;
  #   };
  #   mutableTaps = false;
  #   autoMigrate = true;
  # };

  system.primaryUser = "${host}";
  system.defaults = {
  	# TODO: Migrate .dots/mac/defaults.sh here
    dock = {
      autohide = true;
      orientation = "left";
      # show-process-indicator = false;
    };
    # dock.mru-spaces = false;
    finder = {
	    AppleShowAllExtensions = true;
		ShowPathbar = true;
		FXPreferredViewStyle = "clmv";
    };
    NSGlobalDomain = {
      ApplePressAndHoldEnabled = false;
      InitialKeyRepeat = 10;
      KeyRepeat = 1;
      NSTableViewDefaultSizeMode = 1;
      AppleShowScrollBars = "WhenScrolling";
      NSUseAnimatedFocusRing = false;
      NSWindowResizeTime = 0.001;
      NSNavPanelExpandedStateForSaveMode = true;
      NSNavPanelExpandedStateForSaveMode2 = true;
      PMPrintingExpandedStateForPrint = true;
      PMPrintingExpandedStateForPrint2 = true;
      NSDocumentSaveNewDocumentsToCloud = false;
      NSTextShowsControlCharacters = true;
      NSDisableAutomaticTermination = true;
    };
    LaunchServices = {
      LSQuarantine = false;
    };
    # WindowManager = { GloballyEnabled = true; }
    keyboard = {
      enableKeyMapping = true;
      # remapCapsLockToEscape = true;
    };
    # loginwindow.LoginwindowText = "";
    screencapture.location = "~/Pictures/Screenshots";
    screensaver.askForPasswordDelay = 10;
    "com.apple.print.PrintingPrefs" = {
      "Quit When Finished" = true;
    };
  };

}
