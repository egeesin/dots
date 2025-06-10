{ host, pkgs, ... }:
let
  inherit (import ../../hosts/${host}/variables.nix) gitUsername gitEmail;
in
{
  home.packages = with pkgs; [
    # git-credential-manager # Secure, cross-platform Git credential storage with authentication to GitHub, Azure Repos, and other popular Git hosting services
    difftastic # a structural diff that understands syntax
    #jujutsu # insecure
    yaziPlugins.lazygit # Lazygit plugin for yazi
    git-credential-manager
  ];
  programs.lazygit.enable = true; # Simple terminal UI for git commands
  programs.git = {
    enable = true;
    lfs.enable = true;
    userName = "${gitUsername}";
    userEmail = "${gitEmail}";
    delta.enable = true; # Git diff with better highlight, installed it as optional dep for batdiff
    # git-credential-oauth.enable = true;

    extraConfig = {
      # core.editor = "hx";
      init.defaultBranch = "main";
      push.autoSetupRemote = true;
      credential = {
        credentialStore = "cache";
        helper= "manager";

        # helper = "${pkgs.git.override { withLibsecret = true; }}/bin/git-credential-libsecret";
        # 
        # credentialStore = "secretservice";
        # 
        # helper = if pkgs.stdenv.isLinux then "libsecret" else "osxkeychain"; # from: https://github.com/arulagrawal/nix/blob/9421d79aaab884e1164ae472f57e65ade8f3cfec/home/git.nix#L43
        # 
        # helper = "${pkgs.git-credential-manager}/bin/git-credential-manager";
        # credentialStore = "gpg";
      };
    };
    # ignores = import ./gitignore.nix;
    ignores = [
      # Source: jcherqui/dotfiles
      "*~"

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
