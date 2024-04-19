echo
echo "▓▒░ Installing packages from brew..."
# shellcheck source=../system/env
. "$DOT_DIR/system/env" # $currentos, $archbits etc.
# shellcheck source=../system/function
. "$DOT_DIR/system/function" # is_available, $currentos, ask, print_platform etc.
# shellcheck source=../system/path
. "$DOT_DIR/system/path"

DOT_CACHE="$DOT_DIR/.cache.sh"

if ! is_executable brew; then ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"; fi
brew doctor
git -C "/usr/local/Homebrew/Library/Taps/homebrew/homebrew-core" fetch --unshallow
brew update
brew upgrade
BREW_PREFIX=$(brew --prefix)

brew bundle --file="$DOT_DIR/setup/Brewfile"
BREW_PREFIX_COREUTILS=$(brew --prefix coreutils)
export BREW_PREFIX_COREUTILS
ln -s "${BREW_PREFIX}/bin/gsha256sum" "${BREW_PREFIX}/bin/sha256sum" >/dev/null 2>&1
set_config "BREW_PREFIX_COREUTILS" "$BREW_PREFIX_COREUTILS" "$DOT_CACHE" >/dev/null 2>&1

# Remove outdated versions from the cellar.
brew cleanup
echo
echo "█▓▒░░ Bundles from Homebrew -> Installed!"
