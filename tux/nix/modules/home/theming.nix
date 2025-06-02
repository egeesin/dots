{pkgs, ...}: {
# { pkgs, ... }: let
  # theme = {
  #   name = "adw-gtk3-dark";
  #   package = pkgs.adw-gtk3;
  # };
  # font = {
  #   name = "Ubuntu Nerd Font";
  #   package = pkgs.nerd-fonts.ubuntu;
  #   size = 11;
  # };
  # cursorTheme = {
  #   name = "Qogir";
  #   size = 24;
  #   package = pkgs.qogir-icon-theme;
  # };
  # iconTheme = {
  #   name = "MoreWaita";
  #   package = pkgs.morewaita-icon-theme;
  # };
# }
# environment.sessionVariables.GTK_THEME = "Adwaita:dark";
# in {
  home = {
    # Based on https://github.com/Aman9das/zaneyos/blob/bcecd853b5be083ebc9ba7a943db22e93f9a9e47/config/home/gtk-qt.nix
    packages = with pkgs; [
      # theme.package
      # font.package
      # cursorTheme.package
      # iconTheme.package

      libcanberra-gtk3 # System sounds
      gsound

      libsForQt5.kio
      kdePackages.kio

      # libsForQt5.qt5ct
      # qt6ct

      libsForQt5.qt5.qtwayland
      kdePackages.qtwayland
      
      # kdePackages.breeze
      # libsForQt5.breeze-qt5
    ];
    # sessionVariables = {
    #   XCURSOR_THEME = cursorTheme.name;
    #   XCURSOR_SIZE = "${toString cursorTheme.size}";
    #   GTK_THEME = "adw-gtk3-dark";
    # };
    # 
    # pointerCursor = {
    #   gtk.enable = true;
    #   name = "Catppuccin-Mocha-Light-Curosrs";
    #   package = pkgs.catppuccin-cursors.mochaLight;
    #   size = 16;
    # };
    # pointerCursor = cursorTheme {
    #   gtk.enable = true;
    #   x11.enable = true;
    # };
  };
  gtk = { # Multi-platform toolkit for creating graphical user interfaces.
    enable = true;
    # font = {
    #   name = "Alegreya Sans";
    #   size = 13;
    # };
    # theme = {
    #   name = "Breeze-Dark";
    #   package = pkgs.libsForQt5.breeze-gtk;
    # };
    # iconTheme = {
    #   name = "Papirus-Dark";
    #   package = pkgs.catppuccing-papirus-folders.override {
    #     flavor = "mocha";
    #     accent = "lavender";
    #   };
    # };
    # cursorTheme = { # Already enabled in Stylix
    #     package = pkgs.posy-cursors;
    #     name = if (config.stylix.polarity == "light") then "Posy_Cursor" else "Posy_Cursor_Black";
    #     size = 24;
        # name = "Catppuccin-Mocha-Light-Cursors";
        # package = pkgs.catppuccin-cursors.mochaLight;
        # size = 36;
    # };
    # iconTheme = { # Already enabled in Stylix
    #   name = "Papirus-Dark";
    #   package = pkgs.papirus-icon-theme;
    # };
    gtk3.extraConfig = {
      gtk-application-prefer-dark-theme = 1;
    };
    gtk4.extraConfig = {
      gtk-application-prefer-dark-theme = 1;
    };
  };



   
  qt = {
    enable = true;
    # platformTheme.name = "qtct";
    # platformTheme.name = "gnome";
    # style = "adwaita-dark";
    # style = {
      # name = "Breeze-Dark";
    #   name = "Breeze-Dark";
    #   name = "kvantum";
    #   package = pkgs.kdePackages.breeze;
    # };
  };

  # home.packages = with pkgs; [
    # (catppuccin-kvantum.override {
    #   accent = "Blue";
    #   variant = "Macchiato";
    # })
    # kdePackages.qtstyleplugin-kvantum
    # libsForQt5.qt5ct
    # papirus-folders
  # ];
  # xdg.configFile = {
  #   "kvantum/ArcDark".source = "${pkgs.arc-kde-theme}/share/kvantum/ArcDark";
  #   "kvantum/kvantum.kvconfig".text = "[General]\ntheme=ArcDark";
  # }
   
  dconf = {
    enable = true;
    settings = {
  #   "org/gnome/desktop/interface" = {
  #     gtk-theme = "Breeze-Dark";
  #     color-scheme = "prefer-dark";
  #   };
      "org/gnome/desktop/interface" = {
        color-scheme = "prefer-dark";
      };
      "org/freedesktop/appearance" = {
        color-scheme = 1;
      };
    };
  };
  stylix = { # theming framework for NixOS that applies color schemes, wallpapers,
  # and fonts to a wide range of applications.
    iconTheme = {
      enable = true;
      dark = "Papirus-Dark";
      light = "Papirus-Light";
      package = pkgs.papirus-icon-theme;
    };
    targets = {
      # waybar.addCss = true;
      # kde.enable = true; # Should work as of 25.05 channel.
      hyprpaper.enable = true;
      btop.enable = false; # TTY option looks better IMO
      alacritty.enable = false; # as of 25.05 i'm getting "undefined variable: bright-yellow" errors while rebuilding.
    };
  };
}
