{ host, ... }:
let
  inherit (import ../../hosts/${host}/variables.nix) gitUsername gitEmail;
in
{
  programs.git = {
    enable = true;
    userName = "${gitUsername}";
    userEmail = "${gitEmail}";
    extraConfig = {
      # core.editor = "hx";
      init.defaultBranch = "main";
    };
    ignores = [

      "*~"

      # Source: jcherqui/dotfiles

      # Compiled source
      "*.class"
      "*.dll"
      "*.exe"
      "*.o"
      "*.so"

      # Packages
      # it's better to unpack these files and commit the raw source
      # git has its own built in compression methods
      "*.7z"
      "*.dmg"
      "*.gz"
      "*.iso"
      "*.jar"
      "*.rar"
      "*.tar"
      "*.zip"

      # Logs and databases #
      "*.log"
      #*.sql
      "*.sqlite"

      # OS generated files #
      ".DS_Store"
      ".DS_Store?"
      "._*"
      ".Spotlight-V100"
      ".Trashes"
      "ehthumbs.db"
      "Thumbs.db"

      # Sublime text #
      "*.sublime-project"
      "*.sublime-workspace"

      # Node.js "
      "node_modules"
      "bower_components"
      "npm-debug.log"


      # Vagrant #
      ".vagrant/"

      # VIM #
      "*.swp"

      "*.bak"

      # Other #
      ".direnv/"
      ".go/"

    ];
  };
}
