-- vim:ft=lua
local wezterm = require 'wezterm'
local config = {}

-- config.default_prog = { '/usr/local/bin/fish', '-l' }
-- config.default_prog = { '/usr/local/bin/zsh', '-l' }
config.default_prog = { "C:\\Users\\ege_e\\scoop\\apps\\pwsh\\current\\pwsh.exe" }

config.font = wezterm.font_with_fallback {
  'Iosevka Aegean Mono',
  'CommitMono Nerd Font'
}

config.font_size = 10

function get_appearance()
  if wezterm.gui then
    return wezterm.gui.get_appearance()
  end
  return 'Dark'
end

function scheme_for_appearance(appearance)
  if appearance:find 'Dark' then
    -- io.popen("sed -i '' 's/theme = \"flexoki_light\"/theme = \"flexoki_dark\"/g' C:\\Users\\ege_e\\AppData\\Roaming\\helix\\config.toml"):close()
    -- io.popen("pkill -USR1 hx"):close()
    return 'flexoki-dark'
  else
    -- io.popen("sed -i '' 's/theme = \"flexoki_dark\"/theme = \"flexoki_light\"/g' C:\\Users\\ege_e\\AppData\\Roaming\\helix\\config.toml"):close()
    -- io.popen("pkill -USR1 hx"):close()
    return 'flexoki-dark'
    -- return 'flexoki-light'
  end
end

config.color_scheme = scheme_for_appearance(get_appearance())
-- config.color_scheme = 'tokyo-night'

-- config.hide_tab_bar_if_only_one_tab = true

config.window_padding = {
  left = 12,
  right = 12,
  top = 22,
  bottom = 22,
}
config.window_frame = {
  -- The font used in the tab bar.
  -- Roboto Bold is the default; this font is bundled
  -- with wezterm.
  -- Whatever font is selected here, it will have the
  -- main font setting appended to it to pick up any
  -- fallback fonts you may have used there.
  font = wezterm.font { family = 'Iosevka Aegean Quasi', weight = 'Bold' },

  -- The size of the font in the tab bar.
  -- Default to 10.0 on Windows but 12.0 on other systems
  font_size = 10.0,

  -- The overall background color of the tab bar when
  -- the window is focused
  active_titlebar_bg = '#333333',

  -- The overall background color of the tab bar when
  -- the window is not focused
  inactive_titlebar_bg = '#333333',
}

config.launch_menu = {
  {
    args = { 'top' },
  },
  {
    label = 'PowerShell 7',
    args = { "C:\\Users\\ege_e\\scoop\\apps\\pwsh\\current\\pwsh.exe" }
  },
  {
    label = 'LunarVim that listens to Godot',
    args = { 'lvim --listen 127.0.0.1:6004' },
  },
  {
    label = 'Command Prompt',
    args = { 'cmd.exe' },
  }
  -- {
  --   label = 'Bash',
  --   args = { 'bash', '-l' },
  --   cwd = "/some/path"
  --   set_environment_variables = { FOO = "bar" },
  -- }
}

config.colors = {
  tab_bar = {
    -- The color of the inactive tab bar edge/divider
    inactive_tab_edge = '#575757',
  },
}

return config
