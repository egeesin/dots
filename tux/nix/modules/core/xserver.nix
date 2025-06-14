{host,pkgs,  ...}: let
  inherit (import ../../hosts/${host}/variables.nix)
  keyboardModel
  keyboardLayout
  keyboardVariant
  keyboardOptions;
in {
 
  # Enable the X11 windowing system.
  services.xserver = {
    enable = true;
    exportConfiguration = true;
    # I only need this for having different kbd layouts. kinda weird this is false by default.
    # Yet people still rightfully complaining about it since 2016 here:
    # https://github.com/NixOS/nixpkgs/issues/19629
    # Configure keymap in X11
    xkb = {
      model = "${keyboardModel}";
      layout = "${keyboardLayout}";
      variant = "${keyboardVariant}";
      options = "${keyboardOptions}";
    };
    excludePackages = [ pkgs.xterm ];
    
  };
}
