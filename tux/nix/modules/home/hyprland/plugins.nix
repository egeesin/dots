{
  inputs,
  # host,
  config,
  # lib,
  pkgs,
  # pkgs-unstable,
  ...
}: let
  # pluginsAsNixpkgs = pkgs.hyprlandPlugins;
  pluginsAsFlake = inputs.hyprland-plugins.packages.${pkgs.system}; # From flake
in {
  wayland.windowManager.hyprland = {
    plugins =
      # https://github.com/hyprwm/hyprland-plugins#plugin-list
      # https://github.com/hyprland-community/awesome-hyprland
    # (with pluginsAsNixpkgs; [
    # ]) ++ (with pluginsAsFlake; [
    (with pluginsAsFlake; [ # Had to move all plugins from nixpkgs to flake source as hyprland (as flake) complains about mismatch versions of plugins
      hyprbars # adds window bar
      csgo-vulkan-fix # force apps to a fake resolution without them realizing it.
      # hyprwinwrap # Desktop environment background (wayland equivalent of xwinwrap, alternative to mpvwallpaper)
      xtra-dispatchers # adds some additional dispatchers
      # hyprscrolling # adds scrolling layout like niri (WIP) https://github.com/dawsers/hyprscroller # Can't build this atm for some reason
    ]) ++ [
      # inputs.hyprkool.packages.${pkgs.system}.default # Replicates the feel of KDE activities/desktop grid layout https://github.com/thrombe/hyprkool#example-configs
      inputs.hypr-dynamic-cursors.packages.${pkgs.system}.hypr-dynamic-cursors
      # inputs.Hyprspace.packages.${pkgs.system}.Hyprspace # macOS/KDE like mission control thingy https://github.com/KZDKM/Hyprspace#configuration
    ];
    settings = {
      plugin = {
        # hyprscrolling = {
        #   "fullscreen_on_one_column" = false; 
        # };
        dynamic-cursors = {
          # https://github.com/VirtCode/hypr-dynamic-cursors#configuration
          # mode = "rotate";
          # mode = "stretch";
          mode = "tilt";
          shake = {
            threshold = 10; # default 6, might be an issue for some games like minecraft
            enabled = true;
            nearest = true;
            effects = true;
          };
          # Should be good for SVG-based cursor themes and higher-res displays
          # https://github.com/VirtCode/hypr-dynamic-cursors#hyprcursor
          # hyprcursor = {
          #   nearest = true;
          #   enabled = true;
          #   resolution = -1;
          #   fallback = "clientside";
          # };
          shaperule = [
            "text, rotate:offset: 90" # apply a 90deg offset in rotate mod to the text shape
            "grab, stretch, stretch:limit:2000" # use stretch mode when grabbing, and set limit low
            # "clientside, none" # don't show any effects on clientside cursors
          ]; 
        };
        hyprbars = {
          bar_height = 20;
          bar_blur = true;
          bar_color = "rgb(${config.lib.stylix.colors.base00})";
          "col.text" = "rgb(${config.lib.stylix.colors.base03})";
          bar_padding = 8;
          bar_button_padding = 8;
          bar_title_enabled = true;
          bar_text_align = "left";
          bar_part_of_window = true;
          bar_precedence_over_border = true;
          icon_on_hover = true;
          # bar_text_font = "Jetbrains Mono";
          hyprbars-button = [
            "rgb(${config.lib.stylix.colors.base00}), 22, 󰖭, hyprctl dispatch killactive, rgb(${config.lib.stylix.colors.base03})"
            "rgb(${config.lib.stylix.colors.base00}), 18, 󰕔, hyprctl dispatch togglefloating, rgb(${config.lib.stylix.colors.base03})"
            "rgb(${config.lib.stylix.colors.base00}), 18, 󰘖, hyprctl dispatch fullscreen, rgb(${config.lib.stylix.colors.base03})"
          ];
        };
        "csgo-vulkan-fix" = {
          # https://github.com/hyprwm/hyprland-plugins/tree/main/csgo-vulkan-fix
          res_w = 1920;
          res_h = 1080;
          class = "cs2"; # not a regex! has to match initial_class exactly
          fix_mouse = true; # whether to fix the mouse position. a select few apps might be wonky with this.
        }; 
      };
      # https://github.com/mageowl/nix-config/blob/15b0a97759f82dfdee4dc2b74a209a171f6e38fa/modules/home/programs/hyprland/waycorner.nix#L10
      # waycorner = {
      #   enable = true;
      #   bottomRight = {
      #     enable = true;
      #     onEnter = ["wlogout"];
      #     # onEnter = ["systemctl" "sleep"];
      #   };
      #   bottomLeft = {
      #     enable = true;
      #     onEnter = [ startMenu ];
      #   };
      #   topRight = {
      #     enable = true;
      #     onEnter = ["swaync-client" "-t" "-sw"];
      #   };
      # };
    };
  };
  
}
