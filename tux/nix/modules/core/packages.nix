{
  pkgs,
  pkgs-unstable,
  # inputs,
  # username,
   ...
}: {

  # Tip: $ realpath $(which <pkgname>) # to find path of package
  programs = {
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
    # hyprland = {
      # enable = false;
      # package = inputs.hyprland.packages.${pkgs.stdenv.hostPlatform.system}.hyprland;
      # portalPackage = inputs.hyprland.packages.${pkgs.stdenv.hostPlatform.system}.xdg-desktop-portal-hyprland;
      # withUWSM = false;
      # xwayland.enable = true;
    # };
    
    # fish.enable = true;
    git.enable = true;
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
    thunderbird.enable = true; #  a free and open-source email client
    lazygit.enable = true; # simple terminal UI for git commands
    yazi.enable = true; # a terminal file manager
    coolercontrol = { # A feature-rich cooling device control and monitoring application for Linux.
      enable = true;
      nvidiaSupport = true;
      # https://docs.coolercontrol.org/tutorials/profile.html
    };
  };

  nixpkgs.config.allowUnfree = true; 

  # https://search.nixos.org/packages
  environment.systemPackages = ( with pkgs; [
    zip
    unzip
    # rar
    unrar
    kdePackages.kde-cli-tools
    kdePackages.ark # archiver/unarchiver
    # file-roller # Archive manager for the GNOME desktop environment

    yq # a lightweight and portable tool that works with yaml and json files.
    nodePackages.prettier # an opinionated code formatter
    shfmt # Shell parser and formatter, installed it for prettybat
    # bat # A cat(1) clone with syntax highlighting and Git integration.
    delta # Git diff with better highlight, installed it as optional dep for batdiff
    difftastic # a structural diff that understands syntax
    eza # A modern replacement for ls.
    zoxide # a smarter cd command, inspired by z and autojump.

    ripgrep # Utility that combines the usability of The Silver Searcher with the raw speed of grep
    ripgrep-all # Ripgrep, but also search in PDFs, E-Books, Office documents, zip, tar.gz, and more

    wezterm # GPU-accelerated cross-platform terminal emulator and multiplexer written by @wez and implemented in Rust
    alacritty # default terminal emulator
    
    acpi # Show battery status and other ACPI information
    fastfetch # An actively maintained, feature-rich and performance oriented, neofetch like system information tool

    brightnessctl # read and control device brightness
    ddcutil # Query and change Linux monitor settings using DDC/CI and USB
    i2c-tools
    helvum # GTK patchbay for pipewire

    btop # Monitor of resources
    cpu-x # Free software that gathers information on CPU, motherboard and more
    # hardinfo2 # System information and benchmarks for Linux systems
    mangojuice # Convenient alternative to GOverlay for setting up MangoHud
    # mangohud
    lm_sensors # Tools for reading hardware sensors
    qdirstat # Graphical disk usage analyzer
    # usbutils # Tools for working with USB devices, such as lsusb
    cyme # List system USB buses and devices. A modern cross-platform lsusb that attempts to maintain compatibility with, but also add new features 

    # drm_info # Small utility to dump info about DRM devices
    # vulkan-tools
    # glmark2
    gpu-viewer # A front-end to glxinfo, vulkaninfo, clinfo and es2_info.
    
    #jujutsu # insecure

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

    libsForQt5.kservice 
    # kdePackages.kservice 
    kdePackages.dolphin #qt6 # there's something wrong when I try to open files, it always forgets what type of application it should run.
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
    nodejs # latest LTS https://nixos.wiki/wiki/Node.js
    # $ npm set prefix ~/.npm-global
    pnpm # faster and better alternative to npm

    # wezterm
    # rofi-wayland
    bitwarden-desktop # Secure and free password manager for all of your devices

    ulauncher # Fast application launcher for Linux, written in Python, using GTK
    nwg-launchers # GTK-based launchers: application grid, button bar, dmenu for sway and other window managers
    # nwg-menu # menu start plugin for nwg-panel
    # https://github.com/NixOS/nixpkgs/issues/297267
    wmctrl # CLI tool to interact with EWMH/NetWM compatible X Window Managers

    # kdePackages.xwaylandvideobridge # Utility to allow streaming Wayland windows to X applications
    # Summons a white unknown window at startup in Hyprland. Probably it's for Plasma?
    droidcam # Linux client for DroidCam app that lets you use your phone as webcam source.
    audacity # Sound editor with graphical UI
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
    mpv # lightweight media player
    mpvScripts.uosc # Feature-rich minimalist proximity-based UI
    mpvScripts.thumbfast # High-performance on-the-fly thumbnailer for mpv
    mpvScripts.visualizer # various audio visualization
    mpvScripts.youtube-chat # overlay youtube chat on top of a video using yt-dlp
    mpvScripts.youtube-upnext # Userscript that allows you to play 'up next'/recommended youtube videos
    mpvScripts.twitch-chat # Show Twitch chat messages as subtitles when watching Twitch VOD with mpv.
    mpvScripts.videoclip # Easily create videoclips with mpv
    mpvScripts.mpv-notify-send # send notifications with notify-send
    mpvScripts.mpv-playlistmanager # Create and manage playlists
    mpvScripts.mpv-discord # Cross-platform Discord Rich Presence integration for mpv with no external dependencies
    mpvScripts.mpris # Add support for media keybinds
    mpvScripts.vr-reversal # Script for mpv to play VR video with optional saving of head tracking data
    mpvScripts.sponsorblock-minimal # SponsorBlock with minimal deps
    mpvScripts.skipsilence # Increase playback speed during silence
    mpvScripts.quality-menu # Switch video quality from YT on-the-go
    mpvScripts.mpv-subtitle-lines # Skip to subtitle lines
    mpvScripts.memo # REcent files menu
    mpvScripts.evafast # Seeking and hybrid fastforwarding like VHS
    mpvScripts.quack # Reduce audio volume after seeking
    mpvScripts.autosub # Fully automatic subtitle downloading
    mpvScripts.manga-reader
    mpvScripts.mpv-image-viewer.minimap # Adds a minimap that displays the position of the image relative to the view
    mpvScripts.mpv-image-viewer.ruler # Adds a ruler command that lets you measure positions, distances and angles in the image. Can be configured through ruler.conf
    mpvScripts.mpv-image-viewer.status-line # Adds a status line that can show different properties in the corner of the window
    mpvScripts.mpv-image-viewer.freeze-window # By default, mpv automatically resizes the window when the current file changes to fit its size. This script freezes the window so that this does not happen
    mpvScripts.mpv-image-viewer.image-positioning # Adds several high-level commands to zoom and pan
    mpvScripts.occivink.crop # Crop the current video in a visual manner

    # spotify # unfree but adfree ->  $ bash <(curl -sSL https://raw.githubusercontent.com/SpotX-Official/SpotX-Bash/main/spotx.sh)
    quodlibet # GTK-based audio player written in Python, using the Mutagen tagging library
    qmmp # Qt-based audio player that looks like Winamp
    fooyin # A customizable music player
    # sayonara # music client
    # kdePackages.elisa
    handbrake # Tool for converting video files and ripping DVDs
    # wf-recorder # a utility program for screen recording of wlroots-based compositors | Usage: https://github.com/ammen99/wf-recorder#usage
    peek # Simple animated GIF screen recorder with an easy to use interface
    kooha # Elegantly record your screen

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
    libsForQt5.qtstyleplugins # Additional style plugins for Qt5, including BB10, GTK, Cleanlooks, Motif, Plastique
    # kdePackages.qt6gtk2 # gtk+2.0 integration plugins for qt6
    kdePackages.koi # Scheduling LIGHT/DARK Theme Converter for the KDE Plasma Desktop

    # kdePackages.kdf # Displays available storage devices and information about their usage
    # kdePackages.kmix # nixos says it's broken
    kdePackages.kmouth # Type-and-say front end for speech synthesizers
    kdePackages.krdc # Remote Desktop Client
    kdePackages.krdp # Library and examples for creating an RDP server
    # kdePackages.kruler
    # kdePackages.kteatime
    kdePackages.ktimer # 
    # kdePackages.ktorrent
    qbittorrent-enhanced # Unofficial enhanced version of qBittorrent, a BitTorrent client
    # kdePackages.kwave # nixos says it's broken
    # kdePackages.kwayland
    # kdePackages.minuet

    kdePackages.partitionmanager # Manage the disk devices, partitions and file systems on your computer
    kdePackages.wacomtablet # GUI for Wacom Linux drivers that supports different button/pen layout profiles

    kdePackages.kolourpaint # Easy-to-use paint program


    # yubikey-manager    
    # 
    glxinfo # available in unstable
    gimp3-with-plugins # only available in unstable atm
    simple-completion-language-server # available in 25.05/unstable
  ]) ++ (with pkgs-unstable; [
    kando # Cross-Platform Pie Menu
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
  ]);

  # Some programs need SUID wrappers, can be configured further or are
  # started in user sessions.
  # programs.mtr.enable = true;
  programs.gnupg.agent = {
    enable = true;
    enableSSHSupport = true;
  };
  programs.dconf.enable = true;
}
