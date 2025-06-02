#!/bin/zsh
echo
echo "▓▒░ Installing bundles from official & user repos..."
# shellcheck source=../system/env
. "$DOT_DIR/system/env" # $currentos, $archbits etc.
# shellcheck source=../system/function
. "$DOT_DIR/system/function" # is_executable, ask, print_platform etc.
# shellcheck source=../system/path
. "$DOT_DIR/system/path"

#----------- Check Core Architecture
if [ ! "$archbits" = 64 ]; then
	echo "ERR: The system isn't 64-bit or undefined, skipping bundle installation." && exit
fi

# Uncomment multilib (to install Steam and Wine emulator) and archlinuxfr just in case
[[ -d $X_DIR ]] && sudo install -m 644 -o root -g root "$X_DIR/mbp11x/etc/pacman.conf" -t /etc

#----------- AUR helper

if ! is_executable yay; then
	echo
	echo "${WHT}AUR package manager missing, installing Yay...${NC}"
	git clone https://aur.archlinux.org/yay.git
	cd yay || exit
	makepkg -si
	cd - || exit
	rm -r yay/
fi

#--- Summon Super User
echo
sudo -v
while true; do sudo -n true; sleep 60; kill -0 "$$" || exit; done 2>/dev/null &
echo

# install_type=3
# install_this="${ess[@]}"
# install_this_aur="${ess2[@]}"

# 1 ... Minimal
# 3 ... Minimal + Essential
# 6 ... Minimal + Essential + Extra
# 10 .. Minimal + Essential + Extra + GUI
# 15 .. All (Minimal + Essential + Extra + GUI + Gaming)

#----------- Package Bundles

#--- Minimal
mini=(
wget
dosfstools
ntfs-3g
udiskie
udisks2
unrar
unzip
zip
gzip
arch-wiki-lite
gnupg
neofetch
acpi
alsa-firmware
alsa-lib
alsa-plugins
alsa-utils
ffmpeg
shntool
gst-libav
bc
lm_sensors
nnn
# stow
wireless_tools
)
mini2=(
hfsprogs
)

#--- Essentials
ess=(
zsh
# htop
ifuse
neovim
python-neovim
# nodejs
# npm
tmux
tmuxp
mpd
# transmission-cli
w3m
youtube-dl
pass
fzf
pulseaudio-alsa
pavucontrol
playerctl
mopidy
cowsay
fontforge
highlight
hwinfo
imagemagick
jq
leptonica
libcaca
libimobiledevice
lolcat
mediainfo
openvpn
perl-image-exiftool
# python2-pip
python-aiohttp
python-async-timeout
python-blinker
python-docopt
python-mock
python-multidict
python-pbr
python-requests
python-yarl
sshfs
)
ess2=(
starship
universal-ctags
jsctags-tern-git
gotop-bin
# neomutt
urlscan-git
# tmuxinator
tmux-bash-completion
vscode-langservers-extracted
yank
bcal
# console-solarized-git
# jekyll
# keybase-bin
)


#--- Extra CLI
ext=(
hub
calcurse
figlet
fortune-mod
# bsd-games
catfish
# cmatrix
# glances
# we-get-git
mps-youtube
ncmpcpp
# newsboat
ripgrep
socat
surfraw
task
# thefuck
tig
typespeed
# weechat
you-get
)
ext2=(
# rtv
# translate-shell
# stig-git
# '2048.c'
# asciinema-git
bash-pipes
bmon-git
# buku
cava
gitsome
# canto-curses
# curseradio-git
greed
imgp-git
# imgurbash2
# jrnl
mdp
megatools
# ninvaders
pacman4console
pass-import
# pockyt
python-natsort
python-urwidtrees-git
python3-kitchen
sc-im
sparklines-git
trash-cli-git
# vitetris
wego-git
)

#--- Graphical User Interface & Media
gui=(
xcb-util-cursor
xorg-server
xorg-xev
xorg-xinit
xorg-xprop
xautolock
# sxiv
urxvt-perls
rxvt-unicode-terminfo
arandr
lxappearance
thunar
thunar-media-tags-plugin
firefox
feh
nitrogen
conky
dunst
# xscreensaver
rofi
i3lock
i3status
mpv
qbittorrent-enhanced-qt5
streamlink
cairo
scrot
maim
krita
# gimp
inkscape
mixxx
pitivi
osdstudio
libreoffice-still
zathura
zathura-pdf-poppler
zathura-cb
poppler
scribus
obsidian
redshift
audacity
tigervnc
ffmpegthumbnailer
glfw-x11
# jre8-openjdk
libqalculate
raw-thumbnailer
remind
# sl

slop
sysstat
tk
tumbler
usbmuxd
)


