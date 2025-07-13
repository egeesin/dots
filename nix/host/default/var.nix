# Based on https://gitlab.com/Zaney/zaneyos/-/blob/main/hosts/default/variables.nix
{
  # Git Configuration ( For Pulling Software Repos )
  gitUsername = "Ege Esin";
  gitEmail = "aegean@duck.com";

  # Hyprland Settings
  extraMonitorSettings = "";

  # Waybar Settings
  clock24h = false;

  # Program Options
  editor = "hx";
  browser = "zen"; # Set Default Browser (google-chrome-stable for google-chrome)
  terminal = "alacritty"; # Set Default System Terminal
  terminalfloating = "alacritty --class floating";
  fileManager = "dolphin";
  launcherMenu = "walker";
  # launcherMenu = "ulauncher";
  # launcherMenu = "rofi --show drun";

  # https://github.com/alexandrunastase/ro-de-keyboard-layout/blob/master/evdev.lst
  keyboardModel = "pc104";
  keyboardLayout = "tr";
  keyboardVariant = "alt";
  keyboardOptions = [
    "caps:escape"
    # "escape:caps"
    # "grp:alt_caps_toggle"
    # "caps:super"
  ];

  # For Nvidia Prime support
  # intelID = "PCI:1:0:0";
  # nvidiaID = "PCI:0:2:0";

  # Enable NFS
  # enableNFS = true;

  # Enable Printing Support
  printEnable = false;

  # Set Stylix Image
  wallpaper = ../../wallpaper.png;

  # Set Waybar
  # Includes alternates such as waybar-curved.nix & waybar-ddubs.nix
  # waybarChoice = ../../module/home/waybar/waybar-simple.nix;

  # Set Animation style
  # Available options are:
  # animations-def.nix  (default)
  # animations-end4.nix (end-4 project)
  # animations-dynamic.nix (ml4w project)
  # animChoice = ../../module/home/hyprland/animations-def.nix;
}
