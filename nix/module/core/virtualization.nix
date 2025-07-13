# {pkgs, ...}: {
{...}: {
  virtualisation = {
    waydroid.enable = false;
    # Don't forget to fetch Waydroid images.
    # $ sudo waydroid init
    # First setup & usage: https://wiki.nixos.org/wiki/Waydroid
  
    # Only enable either docker or podman -- Not both
    libvirtd.enable = false;
    docker.enable = false;
    podman.enable = false;
  };
  programs = {
    virt-manager.enable = false;
  };
  # environment.systemPackages = with pkgs; [
    # virt-viewer # View Virtual Machines
  # ];
}
