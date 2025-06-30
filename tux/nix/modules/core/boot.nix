{ pkgs, inputs, ... }:

{
  boot = {
    # kernelPackages = pkgs.linuxPackages_zen;
    # Rest of it are in hosts/<HOSTNAME>/hardware
    # kernel.sysctl = { "vm.max_map_count" = 2147483642; };
    # Dual-boot: https://nixos.wiki/wiki/Dual_Booting_NixOS_and_Windows
    loader = {
      timeout = 4;
      efi.canTouchEfiVariables = true; # Windows is installed on another disk with a separate EFI partition
      grub = {
        enable = true;
        efiSupport = true;
        devices = [ "nodev" ];
        useOSProber = true; # Auto-detect other systems on the machine
        # https://github.com/Lxtharia/minegrub-theme#nixos-module-flake
        # theme = "${pkgs.kdePackages.breeze-grub}/grub/themes/breeze";
        minegrub-theme = {
          enable = true;
          # splash = "100% Flakes!";
          splash = "EGE IS YOU!";
          background = "background_options/1.8  - [Classic Minecraft].png";
          boot-options-count = 4;
        };
        # Automatically select last chosen OS
        default = "saved";
        extraEntries = "GRUB_SAVEDEFAULT=true";
      };
    };


    # Appimage Support
    # binfmt.registrations.appimage = {
    #   wrapInterpreterInShell = false;
    #   interpreter = "${pkgs.appimage-run}/bin/appimage-run";
    #   recognitionType = "magic";
    #   offset = 0;
    #   mask = ''\xff\xff\xff\xff\x00\x00\x00\x00\xff\xff\xff'';
    #   magicOrExtension = ''\x7fELF....AI\x02'';
    # };
  
    plymouth = {
      enable = true;
      # theme = "green_blocks";
      theme = "blahaj";
      # theme = "mc";
      themePackages = with pkgs; [
        plymouth-blahaj-theme
        # By default we would install all themes
        # (adi1090x-plymouth-themes.override {
        #   selected_themes = [ "green_blocks" ];
        # })
      # ] ++ [
        # inputs.plymouth-minecraft-theme.packages."${system}".plymouth-minecraft-theme
      ];
    };

    # Enable "Silent Boot"
    # consoleLogLevel = 3;
    consoleLogLevel = 0;
    initrd.verbose = false;
    kernelParams = [
      "quiet" # #tell the kernel to not be verbose
      "splash"
      "boot.shell_on_fail"
      "loglevel=3" # kernel log message level  # 1: system is unusable | 3: error condition | 7: very verbose
      # disable systemd status messages
      # rd prefix means systemd-udev will be used instead of initrd
      "systemd.show_status=false" 
      "rd.systemd.show_status=false" 
      # "rd.systemd.show_status=auto" 
      "udev.log_priority=3" # udev log message level
      "rd.udev.log_level=3" # lower the udev log level to show only errors or worse
      # disable the cursor in vt to get a black screen during intermissions
      "vt.global_cursor_default=0"
    ];
    # Hide the OS choice for bootloaders.
    # It's still possible to open the bootloader list by pressing any key
    # It will just not appear on screen unless a key is pressed
    # loader.timeout = 0;

    # Enable NTFS support at boot
    supportedFilesystems = [ "ntfs" ];
  };

  # https://nixos.wiki/wiki/NTFS
  # $ sudo su # Go root mode
  # $ umount /dev/nvme0n1p3
  # $ ntfsusermap /dev/nvme0n1p3
  # Use ntfsusermap to map permissions from Windows in sudo and make sure to unmount targeted NTFS device
  # https://github.com/tuxera/ntfs-3g/wiki/Using-ntfsusermap-to-Build-a-User-Mapping-File#linux-version
  # $ mount -t ntfs-3g -o permissions /dev/nvme0n1p3 /mnt/ege-win # Remount in order to move UserMapping 
  # $ mv UserMapping /mnt/ege-win/.NTFS/UserMapping
  # $ umount /dev/nvme0n1p3 # Remount again to apply changes.
  # $ mount -t ntfs-3g -o permissions /dev/nvme0n1p3 /mnt/ege-win
  # $ exit # Exit root mode
  fileSystems."/mnt/ege-win" = {
    device = "/dev/nvme0n1p3";
    fsType = "ntfs-3g";
    # options = [ "rw" "uid=1000"];
    options = [ "defaults" "uid=1000" "gid=100" "windows_names" ];
    # options = [ "rw" "uid=1000" "gid=100" "windows_names" ];
  };
  # If the disk is still in read-only, in order to confirm it type this
  # journalctl -b0 | grep -i "The disk contains an unclean file system"
  # If there's a log then disable fast boot in Windows.
  # https://learn.microsoft.com/en-us/archive/technet-wiki/25908.fast-startup-how-to-disable-if-it-s-causing-problems
  # Also if you shutdown Windows instead of restarting this kinda fixes it.

  # For controlling monitor brightness
  # services.udev.enable = true;
  services.udev.extraRules = ''
    SUBSYSTEM=="i2c-dev", ACTION=="add", \
      ATTR{name}=="NVIDIA i2c adapter*", \
      TAG+="ddcci", \
      TAG+="systemd", \
      ENV{SYSTEMD_WANTS}+="ddcci@$kernel.service"
  '';
  # https://www.ddcutil.com/i2c_permissions/

  systemd.services."ddcci@" = {
    scriptArgs = "%i";
    script = ''
      echo Trying to attach ddcci to $1
      i=0
      id=$(echo $1 | cut -d "-" -f 2)
      if ${pkgs.ddcutil}/bin/ddcutil getvcp 10 -b $id; then
        echo ddcci 0x37 > /sys/bus/i2c/devices/$1/new_device
      fi
    '';
    serviceConfig.Type = "oneshot";
  };
}
