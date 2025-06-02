{
pkgs,
pkgs-unstable,
...}:
{
  environment.systemPackages = with pkgs; [
    # Lutris Troubleshooting:
    # https://nixos.wiki/wiki/Lutris
    # (lutris.override {
    #   extraLibraries =  pkgs: [
    #     # List library dependencies here
    #   ];
    #   extraPkgs =  pkgs: [
    #     # List package dependencies here
    #   ];
    # })
    umu-launcher # Unified launcher for Windows games on Linux using the Steam Linux Runtime and Tools
    heroic # Native GOG, Epic, and Amazon Games Launcher for Linux, Windows and Mac

    # bottles # Easily run Windows software on Linux with Bottles!
    itch # Best way to play itch io games

    prismlauncher # Free, open source launcher for Minecraft
    mcaselector

    # rare # GUI for Legendary, an Epic Games Launcher open source alternative
    steamtinkerlaunch # Linux wrapper tool for use with the Steam client for custom launch options and 3rd party programs
    
    # Multi-platform emulator frontend for libretro cores 
    (retroarch.withCores (cores: with cores; [
    # Nintendo Emulation
      citra # 3DS
      dolphin # Gamecube/Wii
      melonds # DS/DSi https://docs.libretro.com/library/compatibility/ds/
      mgba # Game Boy/Color/Advance https://docs.libretro.com/library/mgba/
      gambatte # Game Boy/Color
      sameboy # Game Boy/Color
      mupen64plus # N64
      bsnes-mercury-balanced # SNES https://docs.libretro.com/library/compatibility/snes/
      # bsnes-mercury # SNES
      # bsnes-mercury-performance # SNES
      # snes9x # SNES
      mesen # NES https://docs.libretro.com/library/compatibility/nes/
      # fceumm # NES
      # nestopia # NES
      # beetle-vb # VirtualBoy

      # Sega Emulation
      flycast # Dreamcast
      genesis-plus-gx # MS/MD/CD
      # picodrive # MS/MD/CD/32X (Better for ARM) https://docs.libretro.com/library/picodrive/
      beetle-saturn # Saturn

      # Sony Emulation
      swanstation
      ppsspp # PSP https://docs.libretro.com/library/ppsspp/
      play # PS2 https://docs.libretro.com/library/play/
      # pcsx2 # PS2
      pcsx-rearmed # PS/PSX (Has special optimizations for ARM) https://docs.libretro.com/library/pcsx_rearmed/#background

      # Atari Emulation
      stella # 2600 https://docs.libretro.com/library/stella/
      atari800 # 5200 https://docs.libretro.com/library/atari800/

      # Arcade Emulation 
      # fbneo
      mame2003-plus

      # DOS Emulation
      dosbox-pure

      # Commodore Emulation
      # puae # Amiga

      # Other
      fbalpha2012
      scummvm # Emulation for Click2Point 
    ]))

    input-remapper
    rivalcfg # Mapping is still missing in SS Prime https://flozz.github.io/rivalcfg/devices/prime.html
  # ] ++ with pkgs-unstable; [
  ];
  programs = {
    steam = {
      enable = true;
      remotePlay.openFirewall = true;
      dedicatedServer.openFirewall = false;
      gamescopeSession.enable = false;
      extraCompatPackages = [pkgs-unstable.proton-ge-bin];
    };
    gamescope = {
      enable = true;
      capSysNice = true;
      args = [
        "--rt"
        "--expose-wayland"
      ];
    };
    gamemode = {
      enable = true;
      settings = {
        general = {
          renice = 10;
        };

        # Warning: GPU optimisations have the potential to damage hardware
        gpu = {
          apply_gpu_optimisations = "accept-responsibility";
          gpu_device = 0;
          # amd_performance_level = "high";
        };

        custom = {
          start = "${pkgs.libnotify}/bin/notify-send 'GameMode started'";
          end = "${pkgs.libnotify}/bin/notify-send 'GameMode ended'";
        };
      };
    };
  };
  # systemd.user.services.steam = {
  #   enable = true;
  #   description = "Open Steam in the background at boot";
  #   serviceConfig = {
  #     ExecStart = "${pkgs.steam} -nochatui -nofriendsui -silent %U";
  #     wantedBy = [ "graphical-session.target" ];
  #     Restart = "on-failure";
  #     RestartSec = "5s";
  #   };
  # };
  # For Gyro switch controllers
  # services.udev.extraRules = ''
  #   KERNEL=="hidraw*", SUBSYSTEM=="hidraw", MODE="0664", GROUP="plugdev"
  # '';

  # Gamescope Auto Boot from TTY (example)
  # services.xserver.enable = false; # Assuming no other Xserver needed
  # services.getty.autologinUser = "USERNAME_HERE";

  # services.greetd = {
  #   enable = true;
  #   settings = {
  #     default_session = {
  #       command = "${pkgs.gamescope}/bin/gamescope -W 1920 -H 1080 -f -e --xwayland-count 2 --hdr-enabled --hdr-itm-enabled -- steam -pipewire-dmabuf -gamepadui -steamos3 > /dev/null 2>&1";
  #       user = "USERNAME_HERE";
  #     };
  #   };
  # };
}