gui2=(
i3-gaps
i3blocks-gaps-git
i3ipc-glib-git
i3lock-color-git
i3lock-fancy-git
xlunch-git
sublime-text-dev
# google-chrome-dev
ungoogled-chromium
chromium-extension-web-store
urxvt-fullscreen
urxvt-resize-font-git
urxvt-vtwheel
# buku_run-git
byzanz-git
menu-calc
aur/discord
# dropbox
emojione-color-font
# evolus-pencil-bin
gtk-theme-solarc-git
# gtk-youtube-viewer-git
keynav
ksuperkey
font-manager
# ttf-emojione-color
# ttf-inter-ui
# ttf-mac-fonts
# ttf-ms-fonts
# ttf-weather-icons
la-capitaine-icon-theme-git
lead-git
light
# mopidy-iris
# mopidy-local-images
# DEPRECATED mopidy-notifier-git
# mopidy-soundcloud
# mopidy-spotify
# mopidy-spotify-tunigo
pick-colour-picker
polybar-git
qt5-styleplugins
rofi-pass
rxvt-unicode-cvs-patched-wideglyphs
srandrd
# spicetify
# thunar-dropbox
thunar-thumbnailer-openraster
epub-thumbnailer-git
unclutter-xfixes-git
xcalib
xcursor-osx-elcap
# xscreensaver-aerial
)

#--- For macOS
gaming=(
steam
steam-native-runtime
)
gaming2=(
# assaultcube-reloaded
lutris
# mcedit
multimc-git
prism-launcher
# wine-gaming-nine
)

#----------- Choosing bundle

while true; do
	read -rp "Choose package bundle: [M]inimal [E]ssential E[x]tra [G]UI G[a]ming(All) - [C]ancel => " answer
    case $answer in
        [Mm]* ) install_type=1 && break;;
        [Ee]* ) install_type=3 && break;;
        [Xx]* ) install_type=6 && break;;
        [Gg]* ) install_type=10 && break;;
        [Aa]* ) install_type=15 && break;;
        [Cc]* ) echo "No package bundle chosen, installation skipped." && return 0;;
    esac
done


if [ $install_type = 1 ]; then
	get_pkg=("${mini[@]}")
	get_pkg_aur=("${mini2[@]}")
elif [ $install_type = 3 ]; then
	get_pkg=("${mini[@]} ${ess[@]}")
	get_pkg_aur=("${mini2[@]} ${ess2[@]}")
elif [ $install_type = 6 ]; then
	get_pkg=("${mini[@]} ${ess[@]} ${ext[@]}")
	get_pkg_aur=("${mini2[@]} ${ess2[@]} ${ext2[@]}")
elif [ $install_type = 10 ]; then
	get_pkg=("${mini[@]} ${ess[@]} ${ext[@]} ${gui[@]}")
	get_pkg_aur=("${mini2[@]} ${ess2[@]} ${ext2[@]} ${gui2[@]}")
elif [ $install_type = 15 ]; then
	get_pkg=("${mini[@]} ${ess[@]} ${ext[@]} ${gui[@]} ${gaming[@]}")
	get_pkg_aur=("${mini2[@]} ${ess2[@]} ${ext2[@]} ${gui2[@]} ${gaming2[@]}")
fi

#----------- Installation Loop

# sudo -v
# while true; do sudo -n true; sleep 60; kill -0 "$$" || exit; done 2>/dev/null &

pac_options="--downloadonly --noconfirm --noprogressbar --quiet --needed"
aur_options="-a --nocleanmenu --nodiffmenu --noeditmenu --noupgrademenu --noprovides --sudoloop"

# Sync mirrors first.
sudo pacman -Syu "$pac_options"
yay -Syu "$aur_options" "$pac_options"

for x in "${get_pkg[@]}"; do sudo pacman -S "$pac_options" --logfile "$X_DIR/pacman-log-$(date +%Y-%m-%d).txt" "$x"; done
for y in "${get_pkg_aur[@]}"; do yay -S "$pac_options" "$aur_options" "$y"; done

echo "█▓▒░░ Bundles from official & user repo -> Installed!"
