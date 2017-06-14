DOTFILES_DIR="$HOME/.dotfiles"

# Just to make sure config locations are exist
mkdir -p "$HOME/.mixxx"
mkdir -p "$HOME/.ncmpcpp"
mkdir -p "$HOME/.newsbeuter"
mkdir -p "$HOME/.translate-shell"
mkdir -p "$HOME/.turses"
mkdir -p "$HOME/.mpd"
touch "$HOME/.config/mpd/mpd.db"
touch "$HOME/.config/mpd/mpd.log"
touch "$HOME/.config/mpd/mpd.pid"
touch "$HOME/.config/mpd/mpdstate"
mkdir -p "$HOME/.config/dunst"
mkdir -p "$HOME/.config/mpd/playlists"
mkdir -p "$HOME/.config/mps-youtube"
mkdir -p "$HOME/.config/neofetch"
mkdir -p "$HOME/.config/newsbeuter"
mkdir -p "$HOME/.config/nvim"
mkdir -p "$HOME/.config/nvim/colors"
mkdir -p "$HOME/.config/ranger"
mkdir -p "$HOME/.config/rtv"
mkdir -p "$HOME/.config/shower_thoughts"
mkdir -p "$HOME/.config/thefuck"
mkdir -p "$HOME/.config/configstore"
mkdir -p "$HOME/.config/i3"

READLINK=$(which readlink || which greadlink)

cat $DOTFILES_DIR"/symlinks" | while read line; do
	link=$HOME'/'$line
	file=$DOTFILES_DIR'/config/'$line

	if [[ $line == *" "* ]]; then
		link=$HOME'/'$(echo $line | awk '{print $2}')
		file=$DOTFILES_DIR'/config/'$(echo $line | awk '{print $1}')
	fi	

	doLink=true
	doMove=false

	if [[ ! -f $link  && -d $link && $($READLINK -f $link) == $link ]]; then
		doMove=true
	fi

	if [[ -f $link  && ! -d $link && $($READLINK -f $link) == $link ]]; then
		doMove=true
	fi

	if [[ $($READLINK -f $link) == $file ]]; then
		doLink=false
	fi

	if [[ $doLink == true ]]; then
		echo $link" not linked, linking now to $file"
	fi

	if [[ $doMove == true ]]; then
		echo "file exists, creating "$link".old"
		mv $link $link".old"
	fi

	if [[ $doLink == true ]]; then
		mkdir -p $(dirname $link)
		ln -sfv $file $link
	fi
done
