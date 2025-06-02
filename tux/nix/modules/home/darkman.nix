{
  pkgs,
  ...
}: {
  # There's no service option for darkman yet
  # check this instead:
  # https://www.reddit.com/r/NixOS/comments/vbte46/comment/icay2l6/
  # https://git.sr.ht/~rycee/configurations/tree/e2ef1d303619670f28898315b2bdecb0793a4903/item/user/nettle.rycee.nix
  services.darkman = {
    enable = true;
    darkModeScripts = {
      gtk-theme = ''
        ${pkgs.dconf}/bin/dconf write \
          /org/gnome/desktop/interface/color-scheme "'prefer-dark'"
      '';
    };
    lightModeScripts = {
      gtk-theme = ''
        ${pkgs.dconf}/bin/dconf write \
          /org/gnome/desktop/interface/color-scheme "'prefer-light'"
      '';
    };
  };
}
