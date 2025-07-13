{ lib, inputs, config, ... }:
{
  imports = [
    inputs.hyprshell.homeModules.hyprshell
  ];
  programs.hyprshell = {
  # https://github.com/H3rmt/hyprshell/blob/hyprshell-release/nix/module.nix
    enable = true;
    systemd.args = "-v";
    settings = {
      kill_bind = "ctrl+shift+alt, h";
      launcher = {
        max_items = 6;
        animate_launch_ms = 0;
        # show_when_empty = false;
        # plugins.applications = {
          # show_actions_submenu = true;
        # };
        plugins.websearch = {
          enable = true;
          engines = [{
              name = "Unduck";
              url = "https://unduck.link?q={}";
              key = "d";
          }];
        };
      };
      # windows = {
      #   enable = true;
      #   scale = 6; # Float between 0 and 15
      #   overview.open.key = "super";
      #   navigate = "tab";
        # switch = {
        #   enable = true;
        #   open = "alt";
          # navigate = "tab";
        # };
      # };
    };
    styleFile = lib.mkDefault ''
    --border-color: #${ config.lib.stylix.colors.base00 };
    --border-color-active: #${ config.lib.stylix.colors.base01 };

    --bg-color: #${ config.lib.stylix.colors.base01 };
    --bg-color-active: #${ config.lib.stylix.colors.base04 };

    --border-size: 2px;
    --border-radius: 13px;
    --border-style-secondary: solid;

    --text-color: #${ config.lib.stylix.colors.base05};

    --window-padding: 2px;

    .launch {
      animation: pulse 0.7s normal infinite;
    }
    .workspace {
      font-size: 18px;
      font-weight: bold;
      background: var(--bg-color);
      border: var(--border-size) solid var(--border-color);
      border-radius: var(--border-radius);
    }
    .workspace:hover {
      background-color: var(--bg-color-hover);
    }
    .workspace_special {
      border: var(--border-size) solid #${ config.lib.stylix.colors.base0A} /* yellow */
    }
    .workspace_active {
      border: var(--border-size) solid #${ config.lib.stylix.colors.base0E} /* purple */
    }
    .client {
      background: #${ config.lib.stylix.colors.base02};
    }
    .client_active {
      border: var(--border-size) solid #${ config.lib.stylix.colors.base0D}
    }
    @keyframes pulse {
      0% { background: var(--bg-color); }
      5% { background: alpha(var(--border-color-active), 0.4); }
      15% { background: alpha(var(--border-color-active), 0.6); }
      60% { background: alpha(var(--border-color-active), 0.9); }
      100% { background: var(--bg-color); }
    }

    '';
  };
}
