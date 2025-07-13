{host, ...}: let
  inherit (import ../../host/${host}/var.nix) printEnable;
in {
  services = {
    # Enable CUPS to print documents.
    printing = {
      enable = printEnable;
      drivers = [
        # pkgs.hplipWithPlugin
      ];
    };
    avahi = {
      enable = printEnable;
      nssmdns4 = true;
      openFirewall = true;
    };
    ipp-usb.enable = printEnable;
  };
}
