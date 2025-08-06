# vim:ft=toml
# theme = "flexoki_dark"
theme = "base16_default"
# theme = "base16_transparent"
# theme = "naysayer"
# theme = "merionette"
# theme = "monokai_pro_machine"
# theme = "heisenberg"

[editor]
line-number = "relative" 
true-color = true
# shell = ["zsh", "-c"]
# shell = ["cmd", "/C"]

[editor.cursor-shape]
insert = "bar"
normal = "block"
select = "underline"

# [editor.file-picker]
# hidden = false

[editor.statusline]
left = ["mode", "spinner", "version-control", "file-name", "read-only-indicator", "file-modification-indicator"]
right = ["diagnostics", "selections", "file-encoding", "file-line-ending", "file-type", "position", "position-percentage" ]

[editor.whitespace.render]
space = "all"
nbsp = "all"
nnbsp = "all"
newline = "all"

[editor.whitespace.characters]
newline = "ꜚ"

[editor.indent-guides]
render = true
character = "╎" # Some characters that work well: "▏", "┆", "┊", "⸽"
skip-levels = 1

[keys.insert]
"C-[" = "normal_mode"

[keys.select]
"C-[" = "normal_mode"

# [keys.normal.space.space]
# f = "file_explorer"
