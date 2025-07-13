{
  # lib,
  # config,
  # inputs,
  # pkgs,
  # minesddm,
  # profile,
  ...
}:
# }: let

# Based on: https://github.com/kriswill/dotfiles/blob/e1aee5d3851d8aac8d72918975fe3d488cd1159f/nixos/desktops/sddm.nix

# xcfg = config.services.xserver;

# weston-ini = pkgs.writeText "weston.ini" ''
#   [core]
#   xwayland=false
#   shell=fullscreen-shell.so

#   [keyboard]
#   keymap_model=${builtins.toString xcfg.xkb.model}
#   keymap_layout=${builtins.toString xcfg.xkb.layout}
#   keymap_options=${builtins.toString xcfg.xkb.options}
#   keymapvariant=

#   [libinput]
#   enable-tap=true
#   left-handed=false

#   [output]
#   name=DP-1
#   mode=1920x1080@120

#   [output]
#   name=HDMI-A-1
#   mode=off
# '';

# weston-command = lib.concatStringsSep " " [
#   "${lib.getExe pkgs.weston}"
#   "--shell=kiosk"
#   "-c ${weston-ini}"
# ];

# in {
{

  # Services to start in Linux system
  lib.mkIf pkgs.stdenv.targetPlatform.isLinux = {
	  services = {
	    libinput = {
	      enable = true; # Input Handling (touchpad support)
	      touchpad.disableWhileTyping = true;
	    };
	    fstrim.enable = true; # SSD Optimizer
	    gvfs.enable = true; # For mounting USB, adding Trash support in Nautilus & more
	    fwupd.enable = true; # Firmware updater (How to use: https://github.com/fwupd/fwupd#basic-usage-flow-command-line)
	    udisks2.enable = true; # Also for mounting USB & more
	    blueman.enable = true; # Bluetooth manager
	    tumbler.enable = true; # Image/video preview
	    gnome.gnome-keyring.enable = true;
	  };
  };

  # Services to start
  services = {
    # https://nixos.org/manual/nixos/stable/index.html#module-services-flatpak

    # rustdesk-server = {
    # https://search.nixos.org/options?channel=25.05&show=services.rustdesk-server.relay.extraArgs&from=0&size=50&sort=relevance&type=packages&query=rustdesk-server
    #   enable = true;
    #   openFirewall = true;
    #   # relay =
    #   # requires relay server arg
    # };

    # displayManager = {
    #   # defaultSession = "";
    #   # autoLogin.user = "ege"; # it'll be enabled when user is defined
    #   # displayManager.gdm.wayland = true;
    #   # displayManager.gdm.nvidiaWayland = true;
    #   sddm = {
    #     enable = true;
    #     package = pkgs.kdePackages.sddm;
    #     autoNumlock = false;
    #     # wayland.enable = true;
    #     wayland = {
    #       enable = true;
    #       compositor = lib.mkForce "weston";
    #       compositorCommand = weston-command;
    #     };
    #     theme = "minesddm";
    #     # settings = {
    #       # Autologin = {
    #       #   Session = "Hyprland";
    #       #   User = "ege";
    #       # };
    #       # Wayland = {
    #       #   CompositorCommand = "/nix/store/dxp225pbq50sxx9rkvb3y52p6l9w3rpl-weston-14.0.1/bin/weston --shell=kiosk -c /home/ege/.extra/backup/weston-for-sddm.ini";
    #       #   SessionDir = "${inputs.hyprland.packages.${pkgs.system}.hyprland}/share/wayland-sessions";
    #       # };
    #       # X11 = {
    #       #   Enable = false;
    #       # };
    #     # };
    #   };
    # };

    # Enable sound.
    pipewire = {
      enable = true;
      wireplumber.enable = true;
      alsa.enable = true;
      alsa.support32Bit = true;
      pulse.enable = true;
      jack.enable = true;
    };

    playerctld.enable = true;

    # Check this link for screen sharing under XWayland windows:
    # https://wiki.hyprland.org/Useful-Utilities/Screen-Sharing/#xwayland
    dbus.enable = true;

    # Enable the OpenSSH daemon.
    # https://nixos.wiki/wiki/SSH
    openssh = {
      enable = true;
      ports = [ 22 ];
      settings = {
        PasswordAuthentication = true;
        AllowUsers = null; # Allows all users by default. Can be [ "user1" "user2" ]
        UseDns = true;
        X11Forwarding = false;
        PermitRootLogin = "prohibit-password"; # "yes", "without-password", "prohibit-password", "forced-commands-only", "no"
      };
    };
    # Unblock Discord etc.
    dnscrypt-proxy2 = {
      enable = true;
      settings = {
        listen_addresses = ["127.0.0.1:53" "[::1]:53"];
      };
    };
    zapret = {
      enable = true;
      params = [
        "--dpi-desync=fake"
        "--dpi-desync-ttl=8"
      ];
    };
  };
}
