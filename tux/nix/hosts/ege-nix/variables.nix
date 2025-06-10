# Based on https://gitlab.com/Zaney/zaneyos/-/blob/main/hosts/default/variables.nix
# This is a better implementation, will steal some of it later:
# https://github.com/Aman9das/zaneyos/blob/aman9das/hosts/E14nix/options.nix
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
  # terminalfloating = "alacritty --class floating";
  terminalfloating = "alacritty --title floating";
  fileManager = "io.elementary.files";
  # fileManager = "dolphin";

  launcherMenu = "walker";
  # launcherMenu = "ulauncher";
  # launcherMenu = "rofi --show drun";
  # launcherMenu = "nwgdmenu";

  startMenu = "nwg-drawer";
  # startMenu = "nwg-menu";
  # startMenu = "ulauncher";
  # launcherMenu = "wofi --show drun";

  # $ setxkbmap -print -verbose 10
  # https://en.wikipedia.org/wiki/File:Physical_keyboard_layouts_comparison_ANSI_ISO_KS_ABNT_JIS.png
  # $ localectl list-x11-keymap-models
  keyboardModel = "pc105"; # ISO (L-shaped Enter)
  # keyboardModel = "pc104"; # ANSI (Dash-shaped Enter)

  # keyboardModel = "applealu_ansi";
  # keyboardModel = "applealu_iso";
  # keyboardModel = "chromebook";
  # keyboardModel = "hhk";
  # keyboardModel = "microsoftoffice";
  # keyboardModel = "microsoftsurface";
  # keyboardModel = "logitech";
  # keyboardModel = "kinesis";

  # https://github.com/alexandrunastase/ro-de-keyboard-layout/blob/master/evdev.lst
  # $ localectl list-x11-keymap-layouts
  keyboardLayout = "tr, us"; # Turkish as primary, English as secondary
  # "tr, tr, us"; # Turkish as primary and secondary, English as secondary

  # $ localectl list-x11-keymap-variants [layout]
  keyboardVariant = "alt,colemak_dh"; # (Alt-Q)
  # When multiple layouts set, to use default variant, keep it empty and add comma
  # "alt, f, colemak_dh"; # (Alt-Q for primary, F for secondary, CDH for tertiary)
  # "alt,colemak_dh"; # (Alt-Q for primary lyt., Colemak DH for secondary lyt.)
  # "f"; # (F) # F variant for Turkish # https://upload.wikimedia.org/wikipedia/commons/thumb/d/de/KB_Turkey_f_yeni.svg/500px-KB_Turkey_f_yeni.svg.png

  keyboardOptions =  "caps:escape_shifted_capslock, grp:alt_caps_toggle";
  # "caps:escape_shifted_capslock"; # Make Caps Lock an additional Esc, but Shift + Caps Lock is the regular Caps Lock
  # "grp:menu" # Press Menu button to switch between layouts
  # "grp:win_space_toggle" # Press Super+Space to switch between layouts
  # "grp:alt_caps_toggle" # Press Alt+Caps Lock to switch between layouts
  # "caps:escape"; # Make Caps Lock an additional Esc
  # "caps:swapescape"; # Swap Esc and Caps Lock
  # "ctrl:nocaps"; # Map Caps Lock as an additional Ctrl key
  # "ctrl:swapcaps"; # I'd probably use this if I'm using a laptop keyboard.
  # "caps:escape,grp:alt_caps_toggle,caps:super,eurosign:e";

  # For Nvidia Prime support
  # intelID = "PCI:1:0:0";
  # nvidiaID = "PCI:0:2:0";

  # Enable NFS
  # enableNFS = true;

  # Enable Printing Support
  printEnable = false;

  # Set Wallpaper
  wallpaper = ../../wallpaper.png; # Don't surround it with any quote marks.

  # Set Waybar
  # Includes alternates such as waybar-curved.nix & waybar-ddubs.nix
  # waybarChoice = ../../modules/home/waybar/waybar-simple.nix;

  # Set Animation style
  # Available options are:
  # animations-def.nix  (default)
  # animations-end4.nix (end-4 project)
  # animations-dynamic.nix (ml4w project)
  # animChoice = ../../modules/home/hyprland/animations-def.nix;
}
