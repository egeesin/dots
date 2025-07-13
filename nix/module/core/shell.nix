{
  pkgs,
  username,
  ...
}: {
  programs.nh = {
    enable = true;
    clean = {
      enable = true;
      extraArgs = "--keep-since 7d --keep 5";
    };
    flake = "/${if pkgs.stdenv.isDarwin then "Users" else "home"}/${username}/.dots/";
  };

  programs.starship = {
      enable = true;
      settings.add_newline = false;
  };

  environment.systemPackages = with pkgs; [
    nix-output-monitor
    nvd
  ];
  environment.sessionVariables = {
    # If your cursor becomes invisible
    WLR_NO_HARDWARE_CURSORS = 1;
    # Hint electron apps to use wayland
    NIXOS_OZONE_WL = 1;
    # Required for firefox 98+, see:
    # https://github.com/elFarto/nvidia-vaapi-driver#firefox
    # EGL_PLATFORM = "wayland";
  };
}
