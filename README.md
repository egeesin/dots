## Welcome to my castle!
This repository contains personal curated configuration files of CLI/TUI apps you mostly know (nvim, tmux, newsbeuter, mutt, etc.) and the list of packages to be installed. You probably not gonna like exaggerated number of configs, you may not want all of them. So I suggest you not to use install.sh unless you know what's inside.

## Installation
`install.sh` is going to,
- Create link to **zshrc**, gemrc, gitconfig, gitignore\_global 
- Download & install packages from lists
- Create link to configurations `~/.dotfiles/config`
- (Optional) Install files located `~/.extra`
- Ask you to change default shell to **zsh**.

**Note:** Existing configs will be renamed after symlinking process (e.g. .tmux.conf -> .tmux.conf.old)

```sh
git clone https://github.com/egeesin/dotfiles ~/.dotfiles
cd ~/.dotfiles && ./install.sh
```

### Remote
```sh
# w/curl:
sh -c “`curl -fsSL https://raw.github.com/egeesin/dotfiles/master/remote-install.sh`”

# w/wget:
sh -c “`wget -O - --no-check-certificate https://raw.githubusercontent.com/egeesin/dotfiles/master/remote-install.sh`”
```

## Usage
```
dot <command>

Commands:
   help        This help message
   edit        Open dotfiles in editor
   reload      Reload shell configuration
   link        Relink configurations
   test        Run tests
   up          Update packages and pkg managers (npm, pip, macOS, brew, gem, pacman, pacaur)
   clean       Clean up caches (brew, npm, gem, rvm)
   defaults    Apply macOS system defaults
   dock        Apply macOS dock placements
   install     Install packages listed from the dotfiles/install (e.g. dot install npm)
```

## Credits
- [install.sh](https://github.com/egeesin/dotfiles/blob/archlinux/install.sh), [remote-install.sh](https://github.com/egeesin/dotfiles/blob/archlinux/install.sh), the dotfiles command, mackup, directory structure, etc. belongs to [webpro](https://github.com/webpro/dotfiles).
- Symlinking system from [olzraiti](https://github.com/olzraiti/dotfiles) 
- macOS defaults from [mathiasbynens](https://github.com/mathiasbynens/dotfiles) 
- i3, mpd and ncmpcpp configs from [mohabaks](https://github.com/mohabaks/dotfiles) 
	 
## Useful articles/links about dotfiles
- [dotfiles.github.io](https://dotfiles.github.io/)
- [Using Git and GitHub to Manage Your Dotfiles - Micheal Smalley](http://blog.smalleycreative.com/tutorials/using-git-and-github-to-manage-your-dotfiles/)
- [Getting started with dotfiles - webpro](https://medium.com/@webprolific/getting-started-with-dotfiles-43c3602fd789)
- [Managing your dotfiles - webpro](https://medium.com/@webprolific/managing-your-dotfiles-7d2725297304)
- [bradyholt/dotfiles](https://github.com/bradyholt/dotfiles)
- [holman/dotfiles](https://github.com/holman/dotfiles)
- [mohabaks/dotfiles](https://github.com/mohabaks/dotfiles)
