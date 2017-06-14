# Install Homebrew

command -v brew > /dev/null 2&>1 || ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
brew doctor
brew tap homebrew/versions
brew tap homebrew/dupes
brew update
brew upgrade

# Install packages

apps=(
coreutils
findutils
gnu-sed
grep
ansiweather
asciinema
atool
bats
boost
buku
cairo
calcurse
cmatrix
cowsay
dark-mode
dockutil
fasd
ffmpeg
fftw
figlet
fontconfig
fontforge
fortune
freetype
fzf
git
git-extras
passy/givegif/givegif
gnupg2
go
hget
htop-osx
httpie
hub
imagemagick
imessage-ruby
jrnl
leptonica
lolcat
mackup
mas
mdp
mpd
mplayer
mps-youtube
mpv
ncurses
ncmpcpp
neofetch
neomutt/homebrew-neomutt/neomutt
neovim/neovim/neovim
newsbeuter
ninvaders
openssl
pango
pass
poppler
psgrep
python
ranger
reattach-to-user-namespace
remind
ripgrep
rtv
ruby
shellcheck
sl
spark
ssh-copy-id
surfraw
terminal-notifier
tesseract
thefuck
tldr
tmux
translate-shell
transmission
tree
tty-clock
typespeed
urlview
vitetris
w3m
wget
yank
youtube-dl
zplug
zsh
zsh-completions
)

brew install "${apps[@]}"

# Remove outdated versions from the cellar.
brew cleanup

# Symlink Zplug
ln -s "$( brew --prefix )"/opt/zplug ~/.zplug
