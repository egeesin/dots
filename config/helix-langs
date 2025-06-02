# vim:ft=toml
use-grammars = { only = [ "awk", "bash", "c", "c-sharp", "diff", "dockerfile", "env", "elixir", "fish", "gdscript",
"git-attributes", "git-commit", "git-config", "git-ignore", "git-rebase", "glsl", "go", "gleam", "godot-resource", "html",
"java", "javascript", "jinja", "jq", "json", "json5", "jsonc", "jsx", "ini", "liquid", "log",
"lua", "make", "markdoc", "markdown", "markdown.inline", "mojo", "nginx", "nix", "nunjucks", "nu", "passwd",
"pem", "php", "php-only", "pkgbuild", "pkl", "kdl", "po", "powershell", "python", "regex",
"ruby", "rust", "scss", "svelte", "swift", "todotxt", "toml", "typescript", "twig", "vue",
"wgsl", "webc", "xml", "yaml", "zig"] }

# https://docs.helix-editor.com/guides/adding_languages.html
# https://github.com/helix-editor/helix/wiki/Language-Server-Configurations#gdscript

[language-server.scls]
# cargo install --git https://github.com/estin/simple-completion-language-server.git#
command = "simple-completion-language-server"

[language-server.scls.config]
max_completion_items = 100           # set max completion results len for each group: words, snippets, unicode-input
feature_words = true                 # enable completion by word
feature_snippets = true              # enable snippets
snippets_first = true                # completions will return before snippets by default
snippets_inline_by_word_tail = false # suggest snippets by WORD tail, for example text `xsq|` become `x^2|` when snippet `sq` has body `^2`
feature_unicode_input = false        # enable "unicode input"
feature_paths = false                # enable path completion
feature_citations = false            # enable citation completion (only on `citation` feature enabled)

[language-server.scls.environment]
RUST_LOG = "info,simple-completion-language-server=info"
LOG_FILE = "/tmp/completion.log"

[[language]]
name = "stub"
scope = "text.stub"
file-types = []
shebangs = []
roots = []
auto-format = false
language-servers = [ "scls" ]

[language-server.shopify-theme-check]
command = "shopify"
args = ["theme", "language-server"]

# pnpm install -g @shopify/cli@latest
[[language]]
name = "liquid"
scope = "source.liquid"
file-types = ["liquid"]
injection-regex = "^liquid$"
indent = { tab-width = 2, unit = "\t"}
language-servers = ["scls", "shopify-theme-check"]
block-comment-tokens = { start = "{%- comment -%}", end = "{%- endcomment -%}" }

[[grammar]]
name = "liquid"
source = { git = "https://github.com/hankthetank27/tree-sitter-liquid", rev = "d269f4d52cd08f6cbc6636ee23cc30a9f6c32e42"}
# In order to add syntax highlighting you must follow this:
# https://docs.helix-editor.com/guides/adding_languages.html#queries

[language-server.godot]
command = "ncat" # or nc
args = [ "127.0.0.1", "6005"]
language-id = "gdscript"

[[language]]
name = "gdscript"
language-servers = ["godot"]


# [[language]]
# name = "html"
# file-types = ["html", "xml"]
# auto-format = false

# [[language]]
# name = "css"
# auto-format = false

# [[language]]
# name = "js"
# indent = { tab-width = 2, unit = "  " }
# auto-format = false

[[language]]
name = "html"
language-servers = [ "scls", "vscode-html-language-server" ]

[[language]]
name = "css"
language-servers = [ "scls", "vscode-css-language-server" ]

[[language]]
name = "javascript"
language-servers = [ "scls", "typescript-language-server" ]

[[language]]
name = "json"
language-servers = [ "scls", "vscode-json-language-server" ]

[[language-server.vscode-json-language-server.config.json.schemas]]
fileMatch = [ "package.json" ]
url = "https://json.schemastore.org/package.json"

[[language]]
name = "toml"
language-servers = [ "scls", "taplo" ]

[[language]]
name = "rust"
language-servers = [ "scls", "rust-analyzer" ]

[[language]]
name = "git-commit"
language-servers = [ "scls" ]
