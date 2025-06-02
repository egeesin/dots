{ lib,pkgs, ... }:

{
  services.hypridle = {
    enable = true;
    settings = {
      # 
      # https://wiki.hyprland.org/Hypr-Ecosystem/hypridle/#listeners
      general = {
          lock_cmd = "pidof hyprlock || ${lib.getExe pkgs.hyprlock}"; # runs hyprlock if it is not already running (this is always run when "loginctl lock-session" is called) 
          # unlock_cmd = "killall hyprlock"; # kills hyprlock when unlocking (this is always run when "loginctl unlock-session" is called)
          before_sleep_cmd = "loginctl lock-session";    # ensures that the session is locked before going to sleep
          after_sleep_cmd = "hyprctl dispatch dpms on"; # turn of screen after sleep (not strictly necessary, but just in case)
          ignore_dbus_inhibit = false;             # whether to ignore dbus-sent idle-inhibit requests (used by e.g. firefox or steam)
      };



      listener = [
        # { # turn off screen faster if session is already locked (disabled by default)
        #   timeout = 30;                            # 30 seconds
        #   on-timeout = pidof hyprlock && hyprctl dispatch dpms off # turns off the screen if hyprlock is active
        #   on-resume = pidof hyprlock && hyprctl dispatch dpms on    # command to run when activity is detected after timeout has fired.
        # };
        { # Warn
          timeout = 1800; # 9 min
          on-timeout = "notify-send 'You\'re idle.'"; # command to run when timeout has passed
          on-resume = "notify-send 'No longer idle.'";  # command to run when activity is detected after timeout has fired.
        }
        { # Screen Lock
          timeout = 2400; # 2 hours (120*20)
          # on-timeout = "loginctl lock-session"; # command to run when timeout has passed
          on-timeout = "${lib.getExe pkgs.hyprlock}"; # command to run when timeout has passed
          #on-resume = "notify-send -i $iDIR ' System Unlocked!'";  # command to run when activity is detected after timeout has fired.
        }
        # { # Turn off screen (disabled by default)
        #   timeout = 630;                            # 10.5 min
        #   on-timeout = "hyprctl dispatch dpms off";  # command to run when timeout has passed
        #   on-resume = "hyprctl dispatch dpms on";    # command to run when activity is detected after timeout has fired.
        # };

        # { # Suspend (disabled by default)
        #   timeout = 1200;                            # 20 min
        #   on-timeout = "systemctl suspend"; # command to run when timeout has passed
        #   on-resume = "notify-send -i $iDIR ' Oh! you\'re back' 'Hello !!!'";  # command to run when activity is detected after timeout has fired.
        # };
      ];
    
    };
  };
}
