{
  pkgs,
  pkgs-unstable,
  inputs,
  lib,
  # username,
   ...
}: {
  # Tip: $ realpath $(which <pkgname>) # to find path of package
  programs = {
    # fish.enable = true; # I'm fine with bash for now.
    git.enable = true;
    atuin.enable = true;
    atuin.flags = [ "--disable-up-arrow" ];
    # direnv.enable = true;
    thunderbird.enable = true; #  a free and open-source email client
    yazi.enable = true; # a terminal file manager
    coolercontrol = lib.optional stdenv.isLinux { # A feature-rich cooling device control and monitoring application for Linux.
      enable = true;
      nvidiaSupport = true;
      # https://docs.coolercontrol.org/tutorials/profile.html
    };

    # Some programs need SUID wrappers, can be configured further or are
    # started in user sessions.
    # programs.mtr.enable = true;
    gnupg.agent = {
      enable = true;
      enableSSHSupport = true;
    };
    dconf.enable = true;

    # uwsm = {
    #   enable = false;
    #   waylandCompositors = {
    #     hyprland = {
    #       prettyName = "Hyprland";
    #       comment = "Hyprland compositor managed by UWSM";
    #       # binPath = "/run/current-system/sw/bin/Hyprland";
    #       binPath = "/etc/profiles/per-user/${username}/bin/Hyprland";
    #     };
    #   };
    # };

    hyprland = lib.optional stdenv.isLinux {
      enable = true;
      package = inputs.hyprland.packages.${pkgs.system}.hyprland;
      portalPackage = inputs.hyprland.packages.${pkgs.system}.xdg-desktop-portal-hyprland;
      # withUWSM = false;
      xwayland.enable = true;
    };

    # Using zen instead.
    # google-chrome = {
    #   enable = true;
    #   package = pkgs.google-chrome;

    #   # https://wiki.archlinux.org/title/Chromium#Native_Wayland_support
    #   commandLineArgs = [
    #     "--ozone-platform-hint=auto"
    #     "--ozone-platform=wayland"
    #     # make it use GTK_IM_MODULE if it runs with Gtk4, so fcitx5 can work with it.
    #     # (only supported by chromium/chrome at this time, not electron)
    #     "--gtk-version=4"
    #     # make it use text-input-v1, which works for kwin 5.27 and weston
    #     "--enable-wayland-ime"

    #     # enable hardware acceleration - vulkan api
    #     # "--enable-features=Vulkan"
    #   ];
    # };
    # firefox = {
    #   enable = false;
    #   preferencesStatus = "user";
    #   policies = {
    #     DisableTelemetry = true;
    #     DisableFirefoxStudies = true;
    #     EnableTrackingProtection = {
    #       Value= true;
    #       Locked = true;
    #       Cryptomining = true;
    #       Fingerprinting = true;
    #     };
    #     DisablePocket = true;
    #     DontCheckDefaultBrowser = true;
    #     DisplayBookmarksToolbar = "newtab";
    #     SearchBar = "unified";
    #     SearchEngines = {
    #       PreventInstalls = false;
    #     };
    #     Preferences = {
    #       extensions.pocket.enabled = "lock-false";
    #       browser.formfill.enable = "lock-false";
    #       browser.newtabpage.activity-stream.feeds.section.topstories = "lock-false";
    #       browser.newtabpage.activity-stream.feeds.snippets = "lock-false";
    #       browser.newtabpage.activity-stream.showSponsored = "lock-false";
    #       browser.newtabpage.activity-stream.system.showSponsored = "lock-false";
    #       browser.newtabpage.activity-stream.showSponsoredTopSites = "lock-false";
    #     };
    #   };
    # };
    # vscode = {
    #   enable = true;
    #   package =
    #     pkgs.vscode.override
    #     {
    #       isInsiders = false;
    #       # https://wiki.archlinux.org/title/Wayland#Electron
    #       commandLineArgs = [
    #         "--ozone-platform-hint=auto"
    #         "--ozone-platform=wayland"
    #         # make it use GTK_IM_MODULE if it runs with Gtk4, so fcitx5 can work with it.
    #         # (only supported by chromium/chrome at this time, not electron)
    #         "--gtk-version=4"
    #         # make it use text-input-v1, which works for kwin 5.27 and weston
    #         "--enable-wayland-ime"

    #         # TODO: fix https://github.com/microsoft/vscode/issues/187436
    #         # still not works...
    #         "--password-store=gnome" # use gnome-keyring as password store
    #       ];
    #     };
    # };
  };

  # https://search.nixos.org/packages
  environment.systemPackages =
  ( with pkgs; [
    zip unzip unrar
    # rar

    # yq # a lightweight and portable tool that works with yaml and json files.
    jq # JSON processor
    jqp # TUI playground to experiment with jq
    shfmt # Shell parser and formatter, installed it for prettybat
    # bat # A cat(1) clone with syntax highlighting and Git integration.
    eza # A modern replacement for ls.
    zoxide # a smarter cd command, inspired by z and autojump.
    sshs # terminal user interface for ssh
    nushell

    television # Blazingly fast general purpose fuzzy finder TUI
    nix-search-tv # Fuzzy search for Nix packages
    ripgrep # Utility that combines the usability of The Silver Searcher with the raw speed of grep
    ripgrep-all # Ripgrep, but also search in PDFs, E-Books, Office documents, zip, tar.gz, and more

    # wezterm # GPU-accelerated cross-platform terminal emulator and multiplexer written by @wez and implemented in Rust

    helix # normally it's available in home-manager, but including here too so I can use it in sudo
    nodePackages.prettier # an opinionated code formatter
    shellcheck-minimal # Shell script analysis tool
    hyprls # LSP server for Hyprland's configuration language
    nixpkgs-lint
    nixfmt-rfc-style # Official formatter for Nix code

    fastfetch # An actively maintained, feature-rich and performance oriented, neofetch like system information tool
    # fastfetchMinimal

    btop # Monitor of resources with cool visuals/graphs
    # bmon # bandwidth monitor and rate estmator
    bandwhich # CLI utility for displaying current network utilization
    cyme # List system USB buses and devices. A modern cross-platform lsusb that attempts to maintain compatibility with, but also add new features
    tuptime # Total uptime & downtime statistics utility

    ntfs3g # FUSE-based NTFS driver with full write support

    zellij # Terminal workspace with batteries included (tmux but better)

    uv # Extremely fast Python package installer and resolver, written in Rust
    wget # Tool for retrieving files using HTTP, HTTPS, and FTP
    # asdf-vm # Extendable version manager with support for Ruby, Node.js, Erlang & more
    # nodejs # latest LTS https://nixos.wiki/wiki/Node.js
    fnm # https://archive.is/20250326081937/https://medium.com/thelinux/managing-node-js-versions-on-nixos-a-comprehensive-guide-0b452e194a1b
    cargo
    # $ npm set prefix ~/.npm-global
    pnpm # faster and better alternative to npm

    # wezterm

    wmctrl # CLI tool to interact with EWMH/NetWM compatible X Window Managers

    audacity # Sound editor with graphical UI

    syncthingtray-minimal # Tray application and Dolphin/Plasma integration for Syncthing
    inkscape-with-extensions # Vector graphics editor

    # fontconfig
    font-manager # Simple font management for GTK desktop environments

    graphicsmagick # Swiss army knife of image processing
    rawtherapee # RAW photo editor
    # nufraw
    ffmpeg # Complete, cross-platform solution to record, convert and stream audio and video
    # haruna # Open source video player built with Qt/QML and libmpv
    # vlc # Cross-platform media player and streaming server
    handbrake # Tool for converting video files and ripping DVDs

    quodlibet # GTK-based audio player written in Python, using the Mutagen tagging library
    # termusic # Music Player TUI written in Rust
    # sayonara # music client

    # feh
    f3d # lightweight 3d model viewer

    qbittorrent-enhanced # Unofficial enhanced version of qBittorrent, a BitTorrent client

    caligula # A user-friendly, lightweight TUI for disk imaging. Far better than dd

    simple-completion-language-server # available in 25.05/unstable
  ]) ++ (with pkgs-unstable; [
    alejandra # uncompromising nix code formatter
    # nil # lsp for nix
    nixd # lsp for nix but newer
    deadnix # Find and remove unused code in .nix source files
    statix # Lints and suggestions for the nix programming language
    typescript-language-server # lsp for TypeScript
    vscode-langservers-extracted # lsp for SCSS
    gdtoolkit_4 # formatter/linter for GDScript
    nmap # for connecting Godot's LSP via ncat
    bash-language-server # lsp for Bash
    yaml-language-server # lsp for YAML
    lua-language-server # lsp for Lua

  ]) ++ (lib.optionals stdenv.isLinux with pkgs; [

    alacritty # default terminal emulator
    kdePackages.kde-cli-tools
    kdePackages.ark # archiver/unarchiver
    # file-roller # Archive manager for the GNOME desktop environment

    acpi # Show battery status and other ACPI information

    brightnessctl # read and control device brightness
    ddcutil # Query and change Linux monitor settings using DDC/CI and USB
    v4l-utils # v4l2loopback GUI utilities
    i2c-tools # Set of I2C tools for Linux
    helvum # GTK patchbay for pipewire

    atop # Another monitor of resources but more simple and precise
    kmon # Linux Kernel Manager and Activity Monitor

    cpu-x # Free software that gathers information on CPU, motherboard and more
    # hardinfo2 # System information and benchmarks for Linux systems
    mangojuice # Convenient alternative to GOverlay for setting up MangoHud
    # mangohud
    lm_sensors # Tools for reading hardware sensors
    qdirstat # Graphical disk usage analyzer
    # usbutils # Tools for working with USB devices, such as lsusb
    # kdePackages.kdf # Displays available storage devices and information about their usage

    # drm_info # Small utility to dump info about DRM devices
    # vulkan-tools
    # glmark2
    gpu-viewer # A front-end to glxinfo, vulkaninfo, clinfo and es2_info.

    # wlr-randr
    egl-wayland # EGLStream-based Wayland external platform
    wayland-utils # Wayland utilities (wayland-info)

    libnotify # Library that sends desktop notifications to a notification daemon

    exfat # Free exFAT file system implementation

    pantheon.elementary-files
    filezilla # Graphical FTP, FTPS and SFTP client
    ffmpegthumbnailer # Lightweight video thumbnailer
    epub-thumbnailer
    # nufraw-thumbnailer
    bign-handheld-thumbnailer
    kdePackages.kdegraphics-thumbnailers

    # rofi-wayland
    bitwarden-desktop # Secure and free password manager for all of your devices

    obsidian # Powerful knowledge base that works on top of a local folder of plain text Markdown files

    # kdePackages.xwaylandvideobridge # Utility to allow streaming Wayland windows to X applications
    # Summons a white unknown window at startup in Hyprland. Probably it's for Plasma?
    droidcam # Linux client for DroidCam app that lets you use your phone as webcam source.
    soundconverter
    # easyeffects # pipewire compatible audio adjustment tool
    rnnoise-plugin # Real-time noise suppression plugin for voice based on Xiph's RNNoise
    syshud # simple system status indicator written in gtkmm 4

    # musikcube # A cross-platform terminal-based music player
    # spotify # unfree but adfree ->  $ bash <(curl -sSL https://raw.githubusercontent.com/SpotX-Official/SpotX-Bash/main/spotx.sh)
    # qmmp # Qt-based audio player that looks like Winamp
    fooyin # A customizable music player
    # kdePackages.elisa
    # kdePackages.minuet # Music education software

    qview # lightweight image viewer
    zathura # lightweight pdf viewer with vi-keybinds
    # kdePackages.okular
    # peruse # comic book viewer

    kdePackages.kate # Text editor
    zed-editor # High-performance, multiplayer code eidtor from the creators of Atom and Tree-sitter
    meld # Diff client
    # kdiff3 # Compares and merges 2 or 3 files or directories
    kdePackages.kcalc # Calculator GUI
    # hyprcursor # https://wiki.hyprland.org/FAQ/#how-do-i-change-me-mouse-cursor
    # kdePackages.kcolorpicker
    # hyprland-qt-support # couldn't find
    # hyprsunset # https://wiki.hyprland.org/Hypr-Ecosystem/hyprsunset/

    themix-gui # Graphical application for designing themes and exporting them using plugins
    nwg-look # gtk theming tool like lxappearance but newer
    ocs-url # Open Collaboration System for use with DE store websites
    # kdePackages.qt6ct # qt6 config tool
    # libsForQt5.qt5ct # qt5 config tool
    # inspector # Gtk4 Libadwaita wrapper for various system info cli commands
    # libsForQt5.qtstyleplugins # Additional style plugins for Qt5, including BB10, GTK, Cleanlooks, Motif, Plastique
    # kdePackages.qt6gtk2 # gtk+2.0 integration plugins for qt6
    kdePackages.koi # Scheduling LIGHT/DARK Theme Converter for the KDE Plasma Desktop

    # kdePackages.kmix # Volume control program but nixos says it's broken
    kdePackages.kmouth # Type-and-say front end for speech synthesizers
    kdePackages.krdc # Remote Desktop Client
    kdePackages.krdp # Library and examples for creating an RDP server
    # kdePackages.kruler
    mpris-timer # timer app
    # kdePackages.ktorrent
    # kdePackages.kwayland

    kdePackages.partitionmanager # Manage the disk devices, partitions and file systems on your computer

    libwacom
    kdePackages.wacomtablet # GUI for Wacom Linux drivers that supports different button/pen layout profiles

    kdePackages.kolourpaint # Easy-to-use paint program

    # yubikey-manager

    # glxinfo # available in unstable
    gimp3-with-plugins # only available in unstable atm

  ]) ++ (lib.optionals stdenv.isLinux with pkgs-unstable; [

    deskflow # Share a single keyboard and mouse between multiple computers.

    # kando # Cross-Platform Pie Menu
    godot # Free and Open Source 2D and 3D game engine

    libsForQt5.kservice
    kdePackages.dolphin #qt6 # there's something wrong when I try to open files, it always forgets what type of application it should run.

    # wineWowPackages.stable # supports both 32-bit and 64-bit Windows executables.
    wineWowPackages.waylandFull
    winetricks
  ]);

  homebrew = lib.optional stdenv.isDarwin {
  # Go to https://formulae.brew.sh to search Brews and Casks
  	enable = true;
    onActivation = {
      autoUpdate = true;
      upgrade = true;
      cleanup = "uninstall";
    };
    taps = [
      "homebrew/bundles"
      "homebrew/services"
      "deskflow/homebrew-tap"
    ];
    brews = [
    # "graphicsmagick"
    ];
    casks = [
      # "google-chrome"
      "localsend" # An open-source cross-platform alternative to AirDrop
      "deskflow" # Share one mouse and keyboard between multiple computers on Windows, macOS and Linux
      "bitwarden"
      "appcleaner"
      "keybase"
      "the-unarchiver"
      "wezterm"
      # "ghostty"
      # "alacritty"
      "wacom-tablet"
      "stats"
      "fanny"
      "macs-fan-control"
      "monitorcontrol"
      # "dropbox"
      "scroll-reverser"
      "linearmouse"
      "orion"
      # "zen"
      "ungoogled-chromium"
      # "netnewswire"
      "obsidian"
      "iina"
      # "spotify"
      # tap "khanhas/tap"
      # brew "spicetify-cli"
      # "bluestacks"
      "discord"
      "element" # Matrix collaboration client
      "handbrake"
      "losslesscut"

      # "fontgoggles" # Font viewer for various font formats
      "unicodechecker"
      "exifrenamer"
      # "virtualbox"
      "karabiner-elements"
      "penc"
      # "soundflower"
      "inkscape"
      "imageoptim"
      "prismlauncher"
      "steam"
      "qlcolorcode"
      "qlstephen"
      "qlmarkdown"
      "quicklook-json"
      "qlprettypatch"
      "quicklook-csv"
      # "betterzipql"
      "qlimagesize"
      "webpquicklook"
      "quicklookase"
      "quicklook-pat"
      "qlvideo"
      "suspicious-package"
      "adobe-creative-cloud-cleaner-tool"

      "f3d" # Fast and minimalist 3D viewer

      "sensiblesidebuttons"

      "beeper"
      "signal"
      "c0re100-qbittorrent"
     ];
     masApps = {

     };
  };

  # Make sure xdg.portal.enable is true
  services.flatpak.enable = true;
  systemd.services.flatpak-repo = {
    wantedBy = ["multi-user.target"];
    path = [pkgs.flatpak];
    script = ''
      flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo
    '';
  };

  # Install AppImage package manager too
  programs.appimage = {
    enable = true;
    binfmt = true; # AppImage files can be invoked directly as if they were normal programs
  };

  environment.systemPackages = with pkgs; [
    # kdePackages.discover # Optional: Install if you use Flatpak or fwupd firmware update sevice
    gearlever # manage AppImages with ease
  ];

  imports = [
    # inputs.minesddm.nixosModules.default
    inputs.minegrub-theme.nixosModules.default
    inputs.stylix.nixosModules.stylix
  ];

  nixpkgs = {
    config.allowUnfree = true;
    overlays = [
      inputs.dolphin-overlay.overlays.default # This Nix overlay fixes Dolphin's "Open with" menu when running outside of KDE (e.g., under Hyprland or other Wayland compositors).
      inputs.grim-hyprland.overlays.default # A fork of grim that takes advantage of Hyprland's custom protocols to grab specific windows.
      # inputs.fancontrol-gui.overlays.default
    ];
  };
}
