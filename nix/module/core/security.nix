{pkgs, ...}: {
  security = {
    rtkit.enable = true; # Enable RealtimeKit for audio purposes
    polkit = {
      enable = true;
      extraConfig = ''
        polkit.addRule(function(action, subject) {
          if ( subject.isInGroup("users") && (
           action.id == "org.freedesktop.login1.reboot" ||
           action.id == "org.freedesktop.login1.reboot-multiple-sessions" ||
           action.id == "org.freedesktop.login1.power-off" ||
           action.id == "org.freedesktop.login1.power-off-multiple-sessions"
          ))
          { return polkit.Result.YES; }
        })
      '';
    };   
    pam.services.hyprlock = {};
    # pam.services.login.enableGnomeKeyring = true;
    # pam.services.swaylock = {
    #   text = ''auth include login '';
    # };
  };
  # systemd.user.services.polkit-gnome-authentication-agent-1 = {
  #   Unit.Description = "polkit-gnome-authentication-agent-1";

  #   Install = {
  #     WantedBy = [ "graphical-session.target" ];
  #     Wants = [ "graphical-session.target" ];
  #     After = [ "graphical-session.target" ];
  #   };

  #   Service = {
  #     Type = "simple";
  #     ExecStart = "${pkgs.polkit_gnome}/libexec/polkit-gnome-authentication-agent-1";
  #     Restart = "on-failure";
  #     RestartSec = 1;
  #     TimeoutStopSec = 10;
  #   };
  # };
}
