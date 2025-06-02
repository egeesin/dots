{
  inputs,
  pkgs,
  username,
  ...
}: let
  tuigreet = "${pkgs.greetd.tuigreet}/bin/tuigreet";
  # hyprland-session = "${pkgs.hyprland}/share/wayland-sessions";
  hyprland-session = "${inputs.hyprland.packages.${pkgs.system}.hyprland}/share/wayland-sessions";
 in {
  services.greetd = {
    enable = true;
    vt = 3;
    settings = {
      default_session = {
        user = username;
        # command = "${tuigreet} --time --remember --remember-session --sessions Hyprland"; # start Hyprland with a TUI login manager
        command = "${tuigreet} --time --remember --remember-session --sessions ${hyprland-session}"; # start Hyprland with a TUI login manager
      };
    };
  };
  # systemd.services.greetd.serviceConfig = {
  #   Type = "idle";
  #   StandardInput = "tty";
  #   StandardOutput = "tty";
  #   StandardError = "journal"; # Without this errors will spam on screen
  #   # Without these bootlogs will spam on screen
  #   TTYReset = true;
  #   TTYVHangup = true;
  #   TTYVTDisallocate = true;
  # };
}
