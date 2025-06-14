{
  pkgs,
  pkgs-unstable,
  inputs,
  # username,
   ...
}: {
  # Tip: $ realpath $(which <pkgname>) # to find path of package
  programs = {
    # fish.enable = true; # I'm fine with bash for now.
    git.enable = true;
    thunderbird.enable = true; #  a free and open-source email client
    yazi.enable = true; # a terminal file manager
    coolercontrol = { # A feature-rich cooling device control and monitoring application for Linux.
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

    hyprland = {
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
  environment.systemPackages = ( with pkgs; [
    zip unzip unrar
    # rar
    kdePackages.kde-cli-tools
    kdePackages.ark # archiver/unarchiver
    # file-roller # Archive manager for the GNOME desktop environment

    # yq # a lightweight and portable tool that works with yaml and json files.
    jq # JSON processor 
    nodePackages.prettier # an opinionated code formatter
    shfmt # Shell parser and formatter, installed it for prettybat
    # bat # A cat(1) clone with syntax highlighting and Git integration.
    eza # A modern replacement for ls.
    zoxide # a smarter cd command, inspired by z and autojump.

    television # Blazingly fast general purpose fuzzy finder TUI
    nix-search-tv # Fuzzy search for Nix packages
    ripgrep # Utility that combines the usability of The Silver Searcher with the raw speed of grep
    ripgrep-all # Ripgrep, but also search in PDFs, E-Books, Office documents, zip, tar.gz, and more

    # wezterm # GPU-accelerated cross-platform terminal emulator and multiplexer written by @wez and implemented in Rust
    alacritty # default terminal emulator

    helix # normally it's available in home-manager, but including here too so I can use it in sudo
    
    acpi # Show battery status and other ACPI information
    fastfetch # An actively maintained, feature-rich and performance oriented, neofetch like system information tool

    brightnessctl # read and control device brightness
    ddcutil # Query and change Linux monitor settings using DDC/CI and USB
    v4l-utils # v4l2loopback GUI utilities
    i2c-tools # Set of I2C tools for Linux
    helvum # GTK patchbay for pipewire

    btop # Monitor of resources with cool visuals/graphs
    atop # Another monitor of resources but more simple and precise
    # bmon # bandwidth monitor and rate estmator
    kmon # Linux Kernel Manager and Activity Monitor
    bandwhich # CLI utility for displaying current network utilization
    cpu-x # Free software that gathers information on CPU, motherboard and more
    # hardinfo2 # System information and benchmarks for Linux systems
    mangojuice # Convenient alternative to GOverlay for setting up MangoHud
    # mangohud
    lm_sensors # Tools for reading hardware sensors
    qdirstat # Graphical disk usage analyzer
    # usbutils # Tools for working with USB devices, such as lsusb
    cyme # List system USB buses and devices. A modern cross-platform lsusb that attempts to maintain compatibility with, but also add new features 
    # kdePackages.kdf # Displays available storage devices and information about their usage
    tuptime # Total uptime & downtime statistics utility

    # drm_info # Small utility to dump info about DRM devices
    # vulkan-tools
    # glmark2
    gpu-viewer # A front-end to glxinfo, vulkaninfo, clinfo and es2_info.

    # wlr-randr
    egl-wayland # EGLStream-based Wayland external platform
    wayland-utils # Wayland utilities (wayland-info)

    libnotify # Library that sends desktop notifications to a notification daemon

    ntfs3g # FUSE-based NTFS driver with full write support
    exfat # Free exFAT file system implementation

    shellcheck-minimal # Shell script analysis tool
    hyprls # LSP server for Hyprland's configuration language
    nixpkgs-lint
    nixfmt-rfc-style # Official formatter for Nix code

    zellij # Terminal workspace with batteries included (tmux but better)

    pantheon.elementary-files
    filezilla # Graphical FTP, FTPS and SFTP client
    ffmpegthumbnailer # Lightweight video thumbnailer
    epub-thumbnailer
    # nufraw-thumbnailer
    bign-handheld-thumbnailer
    kdePackages.kdegraphics-thumbnailers

    uv # Extremely fast Python package installer and resolver, written in Rust
    wget # Tool for retrieving files using HTTP, HTTPS, and FTP
    # asdf-vm # Extendable version manager with support for Ruby, Node.js, Erlang & more
    # nodejs # latest LTS https://nixos.wiki/wiki/Node.js
    fnm # https://archive.is/20250326081937/https://medium.com/thelinux/managing-node-js-versions-on-nixos-a-comprehensive-guide-0b452e194a1b
    cargo
    # $ npm set prefix ~/.npm-global
    pnpm # faster and better alternative to npm

    # wezterm
    # rofi-wayland
    bitwarden-desktop # Secure and free password manager for all of your devices

    wmctrl # CLI tool to interact with EWMH/NetWM compatible X Window Managers


    # kdePackages.xwaylandvideobridge # Utility to allow streaming Wayland windows to X applications
    # Summons a white unknown window at startup in Hyprland. Probably it's for Plasma?
    droidcam # Linux client for DroidCam app that lets you use your phone as webcam source.
    audacity # Sound editor with graphical UI
    soundconverter
    # easyeffects # pipewire compatible audio adjustment tool
    rnnoise-plugin # Real-time noise suppression plugin for voice based on Xiph's RNNoise 
    syshud # simple system status indicator written in gtkmm 4

    obsidian # Powerful knowledge base that works on top of a local folder of plain text Markdown files
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

    # spotify # unfree but adfree ->  $ bash <(curl -sSL https://raw.githubusercontent.com/SpotX-Official/SpotX-Bash/main/spotx.sh)
    quodlibet # GTK-based audio player written in Python, using the Mutagen tagging library
    # qmmp # Qt-based audio player that looks like Winamp
    # musikcube # A cross-platform terminal-based music player
    # termusic # Music Player TUI written in Rust
    fooyin # A customizable music player
    # sayonara # music client
    # kdePackages.elisa
    # kdePackages.minuet # Music education software

    qview # lightweight image viewer
    # feh
    f3d # lightweight 3d model viewer
    zathura # lightweight pdf viewer with vi-keybinds
    # kdePackages.okular
    # peruse # comic book viewer

    kdePackages.kate # Text editor
    meld # Diff client
    # kdiff3 # Compares and merges 2 or 3 files or directories
    kdePackages.kcalc # Calculator GUI
    bcal # Bits, bytes and address calculator
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
    qbittorrent-enhanced # Unofficial enhanced version of qBittorrent, a BitTorrent client
    # kdePackages.kwayland

    kdePackages.partitionmanager # Manage the disk devices, partitions and file systems on your computer
    caligula # A user-friendly, lightweight TUI for disk imaging. Far better than dd 

    wacomtablet # GUI for Wacom Linux drivers that supports different button/pen layout profiles
    # kdePackages.wacomtablet # GUI for Wacom Linux drivers that supports different button/pen layout profiles

    kdePackages.kolourpaint # Easy-to-use paint program

    # pkgs.mkShell = {
    #   nativeBuildInputs = with pkgs; [
        pkg-config
        gobject-introspection
        cargo
        cargo-tauri
        nodejs
      # ];
      # buildInputs = with pkgs; [
        at-spi2-atk
        atkmm
        cairo
        gdk-pixbuf
        glib
        gtk3
        harfbuzz
        librsvg
        libsoup_3
        pango
        webkitgtk_4_1
        openssl
    #   ];
    # };

    # yubikey-manager    
    # 
    glxinfo # available in unstable
    gimp3-with-plugins # only available in unstable atm
    simple-completion-language-server # available in 25.05/unstable
  ]) ++ (with pkgs-unstable; [
    # input-leap # Open-source KVM (Keyboard, video, mouse) software

    # kando # Cross-Platform Pie Menu

    alejandra # uncompromising nix code formatter
    # nil # lsp for nix
    nixd # lsp for nix but newer
    deadnix # Find and remove unused code in .nix source files
    statix # Lints and suggestions for the nix programming language
    typescript-language-server # lsp for TypeScript
    vscode-langservers-extracted # lsp for SCSS
    godot # Free and Open Source 2D and 3D game engine
    gdtoolkit_4 # formatter/linter for GDScript
    nmap # for connecting Godot's LSP via ncat
    bash-language-server # lsp for Bash
    yaml-language-server # lsp for YAML
    lua-language-server # lsp for Lua
    shopify-cli # lsp for Liquid templating language
    libsForQt5.kservice 
    kdePackages.dolphin #qt6 # there's something wrong when I try to open files, it always forgets what type of application it should run.

    # wineWowPackages.stable # supports both 32-bit and 64-bit Windows executables.
    wineWowPackages.waylandFull
    winetricks
  ]);

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
