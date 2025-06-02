{pkgs, ...}: {

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
    kdePackages.discover # Optional: Install if you use Flatpak or fwupd firmware update sevice
    gearlever # manage AppImages with ease
  ];  
}
