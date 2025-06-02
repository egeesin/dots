{pkgs, pkgs-unstable, ...}: {
  environment.systemPackages = ( with pkgs; [
    shopify-cli

    eartag
    picard # music tag editor
    cava # Cross-platform Audio Visualizer

    nvtopPackages.full
    nvfancontrol

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

    obs-studio # screen recorder/streamer
    obs-studio-plugins.wlrobs
    # obs-studio-plugins.obs-nvfbc # unstable says it's broken
    obs-studio-plugins.input-overlay  
    obs-studio-plugins.droidcam-obs
    obs-studio-plugins.obs-freeze-filter 
    obs-studio-plugins.obs-livesplit-one 
    obs-studio-plugins.obs-replay-source
    obs-studio-plugins.obs-move-transition
    obs-studio-plugins.obs-transition-table
    obs-studio-plugins.obs-pipewire-audio-capture
    obs-studio-plugins.advanced-scene-switcher

    blender # 3D modelling tool
    blockbench # 3D modelling tool but for voxels and Minecraft
    lunacy # Free design software that keeps your flow with AI tools and built-in graphics
    fontforge # Font editor
    fontbakery # Tool for checking the quality of font projects
    birdfont # Font editor which can generate fonts in TTF, EOT, SVG and BIRDFONT format
    pureref # Unfree

    localsend # Open source cross-platform alternative to AirDrop

    fractal # Matrix group messaging app
    signal-desktop # Private, simple, and secure messenger
    
    # penpot-desktop
    kdePackages.kolourpaint # Easy-to-use paint program
    krita # Free and open source painting application

    syncplay # Free software that synchronises media players
    yt-dlp # video downloader
    ytmdl # music/metadata downloader
    streamlink # pipes video streams
    soulseekqt # official qt soulseek client
    # exactaudiocopy # Precise CD audio grabber for creating perfect quality rips using CD and DVD drives

    libreoffice-qt6 # office suite
    scribus # indesign alternative press publishing tool

    genesys # Family tree generator
    
    gkrellm # Themeable process stack of system monitors
    warpd # Modal keyboard driven interface for mouse manipulation
    # cmatrix

    neo # Simulates the digital rain from "The Matrix"
    cowsay
    fortune # Program that displays a pseudorandom message from a database of quotations
    fortune-kind # Kinder, curated fortune, written in rust
    clolcat # Much faster lolcat -> Rainbow version of cat
    taoup # Tao of Unix Programming
    vitetris # Terminal-based Tetris clone by Victor Nilsson
    bsdgames # Ports of all the games from NetBSD-current that are free
    typespeed # Curses based typing game
    cbonsai # Grow bonsai trees in your terminal
    nbsdgames # A package of 18 text-based modern games
    pipes # Animated pipes terminal screensaver
    figlet
    linuxwave
    dwt1-shell-color-scripts
  ]) ++ ( with pkgs-unstable; [
    davinci-resolve # video editor
    vesktop # Alternate client for Discord with Vencord built-in (Has screensharing bug fixes for Wayland systems)
    # Note: don't forget to add { "SKIP_HOST_UPDATE": true } in ~/.config/discord (or vencord maybe)/settings.json
    # discord # All-in-one cross-platform voice and text chat for gamers (Doesn't have any fixes for more than 5yrs old blurry screenshare bug.)
    beeper # Useful for connecting various messaging platforms but as of 4.0, it's invisible in Wayland. Deleting GPU cache also doesn't work except starting with --disable-gpu parameter.
  ]);
  # Android Debug Bridge
  programs.adb.enable = true;
}
