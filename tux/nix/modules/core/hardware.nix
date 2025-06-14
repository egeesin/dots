{ ... }:
{
  hardware = {

    # Bluetooth
    bluetooth.enable = true;
    bluetooth.powerOnBoot = true;

   # Enable OpenGL
    graphics = {
      enable = true;
      enable32Bit = true; # for Wine
    };

    # openrazer.enable = true;
    # opentabletdriver = {
    #   enable = true;
    #   daemon.enable = true;
    # };

    # fancontrol = {
    #   enable = true;
    #   config = {
    #     # requires config too
    #   };
    # };
    # trackpoint.enable = true;
    # steam-hardware.enable = true;
    # xone.enable = true;
    # xpadneo.enable = true;
    # keyboard.qmk.enable = true;
    # enableRedistributableFirmware = true;
  };
}
