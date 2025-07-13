{
  pkgs,
  # pkgs-unstable,
  config,
  # lib,
  host,
  ...
}: let

  inherit (import ../../host/${host}/var.nix) wallpaper;

  # https://tinted-theming.github.io/tinted-gallery/
  # theme = "${pkgs.base16-schemes}/share/themes/everforest-dark-hard.yaml";
  # theme = "${pkgs.base16-schemes}/share/themes/gruvbox-light-medium.yaml";
  # theme = "${pkgs.base16-schemes}/share/themes/gruvbox-dark-hard.yaml";
  # theme = "${pkgs.base16-schemes}/share/themes/terracotta-dark.yaml";
  theme = "${pkgs.base16-schemes}/share/themes/mocha.yaml";
  # theme = "${pkgs.base16-schemes}/share/themes/monokai.yaml";
  # theme = "${pkgs.base16-schemes}/share/themes/gotham.yaml";
  # theme = "${pkgs.base16-schemes}/share/themes/eva.yaml";
  # theme = "${pkgs.base16-schemes}/share/themes/harmonic16-dark.yaml";
  # theme = "${pkgs.base16-schemes}/share/themes/kanagawa.yaml";
  # theme = "${pkgs.base16-schemes}/share/themes/kimber.yaml";
  # theme = "${pkgs.base16-schemes}/share/themes/solarflare.yaml";
  # theme = "${pkgs.base16-schemes}/share/themes/precious-dark-fifteen.yaml";
  # theme = "${pkgs.base16-schemes}/share/themes/jabuti.yaml";
  # theme = "${pkgs.base16-schemes}/share/themes/windows-10.yaml";
  # theme = "${pkgs.base16-schemes}/share/themes/vesper.yaml";
  # theme = "${pkgs.base16-schemes}/share/themes/hopscotch.yaml";
  # theme = "${pkgs.base16-schemes}/share/themes/tarot.yaml";
  # theme = "${pkgs.base16-schemes}/share/themes/oceanicnext.yaml";

  # generatedImage = pkgs.runCommand "${wallpaper}" { } ''
  #   COLOR=$(${lib.getExe pkgs.yq} -r .palette.base00 ${theme})
  #   ${lib.getExe pkgs.graphicsmagick} convert -size 1920x1920 xc:$COLOR $out
  # '';
in {
  environment.systemPackages = with pkgs; [
    gowall
  ];
  # Default font settings
  fonts = {
    fontDir.enable = true; # For exposing fonts dirs to Flatpak apps.
    fontconfig = {
      enable = true;
      defaultFonts = {
        serif = [ config.stylix.fonts.serif.name ];
        sansSerif = [ config.stylix.fonts.sansSerif.name ];
        monospace = [ config.stylix.fonts.monospace.name ];
      };
      useEmbeddedBitmaps = true;
    };
    packages = (with pkgs; [
      inter-nerdfont
      # fantasque-sans-mono
      # nerdfonts.symbols-only # attribute deosn't exist for some reason
      # nerdfonts # (Includes all patched fonts)
      commit-mono
      # twemoji-color-font
      # font-awesome
      # ultimate-oldschool-pc-font-pack
      # twemoji-color-font
      # gelasio # Font which is metric-compatible with Microsoft's Georgia
      comic-neue # Casual type face: Make your lemonade stand look like a fortune 500 company
      comic-relief # Font metric-compatible with Microsoft Comic Sans
      garamond-libre
      # alegreya-sans # Humanist sans serif family with a calligraphic feeling
      minecraftia # First we mine, then we craftia. Let's Minecraftia!
      xkcd-font # title.
      corefonts # Microsoft's TrueType core fonts for the Web
      open-fonts # Collection of beautiful free and open source fonts
      kreative-square # Fullwidth scalable monospace font designed specifically to support pseudographics, semigraphics, and private use characters
      nerd-fonts.symbols-only # (Only includes symbols) available in unstable/25.05
    # ]) ++ (with pkgs-unstable; [
    ]);
  };
  # Styling Options
  stylix = {
    enable = true;
    # image = generatedImage;
    image = wallpaper;
    # image = pkgs.fetchurl {
    #   url = "https://r4.wallpaperflare.com/wallpaper/643/872/938/astronaut-relaxing-black-background-floater-space-hd-wallpaper-58a65d781020dc68109c91ee5842b45a.jpg";
    #   sha256 = "f12b95cecfbca53656d61702f951f6c6b1318b8bd6e5d2a2390c063647128baa";
    # };
    base16Scheme = theme;
    polarity = "dark";
    # polarity = "either";
    opacity.terminal = 0.85;

    cursor = {
      package = pkgs.posy-cursors;
      name = "Posy_Cursor_Black";
      size = 24;
      # name = "Apple-Custom";
      # package =
      #   with config.lib.stylix.colors.withHashtag;
      #   packages.${pkgs.system}.apple-cursor.override {
      #     background_color = base00;
      #     outline_color = base07;
      #     accent_color = base0D;
      #   };
      # size = 21;
      # package = pkgs.apple-cursor;
      # name = "macOS";
      # size = 24;
    };
    fonts = {
      sansSerif =
      # config.stylix.fonts.monospace;
      {
        # package = pkgs.inter;
        package = pkgs.alegreya-sans;
        name = "Alegreya Sans";
        # package = pkgs.inter-nerdfont;
        # name = "Inter Nerd Font";
        # package = inputs.apple-fonts.package.${pkgs.system}.sf-pro-nerd;
        # name = "SFProDisplay nerd Font";
      };
      monospace = {
        # package = pkgs.fantasque-sans-mono;
        # name = "Fantasque Sans Mono";
        # package = pkgs-unstable.nerd-fonts.fantasque-sans-mono;
        package = pkgs.nerd-fonts.fantasque-sans-mono;
        name = "FantasqueSansM Nerd Font";
        # package = pkgs.commit-mono;
        # name = "Commit Mono";
        # package = pkgs.nerd-fonts.hack;
        # package = pkgs.nerd-fonts.iosevka;
        # package = pkgs.nerd-fonts.gohufont;
        # package = pkgs.nerd-fonts.monaspace;
        # package = pkgs.nerd-fonts.commit-mono;
        # package = pkgs.nerd-fonts.atkynson-mono;
        # package = pkgs.nerd-fonts.recursive-mono;
        # package = pkgs.nerd-fonts.comic-shanns-mono;
      };
      serif =
      # config.stylix.fonts.monospace;
      {
        package = pkgs.gelasio;
        name = "Gelasio";
      };
      emoji =
      {
        package = pkgs.twemoji-color-font;
        name = "Twitter Color Emoji";
      };
      sizes = {
        # Alegreya Sans looks small comparing to other sans fonts
        # so it must have higher unit except terminal.
        applications = 13;
        terminal = 13;
        desktop = 13;
        popups = 13;

        # applications = 11;
        # terminal = 13;
        # desktop = 10;
        # popups = 11;

        # applications = 12;
        # terminal = 14;
        # desktop = 11;
        # popups = 12;
      };
    };
    targets = {
      plymouth.enable = false; # because blahaj is better.
      grub.enable = false; # Must not conflict with minegrub theme.
      qt = {
        enable = true;
        # platform = lib.mkForce "qtct";
        # platform = lib.mkForce "gnome";
        # platform = lib.mkForce "adwaita";
      };
    };
  };

}
