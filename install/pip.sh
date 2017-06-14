packages=(
Cython --install-option="--no-cython-compile"
Pillow
BeautifulSoup4
virtualenv
AskQuora
gallery-dl
pockyt
)
# Note: https://github.com/alyakhtar/Katastrophe/issues/9

[[ "$(uname -s)" == "Darwin" ]] && pip install "${packages[@]}"
[[ "$(uname -s)" == "Linux" ]] && sudo pip install "${packages[@]}"

# Python 3+ packages
packages=(
requests
docopt
git+https://github.com/0xl3vi/we-get
)

[[ "$(uname -s)" == "Darwin" ]] && pip3 install "${packages[@]}"
[[ "$(uname -s)" == "Linux" ]] && sudo pip3 install "${packages[@]}"

# macOS only
if [ "$(uname -s)" == "Darwin" ]; then
	pip install haxor-news
	pip install cheat
	pip install urlscan
	pip3 install stig
fi
