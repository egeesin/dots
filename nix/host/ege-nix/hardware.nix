# Do not modify this file!  It was generated by ‘nixos-generate-config’
# and may be overwritten by future invocations.  Please make changes
# to /etc/nixos/configuration.nix instead.
# { config, lib, pkgs, modulesPath, ... }: {
{
config,
pkgs,
lib,
modulesPath,
... }:
{
  imports = [
    (modulesPath + "/installer/scan/not-detected.nix")
  ];

  boot = {
    initrd = {
      availableKernelModules = [
       "nvme"
       "xhci_pci"
       "ahci"
       "usbhid"
       "usb_storage"
       "sd_mod"
      ];
      kernelModules = [];
    };
    # $ nix repl # List Linux kernels
    # kernelPackages = pkgs.linuxPackages_latest; # This acts funny when you try to install Nvidia driver
    blacklistedKernelModules = [ "k10temp" ]; # on behalf of zenpower
    kernelModules = [
      "kvm-amd" # # amd virtualization
      "v4l2loopback" # Virtual Camera
      "snd-aloop" # Virtual Microphone
      # For controlling monitor brightness
      "zenpower" # zenpower is for reading cpu info, i.e voltage
      "coretemp"
      "msr" # x86 CPU MSR access device
      "i2c-dev"
      "ddcci_backlight"
    ];
    extraModulePackages = [
      config.boot.kernelPackages.v4l2loopback
      config.boot.kernelPackages.ddcci-driver
    ];

    # For Bluetooth and adding OBS Virtual Cam
    extraModprobeConfig = ''
    options v4l2loopback devices=1 video_nr=1 card_label="VirtualCam" exclusive_caps=1
    options bluetooth disable_ertm=1
    '';
    # exclusive_caps: Chromium, Electron, etc. will only show device when actually streaming.

  };
  hardware.cpu.amd.updateMicrocode = lib.mkDefault config.hardware.enableRedistributableFirmware;

  # For SSDs
  # services.fstrim.enable = true;
  fileSystems = {
    "/" = {
      device = "/dev/disk/by-uuid/2814f870-f425-447e-8e66-dc5d72d80ce6";
      fsType = "ext4";
    };

    "/boot" = {
      device = "/dev/disk/by-uuid/D6F8-D5B6";
      fsType = "vfat";
      options = [ "fmask=0077" "dmask=0077" ];
    };
  };

  swapDevices =
    [ { device = "/dev/disk/by-uuid/749e67f6-83c5-436a-bfdf-6f2b342d7eb3"; }
    ];

  environment.systemPackages = with pkgs; [
    zenmonitor # Monitoring software for AMD Zen-based CPUs
  ];
  # Enables DHCP on each ethernet and wireless interface. In case of scripted networking
  # (the default) this is the recommended approach. When using systemd-networkd it's
  # still possible to use this option, but it's recommended to use it in conjunction
  # with explicit per-interface declarations with `networking.interfaces.<interface>.useDHCP`.
  networking.useDHCP = lib.mkDefault true;
  # networking.interfaces.enp8s0.useDHCP = lib.mkDefault true;

  nixpkgs.hostPlatform = lib.mkDefault "x86_64-linux";
  hardware.i2c.enable = true; # For Accessing monitor/device brightness control at user-level.
  hardware.enableAllFirmware = true; # Whether to enable all firmware regardless of license
}
