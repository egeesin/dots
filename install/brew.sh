export PATH="/usr/local/sbin:/usr/local/bin:$PATH"

if ! is-executable brew; then ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"; fi
brew doctor
brew update
brew upgrade
brew bundle --file="$DOT_DIR/install/pkglist/Brewfile"
export BREW_PREFIX_COREUTILS=`brew --prefix coreutils`
set-config "BREW_PREFIX_COREUTILS" "$BREW_PREFIX_COREUTILS" "$DOT_CACHE"
# Just in case doesn't work,
#. "$DOT_DIR/etc/brew.sh"
#. "$DOT_DIR/etc/cask.sh"
