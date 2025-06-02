{inputs,pkgs, ...}: {
  environment.systemPackages = with pkgs; [
    xdg-user-dirs # Tool to help manage well known user directories like the desktop folder and the music folder
    xdg-user-dirs-gtk # Companion to xdg-user-dirs that integrates it into the GNOME desktop and GTK applications
  ];
  environment.etc."xdg/user-dirs.defaults".text = ''
    DESKTOP=$HOME/Desktop
    DOWNLOAD=$HOME/Downloads
    TEMPLATES=$HOME/Templates
    PUBLICSHARE=$HOME/Public
    DOCUMENTS=$HOME/Documents
    MUSIC=$HOME/Music
    PICTURES=$HOME/Pictures
    VIDEOS=$HOME/Videos
  '';
  xdg = {
    portal = {
      enable = true; # enable xdg desktop integration
      xdgOpenUsePortal = true; # https://github.com/NixOS/nixpkgs/issues/160923
      wlr.enable = true; # enable desktop portal for wlroots-based desktops
      extraPortals = with pkgs; [
        xdg-desktop-portal-gtk
        xdg-desktop-portal-gnome
        kdePackages.xdg-desktop-portal-kde
        libsForQt5.xdg-desktop-portal-kde
        xdg-desktop-portal-hyprland
        # https://search.nixos.org/options?channel=24.11&show=xdg.portal.extraPortals&from=0&size=50&sort=relevance&type=packages&query=xdg
        # GNOME and KDE already adds xdg-desktop-portal-gtk; and
        # xdg-desktop-portal-kde respectively. On other desktop environments
        # you probably want to add them yourself.
      ];
      configPackages = [inputs.hyprland.packages.${pkgs.system}.hyprland];
    };
  };
}
