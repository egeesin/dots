{ ... }: {
  programs.helix = { # Post-modern modal text editor
    enable = true;
    defaultEditor = true;
    settings = {
      editor = {
        cursor-shape = {
          insert = "bar";
          normal = "block";
          select = "underline";
        };
        indent-guides = {
          character = "╎";
          render = true;
          skip-levels = 1;
        };
        line-number = "relative";
        statusline = {
          left = [
            "mode"
            "spinner"
            "version-control"
            "file-name"
            "read-only-indicator"
            "file-modification-indicator"
          ];
          right = [
            "diagnostics"
            "selections"
            "file-encoding"
            "file-line-ending"
            "file-type"
            "position"
            "position-percentage"
          ];
        };
        true-color = true;
        whitespace = {
          characters = { newline = "ꜚ"; };
          render = {
            nbsp = "all";
            newline = "all";
            nnbsp = "all";
            space = "all";
          };
        };
      };
      keys = {
        insert = { "C-[" = "normal_mode"; };
        select = { "C-[" = "normal_mode"; };
      };
      # theme = "base16_default"; # Disabling this so Stylix won't conflict.
    };
    languages = {
      grammar = [{
        name = "liquid";
        source = {
          git = "https://github.com/hankthetank27/tree-sitter-liquid";
          rev = "d269f4d52cd08f6cbc6636ee23cc30a9f6c32e42";
        };
      }];
      language = [
        {
          auto-format = false;
          file-types = [ ];
          language-servers = [ "scls" ];
          name = "stub";
          roots = [ ];
          scope = "text.stub";
          shebangs = [ ];
        }
        {
          block-comment-tokens = {
            end = "{%- endcomment -%}";
            start = "{%- comment -%}";
          };
          file-types = [ "liquid" ];
          indent = {
            tab-width = 2;
            unit = "	";
          };
          injection-regex = "^liquid$";
          language-servers = [ "scls" "shopify-theme-check" ];
          name = "liquid";
          scope = "source.liquid";
        }
        {
          language-servers = [ "godot" ];
          name = "gdscript";
        }
        {
          language-servers = [ "scls" "vscode-html-language-server" ];
          name = "html";
        }
        {
          language-servers = [ "scls" "vscode-css-language-server" ];
          name = "css";
        }
        {
          language-servers = [ "scls" "typescript-language-server" ];
          name = "javascript";
        }
        {
          language-servers = [ "scls" "vscode-json-language-server" ];
          name = "json";
        }
        {
          language-servers = [ "scls" "taplo" ];
          name = "toml";
        }
        {
          language-servers = [ "scls" "rust-analyzer" ];
          name = "rust";
        }
        {
          language-servers = [ "scls" ];
          name = "git-commit";
        }
      ];
      language-server = {
        nixd = {
          command = "nixd";
          formatting = {
            command = ["alejandra"]; 
          };
          # Make sure FLAKE environment variable exists
          # nixpkgs.expr = "import (builtins.getFlake \"/etc/nixos\").inputs.nixpkgs { }";
          # options.nixos.expr = "(builtins.getFlake \"/etc/nixos\").nixosConfigurations.<HOSTNAME>.options";
          nixpkgs.expr = "import (builtins.getFlake \"$FLAKE\").inputs.nixpkgs { }";
          options.nixos.expr = "(builtins.getFlake \"$FLAKE\").nixosConfigurations.nvidia.options";
        };
        godot = {
          args = [ "127.0.0.1" "6005" ];
          command = "ncat";
          language-id = "gdscript";
        };
        scls = {
          command = "simple-completion-language-server";
          config = {
            feature_citations = false;
            feature_paths = false;
            feature_snippets = true;
            feature_unicode_input = false;
            feature_words = true;
            max_completion_items = 100;
            snippets_first = true;
            snippets_inline_by_word_tail = false;
          };
          environment = {
            LOG_FILE = "/tmp/completion.log";
            RUST_LOG = "info,simple-completion-language-server=info";
          };
        };
        shopify-theme-check = {
          args = [ "theme" "language-server" ];
          command = "shopify";
        };
        vscode-json-language-server = {
          config = {
            json = {
              schemas = [{
                fileMatch = [ "package.json" ];
                url = "https://json.schemastore.org/package.json";
              }];
            };
          };
        };
      };
      use-grammars = {
        only = [
          "awk"
          "bash"
          "c"
          "c-sharp"
          "diff"
          "dockerfile"
          "env"
          "elixir"
          "fish"
          "gdscript"
          "git-attributes"
          "git-commit"
          "git-config"
          "git-ignore"
          "git-rebase"
          "glsl"
          "go"
          "gleam"
          "godot-resource"
          "html"
          "java"
          "javascript"
          "jinja"
          "jq"
          "json"
          "json5"
          "jsonc"
          "jsx"
          "ini"
          "liquid"
          "log"
          "lua"
          "make"
          "markdoc"
          "markdown"
          "markdown.inline"
          "mojo"
          "nginx"
          "nix"
          "nunjucks"
          "nu"
          "passwd"
          "pem"
          "php"
          "php-only"
          "pkgbuild"
          "pkl"
          "kdl"
          "po"
          "powershell"
          "python"
          "regex"
          "ruby"
          "rust"
          "scss"
          "svelte"
          "swift"
          "todotxt"
          "toml"
          "typescript"
          "twig"
          "vue"
          "wgsl"
          "webc"
          "xml"
          "yaml"
          "zig"
        ];
      };
    };     
  };
}
