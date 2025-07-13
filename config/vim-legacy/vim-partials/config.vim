" ======= Settings
" character encoding
if !&readonly && &modifiable
	set fileencoding=utf-8              " the encoding written to file
endif
set encoding=utf-8                    " the encoding displayed

" General {{{1
set nocompatible " get rid of Vi compatibility mode. SET FIRST!
filetype off
" Enable loading the plugin/indent files for specific file types
if has('autocmd')
    filetype plugin indent on
endif

" let g:loaded_netrwPlugin = 1          "Do not load netrw
" let g:loaded_matchit = 1              "Do not load matchit, use matchup plugin

" set nu rnu
set numberwidth=5 " Set line number character length

if has("win16") || has("win32")
else
	set shell=zsh\ -i
	" set shell=zsh
endif

"autocmd InsertEnter * :set number
"autocmd InsertLeave * :set relativenumber
set backspace=indent,eol,start  "Allow backspace in insert mode
set history=1000                "Store lots of :cmdline history

" if version >= 703
" set undodir=~/.vim/backup
" set undofile
" set undoreload=10000
" endif

if has("cmdline_info")
	set ruler                   " show the ruler
	set rulerformat=%30(%=\:b%n%y%m%r%w\ %l,%c%V\ %P%) " a ruler on steroids
	set showcmd                     "Show incomplete cmds down the bottom
endif
set visualbell                  "No sounds
set t_vb=
set autoread                    "Reload files changed outside vim
set laststatus=2                "last window always has a statusline
set hidden                      "Hide buffer instead of closing it
set pastetoggle=<F2>            "Paste without being smart
set mouse=a mousehide           "Enable mouse support / Hide mouse cursor while typing
set ttyfast
set tabpagemax=12
set confirm
set cmdheight=1
set diffopt+=vertical           "Always use vertical layout for diffs
set pyxversion=3                " Always use Python 3

set nospell " Disable spell checking (while pandoc ftdetect and spell checking is on, it gets annoying with markdown files)

" Search {{{1

set hlsearch                  " highlight search results
set incsearch                 " search as characters are entered
set ignorecase                " make searches case-insensitive
set showmatch                 " Highlight parenthesis
set smartcase

" Backup / Swap {{{1

set noswapfile
set nobk " Don't make a backup after overwriting a file (that keeps one after succesful write)
set nowb " Don't make a backup before overwriting a file (that removes one after succesful write but can be overriden by above config)
" set backup
" set backupdir=~/.vim-tmp,~/.tmp,~/tmp,/var/tmp,/tmp
" set backupskip=/tmp/*,/private/tmp/*
" set directory=~/.vim-tmp,~/.tmp,~/tmp,/var/tmp,/tmp
" set writebackup
" Swap file and backups
"au FocusLost * :wa

" Session Options {{{1

set ssop+=options,buffers,winsize,curdir,folds,help
set ssop+=tabpages,globals " store tabpages and globals in session (This is coming from tabline.nvim docs)

if has("gui_running")
	set ssop+=winpos,resize
else
	set ssop-=winpos,resize
endif

" Clipboard {{{1
"
" if has('mac')
" 	let g:clipboard = {
" 		\   'name': 'macOS-clipboard',
" 		\   'copy': {
" 		\      '+': 'pbcopy',
" 		\      '*': 'pbcopy',
" 		\    },
" 		\   'paste': {
" 		\      '+': 'pbpaste',
" 		\      '*': 'pbpaste',
" 		\   },
" 		\   'cache_enabled': 0,
" 		\ }
" endif

" if system('uname -a | grep microsoft') != ""
" 	let g:clipboard = {
" 		\   'name': 'wslClipboard',
" 		\   'copy': {
" 		\      '+': 'win32yank.exe -i',
" 		\      '*': 'win32yank.exe -i',
" 		\    },
" 		\   'paste': {
" 		\      '+': 'win32yank.exe -o',
" 		\      '*': 'win32yank.exe -o',
" 		\   },
" 		\   'cache_enabled': 1,
" 		\ }
" 	" set t_Co=256
" 	set t_ut=""
" endif
" set clipboard+=unnamedplus"

" if has('clipboard')
" 	set clipboard& clipboard+=unnamedplus
" endif


" Indentation {{{1
set autoindent
set smartindent
set smarttab                  " use tabs at the start of a line, spaces elsewhere
set ts=4 sw=4 noet            " tab & shift spacing (No spaces/Tabs and shift units are 4 spaces)
" set ts=2 sw=2 et              " tab & shift spacing (2x spaces and shifts/No tab char)
set softtabstop=4             " unify
set shiftround                " always indent/outdent to the nearest tabstop

set list
" set listchars=tab:▸\ ,eol:¬
" set listchars=tab:░\ ,trail:␣,eol:↴,nbsp:+,extends:»,precedes:«
set listchars=tab:∙\ ,trail:␣,eol:ꜚ,nbsp:∙,extends:→,precedes:←

" Wrapping {{{1

set nowrap                    " don't wrap text
set linebreak                 " wrap lines at convenient points


" Folding {{{1
" set foldnestmax=10            " 10 nested fold max
" set foldlevelstart=10         " Open most folds by default

" toggle foldenable
"
" set foldmethod=marker         " Fold based on indent level
set foldmethod=indent         " Fold based on indent level
set nofoldenable              " don't fold by default

set foldcolumn=2
" set foldnestmax=3
" set foldlevel=1


" Scrolling {{{1

set scrolloff=4
set sidescrolloff=15
set sidescroll=1


" Split Direction {{{1

set splitbelow
set splitright

" Colors {{{1

" set t_Co=256
" set t_AB=^[[48;5;%dm
" set t_AF=^[[38;5;%dm

" Enable True Color support for Neovim if current

set background=dark

" Wild Menu {{{1
"
set wildmenu                "enable ctrl-n and ctrl-p to scroll thru matches
set wildmode=longest:full,full
set wildignore=*.o,*.obj,*~ "stuff to ignore when tab completing
set wildignore+=*vim/backups*
set wildignore+=*sass-cache*
set wildignore+=*DS_Store*
set wildignore+=vendor/rails/**
set wildignore+=vendor/cache/**
set wildignore+=*.gem
set wildignore+=log/**
set wildignore+=tmp/**
set wildignore+=*.jpg,*.bmp,*.gif,*.png,*.jpeg,*.svg
set wildignore+=*.swp,*.pyc,*.bak,*.class,*.orig
set wildignore+=.git,.hg,.bzr,.svn

" Other {{{1

" Persistent Undo {{{2

" if has('persistent_auto')
if has("win16") || has("win32")
" TODO: Windows equivalent of temporary undodir should be declared here.
else
	if !isdirectory("/tmp/.nvim-undo")
		call mkdir("/tmp/.nvim-undo", "", 0700)
	endif
	set undodir=/tmp/.nvim-undo
	set undofile
endif
" endif

" Dynamic Cursor in tmux {{{2

if exists('$TMUX')
	let &t_SI = "\<Esc>Ptmux;\<Esc>\<Esc>]50;CursorShape=1\x7\<Esc>\\"
	let &t_EI = "\<Esc>Ptmux;\<Esc>\<Esc>]50;CursorShape=0\x7\<Esc>\\"
else
	let &t_SI = "\<Esc>]50;CursorShape=1\x7"
	let &t_EI = "\<Esc>]50;CursorShape=0\x7"
endif

autocmd VimResized * :wincmd = " Automatically rebalance windows on vim resize

au BufRead /tmp/mutt-* set tw=72 " Editing draft in Mutt
