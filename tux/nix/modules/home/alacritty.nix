{
  lib,
  # host,
  ...
}: let
  # inherit
  #   (import ../../../hosts/${host}/variables.nix)
  #   ;
in {
  programs.alacritty = {
    enable = true;
    # settings = lib.mkDefault {
    #   bell = {
    #     animation = "EaseOutExpo";
    #     duration = 0;
    #   };
    #   colors = {
    #     draw_bold_text_with_bright_colors = false;
    #   };
    #   cursor = {
    #     style = "Block";
    #     unfocused_hollow = true;
    #   };
    #   debug = {
    #     render_timer = false;
    #   };
    #   env = {
    #     TERM = "xterm-256color";
    #   };
    #   font = {
    #     glyph_offset = {
    #       x = 0;
    #       y = 3;
    #     };
    #     # normal = {
    #     #   family = "Commit Mono";
    #     # };
    #     # offset = {
    #     #   x = 0;
    #     #   y = 6;
    #     # };
    #     # size = 12;
    #     # size = 14;
    #   };
    #   general = {
    #     # import = [ "~/.dots/config/alacritty-color" ];
    #     live_config_reload = true;
    #     # working_directory = "C:\\Users\\ege_e\\";
    #   };
    #   hints = {
    #     enabled = [
    #       {
    #         binding = {
    #           key = "U";
    #           mods = "Control|Shift";
    #         };
    #         command = "open";
    #         hyperlinks = true;
    #         mouse = {
    #           enabled = true;
    #           mods = "None";
    #         };
    #         post_processing = true;
    #         regex = "(ipfs:|ipns:|magnet:|mailto:|gemini:|gopher:|https:|http:|news:|file:|git:|ssh:|ftp:)[^";
    #       }
    #     ];
    #   };
    #   keyboard = {
    #     bindings = [
    #       {
    #         action = "Paste";
    #         key = "Paste";
    #       }
    #       {
    #         action = "Copy";
    #         key = "Copy";
    #       }
    #       {
    #         action = "ClearLogNotice";
    #         key = "L";
    #         mods = "Control";
    #       }
    #       {
    #         chars = "";
    #         key = "L";
    #         mode = "~Vi";
    #         mods = "Control";
    #       }
    #       {
    #         action = "ScrollPageUp";
    #         key = "PageUp";
    #         mode = "~Alt";
    #         mods = "Shift";
    #       }
    #       {
    #         action = "ScrollPageDown";
    #         key = "PageDown";
    #         mode = "~Alt";
    #         mods = "Shift";
    #       }
    #       {
    #         action = "ScrollToTop";
    #         key = "Home";
    #         mode = "~Alt";
    #         mods = "Shift";
    #       }
    #       {
    #         action = "ScrollToBottom";
    #         key = "End";
    #         mode = "~Alt";
    #         mods = "Shift";
    #       }
    #       {
    #         action = "ScrollToBottom";
    #         key = "Space";
    #         mode = "Vi";
    #         mods = "Shift|Control";
    #       }
    #       {
    #         action = "ToggleViMode";
    #         key = "Space";
    #         mods = "Shift|Control";
    #       }
    #       {
    #         action = "ClearSelection";
    #         key = "Escape";
    #         mode = "Vi";
    #       }
    #       {
    #         action = "ScrollToBottom";
    #         key = "I";
    #         mode = "Vi";
    #       }
    #       {
    #         action = "ToggleViMode";
    #         key = "I";
    #         mode = "Vi";
    #       }
    #       {
    #         action = "ToggleViMode";
    #         key = "C";
    #         mode = "Vi";
    #         mods = "Control";
    #       }
    #       {
    #         action = "ScrollLineUp";
    #         key = "Y";
    #         mode = "Vi";
    #         mods = "Control";
    #       }
    #       {
    #         action = "ScrollLineDown";
    #         key = "E";
    #         mode = "Vi";
    #         mods = "Control";
    #       }
    #       {
    #         action = "ScrollToTop";
    #         key = "G";
    #         mode = "Vi";
    #       }
    #       {
    #         action = "ScrollToBottom";
    #         key = "G";
    #         mode = "Vi";
    #         mods = "Shift";
    #       }
    #       {
    #         action = "ScrollPageUp";
    #         key = "B";
    #         mode = "Vi";
    #         mods = "Control";
    #       }
    #       {
    #         action = "ScrollPageDown";
    #         key = "F";
    #         mode = "Vi";
    #         mods = "Control";
    #       }
    #       {
    #         action = "ScrollHalfPageUp";
    #         key = "U";
    #         mode = "Vi";
    #         mods = "Control";
    #       }
    #       {
    #         action = "ScrollHalfPageDown";
    #         key = "D";
    #         mode = "Vi";
    #         mods = "Control";
    #       }
    #       {
    #         action = "Copy";
    #         key = "Y";
    #         mode = "Vi";
    #       }
    #       {
    #         action = "ClearSelection";
    #         key = "Y";
    #         mode = "Vi";
    #       }
    #       {
    #         action = "ClearSelection";
    #         key = "Copy";
    #         mode = "Vi";
    #       }
    #       {
    #         action = "ToggleNormalSelection";
    #         key = "V";
    #         mode = "Vi";
    #       }
    #       {
    #         action = "ToggleLineSelection";
    #         key = "V";
    #         mode = "Vi";
    #         mods = "Shift";
    #       }
    #       {
    #         action = "ToggleBlockSelection";
    #         key = "V";
    #         mode = "Vi";
    #         mods = "Control";
    #       }
    #       {
    #         action = "ToggleSemanticSelection";
    #         key = "V";
    #         mode = "Vi";
    #         mods = "Alt";
    #       }
    #       {
    #         action = "Open";
    #         key = "Return";
    #         mode = "Vi";
    #       }
    #       {
    #         action = "Up";
    #         key = "K";
    #         mode = "Vi";
    #       }
    #       {
    #         action = "Down";
    #         key = "J";
    #         mode = "Vi";
    #       }
    #       {
    #         action = "Left";
    #         key = "H";
    #         mode = "Vi";
    #       }
    #       {
    #         action = "Right";
    #         key = "L";
    #         mode = "Vi";
    #       }
    #       {
    #         action = "Up";
    #         key = "Up";
    #         mode = "Vi";
    #       }
    #       {
    #         action = "Down";
    #         key = "Down";
    #         mode = "Vi";
    #       }
    #       {
    #         action = "Left";
    #         key = "Left";
    #         mode = "Vi";
    #       }
    #       {
    #         action = "Right";
    #         key = "Right";
    #         mode = "Vi";
    #       }
    #       {
    #         action = "First";
    #         key = "Key0";
    #         mode = "Vi";
    #       }
    #       {
    #         action = "Last";
    #         key = "Key4";
    #         mode = "Vi";
    #         mods = "Shift";
    #       }
    #       {
    #         action = "FirstOccupied";
    #         key = "Key6";
    #         mode = "Vi";
    #         mods = "Shift";
    #       }
    #       {
    #         action = "High";
    #         key = "H";
    #         mode = "Vi";
    #         mods = "Shift";
    #       }
    #       {
    #         action = "Middle";
    #         key = "M";
    #         mode = "Vi";
    #         mods = "Shift";
    #       }
    #       {
    #         action = "Low";
    #         key = "L";
    #         mode = "Vi";
    #         mods = "Shift";
    #       }
    #       {
    #         action = "SemanticLeft";
    #         key = "B";
    #         mode = "Vi";
    #       }
    #       {
    #         action = "SemanticRight";
    #         key = "W";
    #         mode = "Vi";
    #       }
    #       {
    #         action = "SemanticRightEnd";
    #         key = "E";
    #         mode = "Vi";
    #       }
    #       {
    #         action = "WordLeft";
    #         key = "B";
    #         mode = "Vi";
    #         mods = "Shift";
    #       }
    #       {
    #         action = "WordRight";
    #         key = "W";
    #         mode = "Vi";
    #         mods = "Shift";
    #       }
    #       {
    #         action = "WordRightEnd";
    #         key = "E";
    #         mode = "Vi";
    #         mods = "Shift";
    #       }
    #       {
    #         action = "Bracket";
    #         key = "Key5";
    #         mode = "Vi";
    #         mods = "Shift";
    #       }
    #       {
    #         action = "SearchForward";
    #         key = "Slash";
    #         mode = "Vi";
    #       }
    #       {
    #         action = "SearchBackward";
    #         key = "Slash";
    #         mode = "Vi";
    #         mods = "Shift";
    #       }
    #       {
    #         action = "SearchNext";
    #         key = "N";
    #         mode = "Vi";
    #       }
    #       {
    #         action = "SearchPrevious";
    #         key = "N";
    #         mode = "Vi";
    #         mods = "Shift";
    #       }
    #       {
    #         chars = "";
    #         key = "K";
    #         mode = "~Vi";
    #         mods = "Command";
    #       }
    #       {
    #         action = "ResetFontSize";
    #         key = "Key0";
    #         mods = "Command";
    #       }
    #       {
    #         action = "IncreaseFontSize";
    #         key = "Equals";
    #         mods = "Command";
    #       }
    #       {
    #         action = "IncreaseFontSize";
    #         key = "Plus";
    #         mods = "Command";
    #       }
    #       {
    #         action = "IncreaseFontSize";
    #         key = "NumpadAdd";
    #         mods = "Command";
    #       }
    #       {
    #         action = "DecreaseFontSize";
    #         key = "Minus";
    #         mods = "Command";
    #       }
    #       {
    #         action = "DecreaseFontSize";
    #         key = "NumpadSubtract";
    #         mods = "Command";
    #       }
    #       {
    #         action = "ClearHistory";
    #         key = "K";
    #         mods = "Command";
    #       }
    #       {
    #         action = "Paste";
    #         key = "V";
    #         mods = "Command";
    #       }
    #       {
    #         action = "Copy";
    #         key = "C";
    #         mods = "Command";
    #       }
    #       {
    #         action = "ClearSelection";
    #         key = "C";
    #         mode = "Vi";
    #         mods = "Command";
    #       }
    #       {
    #         action = "Hide";
    #         key = "H";
    #         mods = "Command";
    #       }
    #       {
    #         action = "Minimize";
    #         key = "M";
    #         mods = "Command";
    #       }
    #       {
    #         action = "Quit";
    #         key = "Q";
    #         mods = "Command";
    #       }
    #       {
    #         action = "Quit";
    #         key = "W";
    #         mods = "Command";
    #       }
    #       {
    #         action = "SpawnNewInstance";
    #         key = "N";
    #         mods = "Command";
    #       }
    #       {
    #         action = "ToggleFullscreen";
    #         key = "F";
    #         mods = "Command|Control";
    #       }
    #       {
    #         action = "SearchForward";
    #         key = "F";
    #         mods = "Command";
    #       }
    #       {
    #         action = "SearchBackward";
    #         key = "B";
    #         mods = "Command";
    #       }
    #     ];
    #   };
    #   mouse = {
    #     bindings = [
    #       {
    #         action = "PasteSelection";
    #         mouse = "Middle";
    #       }
    #     ];
    #     hide_when_typing = false;
    #   };
    #   scrolling = {
    #     history = 10000;
    #     multiplier = 3;
    #   };
    #   selection = {
    #     save_to_clipboard = true;
    #     semantic_escape_chars = ",│`|:\"' ()[]{}<>";
    #   };
    #   # terminal = {
    #     # shell = {
    #       # program = "pwsh";
    #     # };
    #   # };
    #   window = {
    #     decorations = "transparent";
    #     dimensions = {
    #       columns = 80;
    #       lines = 24;
    #     };
    #     dynamic_padding = true;
    #     dynamic_title = true;
    #     opacity = 1;
    #     padding = {
    #       x = 12;
    #       y = 22;
    #     };
    #     startup_mode = "Windowed";
    #   };
    # };
  };
}
