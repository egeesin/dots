{
pkgs,
pkgs-unstable,
...}: {
  environment.systemPackages = ( with pkgs; [
    shopify-cli

    eartag
    tageditor
    picard # music tag editor
    cava # Cross-platform Audio Visualizer

    nvtopPackages.full
    nvitop # Interactive NVIDIA-GPU process viewer, the one-stop solution for GPU process management
    sysz # fzf terminal UI for systemctl
    isd # TUI to interactively work with systemd units
    lazyjournal # TUI for journalctl, file system logs, as well as Docker and Podman containers
    tzupdate # Set the system timezone based on IP geolocation
    lemmeknow # Tool to indentify anything

    kdePackages.kdenlive

    # junction # Choose the application to open files and links

    newsflash # Modern feed reader designed for the GNOME desktop
    tuba # Browse the Fediverse
    video-trimmer # Trim videos quickly
    gnome-characters # Simple utility application to find and insert unusual characters
    # kdePackages.kcharselect # Tool to select and copy special characters from all installed fonts
    gnome-logs # log viewer for the systemd journal
    # kdePackages.ksystemlog
    gnome-maps # map application
    blanket # listen to different sounds
    curtail # Simple & useful image compressor
    identity # Program for comparing multiple versions of an image or video
    pomodoro-gtk # Simple and intuitive timer application (also named Planytimer)
    letterpress # converts your images into a picture made up of ASCII characters
    # komikku # Manga/CB reader for GNOME
    
    lmms # DAW
    soundfont-generaluser
    soundfont-fluid

    ungoogled-chromium

    # obs-studio # screen recorder/streamer
    # obs-studio-plugins.wlrobs
    # # obs-studio-plugins.obs-nvfbc # unstable says it's broken
    # obs-studio-plugins.input-overlay  
    # obs-studio-plugins.droidcam-obs
    # obs-studio-plugins.obs-freeze-filter 
    # obs-studio-plugins.obs-livesplit-one 
    # obs-studio-plugins.obs-replay-source
    # obs-studio-plugins.obs-move-transition
    # obs-studio-plugins.obs-transition-table
    # obs-studio-plugins.obs-pipewire-audio-capture
    # obs-studio-plugins.advanced-scene-switcher
    #
    (wrapOBS {
      plugins = with pkgs.obs-studio-plugins; [
        input-overlay  
        droidcam-obs
        obs-freeze-filter 
        obs-livesplit-one 
        obs-replay-source
        obs-move-transition
        obs-transition-table
        obs-pipewire-audio-capture
        # obs-backgroundremoval
        advanced-scene-switcher
      ];
    })

    blender # 3D modelling tool
    blockbench # 3D modelling tool but for voxels and Minecraft
    lunacy # Free design software that keeps your flow with AI tools and built-in graphics
    fontforge # Font editor
    fontbakery # Tool for checking the quality of font projects
    birdfont # Font editor which can generate fonts in TTF, EOT, SVG and BIRDFONT format
    pureref # Unfree

    heimdall # Cross-platform tool suite to flash firmware onto Samsung devices
    
    localsend # Open source cross-platform alternative to AirDrop

    geary # an email application built around conversations, for the GNOME.
    fractal # Matrix group messaging app
    signal-desktop # Private, simple, and secure messenger
    
    # penpot-desktop
    kdePackages.kolourpaint # Easy-to-use paint program
    krita # Free and open source painting application
    pastel # Command-line tool to generate, analyze, convert and manipulate colors

    syncplay # Free software that synchronises media players
    yt-dlp # video downloader
    ytmdl # music/metadata downloader
    streamlink # pipes video streams
    soulseekqt # official qt soulseek client
    # exactaudiocopy # Precise CD audio grabber for creating perfect quality rips using CD and DVD drives

    libreoffice-qt6 # office suite
    scribus # indesign alternative press publishing tool
    pandoc # Conversion between documentation formats
    sc-im # Spreadsheet Calculator Improvised -- An ncurses spreadsheet program for terminal
    bagels # Powerful expense tracker that lives in your terminal
    # moneyterm # TUI expense and budget tracker

    genesys # Family tree generator
    
    gkrellm # Themeable process stack of system monitors
    warpd # Modal keyboard driven interface for mouse manipulation
    # cmatrix

    graphviz # Graph visualization tools
    scc # Very fast accurate code counter with complexity calculations and COCOMO estimates written in pure Go
    qrtool # A utility for encoding or decoding QR codes
    # textual-paint # TUI image editor inspired by MS Paint # build error
    upiano # Piano in your terminal

    calcure # Modern TUI calendar and task manager with minimal and customizable UI
    clock-rs # Digital clock that runs in terminal. Rust rewrite of tty-clock
    # mapscii # a Braille & ASCII world map renderer for your console. # build error
    tz # Time zone helper
    git-who # Git blame for file trees
    fork-cleaner # Quickly clean up unused forks on your GitHub account
    bcal # Storage conversion and expression calculator
    fend # Arbitrary-precision unit-aware calculator

    cowsay # Program which generates ASCII pictures of a cow with a message
    fortune # Program that displays a pseudorandom message from a database of quotations
    fortune-kind # Kinder, curated fortune, written in rust
    taoup # Tao of Unix Programming
    clolcat # Much faster lolcat -> Rainbow version of cat
    terminaltexteffects # A collection of visual effects that can be applied to terminal piped stdin text

    sl # Steam Locomotive runs across your terminal when you type 'sl'. Ultimate joke command by Masashi Toyoda.
    neo # Simulates the digital rain from "The Matrix"
    pipes # Animated pipes terminal screensaver
    sssnake # Snake that plays itself in terminal
    cbonsai # Grow bonsai trees in your terminal
    figlet # Program for making large letters out of ordinary text
    dwt1-shell-color-scripts # Collection of shell color scripts collected by Derek Taylor
    linuxwave # Generate music from the entropy of Linux

    ttyper
    typioca # Cozy typing speed tester in terminal

  ]) ++ ( with pkgs-unstable; [
    davinci-resolve # Professional video editing, color, effects and audio post-processing

    halloy # IRC application
    vesktop # Alternate client for Discord with Vencord built-in (Has screensharing bug fixes for Wayland systems)
    jmusicbot # A Discord music bot that's easy to set up and run yourself
    # zoom-us
    # Note: don't forget to add { "SKIP_HOST_UPDATE": true } in ~/.config/discord (or vencord maybe)/settings.json
    # dorion # Tiny alternative Discord client (Will try this later, but won't open with nix-shell for some reason, might be related to misconfigured desktop portal.)
    # discord # All-in-one cross-platform voice and text chat for gamers (Doesn't have any fixes for more than 5yrs old blurry screenshare bug.)
    beeper # Useful for connecting various messaging platforms but as of 4.0, it's invisible in Wayland. Deleting GPU cache also doesn't work except starting with --disable-gpu parameter.
  ]);
  # Android Debug Bridge
  programs.adb.enable = true;

}
