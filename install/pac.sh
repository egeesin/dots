DOTFILES_DIR=$HOME/.dotfiles

for x in $(cat "$DOTFILES_DIR/install/pkglist/pac"); do sudo pacman -S --noconfirm $x; done
for y in $(cat "$DOTFILES_DIR/install/pkglist/aur"); do pacaur -a -S --noconfirm --noedit $y; done
