{
  lib,
  config,
  ...
}:
with lib;
let
  cfg = config.drivers.nvidia;
in
{
  options.drivers.nvidia = {
    enable = mkEnableOption "Enable Nvidia Drivers";
  };

  config = mkIf cfg.enable {
    services.xserver.videoDrivers = ["nvidia"]; # Load nvidia driver for Xorg and Wayland
    hardware.nvidia = {
      # Most wayland compositors need this
      modesetting.enable = true;
      # powerManagement.enable = false;
      powerManagement.finegrained = false;
      open = true; # should be true as I'm using Turing architecture
      nvidiaSettings = true;
      package = config.boot.kernelPackages.nvidiaPackages.beta;
      # https://nixos.wiki/wiki/Nvidia
      # https://www.nvidia.com/en-us/drivers/unix/
    };
  };
}
