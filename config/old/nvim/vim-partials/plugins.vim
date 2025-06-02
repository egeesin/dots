" Initial {{{1

if has('nvim')
	Plug 'lambdalisue/suda.vim' "an useful alternative to sudo tee, since sudo tee not working on nvim
endif
Plug 'dstein64/vim-startuptime' " a plugin for profiling startup time
" Type :StartupTime or launch (n)vim with "--startuptime" option to
" profile startup time automatically.

" Movement/Shortcut {{{1
Plug 'tpope/vim-repeat' "Repeat last command with dot
Plug 'ggandor/leap.nvim'
" Type s + two characters to match + labeled letter to leap onto the match.
Plug 'tpope/vim-surround' "shortcut to add paranthesis, gt lt etc.
" Type v(select)S(new-char) to surround with it,
" cs(old-char)(new-char) to change,
" type ds(current-char) to delete

Plug 'terryma/vim-expand-region'
" Visually select increasingly larger regions of text using the same key combination.
" Type + and _ in visual mode

" Plug 'easymotion/vim-easymotion' " <leader> w
" Plug 'jeffkreeftmeijer/vim-numbertoggle'
" Plug 'yuttie/comfortable-motion.vim' "Smooth scrolling
" Note: If you want to support unrepeatable command,
" silent! call repeat#set("\<Plug>MyWonderfulMap", v:count)

" Features that is similar to Sublime Text editor {{{1

" Plug 'kien/tabman.vim' "advanced tab manager
"Plug 'matze/vim-move' "move lines like subl3
Plug 'mg979/vim-visual-multi', {'branch': 'master'}
Plug 'AndrewRadev/splitjoin.vim' " Switch between single-line and multiline forms of code
Plug 'mattn/emmet-vim' "Type Ctrl+y+, - shortcuts for html,css,etc.
Plug 'alvan/vim-closetag' " Provides you a keybind that autocloses (X)HTML tags automatically
if has('nvim')
	Plug 'numToStr/Comment.nvim' " Type gcc/gc to comment the line
	Plug 'ethanholz/nvim-lastplace' " Saves last cursor position on each edited files
	Plug 'windwp/nvim-autopairs' " Auto pairs
else
	Plug 'tpope/vim-commentary'
	Plug 'farmergreg/vim-lastplace' " Saves last cursor position on each edited files
	Plug 'jiangmiao/auto-pairs' " Auto pairs
endif
" Plug 'brooth/far.vim' "Advanced f[ind] a[nd] r[eplace]

" Plug 'Yggdroot/indentLine' " Displays the indention levels with thin vertical lines

Plug 'shellRaining/hlchunk.nvim' " highlight your indent line and the current chunk (context) your cursor stayed
Plug 'yamatsum/nvim-cursorline' " highlights cursor words and lines

" Alignment {{{1
Plug 'godlygeek/tabular' "< this must come before markdown syntax or polyglot plugin!
" Plug 'junegunn/vim-easy-align'
" tommcdo/vim-lion

" Distraction-free Environment {{{1
Plug 'junegunn/goyo.vim' "provides distraction-free environment
" Plug 'pocco81/true-zen.nvim' "provides distraction-free environment in neovim
Plug 'junegunn/limelight.vim' "highlighting focused sentences/paragraphs

" Integration Between Apps {{{1
Plug 'christoomey/vim-tmux-navigator' "integrates vim/tmux pane management

" Ctags
" Plug 'majutsushi/tagbar' "lists all classes of page

" Searching & Finding {{{1
Plug 'haya14busa/is.vim' " Highlight while typing
Plug 'osyo-manga/vim-anzu' " Show search status
" Plug 'mhinz/vim-grepper', { 'on': ['Grepper', '<plug>(GrepperOperator)'] } " Lets you use your favorite Grep tool
" Has issues with Windows, need investigation...

" Git {{{1
Plug 'tpope/vim-git' " git runtime files
if has('nvim')
	Plug 'dinhhuy258/git.nvim' "useful tools for git
	Plug 'lewis6991/gitsigns.nvim' " git decorations (including gutters, signs, stage hunks etc.) implemented purely in Lua
else
	Plug 'tpope/vim-fugitive' "useful tools for git
	" Plug 'airblade/vim-gitgutter', {'branch': 'main'} "highlights the left of the lines which is added/deleted/modified since last commit
endif
"}}}
" LSP, DAP, CMP, Snippet & Linting (Neovim) {{{1
if has('nvim')
	Plug 'williamboman/mason.nvim', {'do': ':MasonUpdate' }
	" Portable package manager that lets you easily install
	" and manage LSP servers, DAP servers, linters, and formatters
	" :MasonUpdate updates registry contents

	" Plug 'Shougo/deoplete.nvim', { 'do': ':UpdateRemotePlugins' }
	" Plug 'Shougo/defx.nvim', { 'do': ':UpdateRemotePlugins' }
	" Plug 'kristijanhusak/defx-git'
	" Plug 'kristijanhusak/defx-icons'

	Plug 'nvim-lua/plenary.nvim'

	" Language Server
	Plug 'neovim/nvim-lspconfig'
	Plug 'williamboman/mason-lspconfig.nvim'

	Plug 'j-hui/fidget.nvim' " LSP Notifier

	" Debug Adapter
	Plug 'mfussenegger/nvim-dap'
	Plug 'rcarriga/nvim-dap-ui'

	" Linters
	Plug 'folke/lsp-colors.nvim'
	Plug 'onsails/lspkind.nvim' " Icons for Auto Completion Items (like VSCode)

	" Auto Completion Plugin & Sources
	Plug 'hrsh7th/nvim-cmp' " Main auto completion plugin

	Plug 'hrsh7th/cmp-nvim-lsp' " nvim-cmp source for Neovim's built-in language server client
	Plug 'FelipeLema/cmp-async-path' " List paths in auto completion

	Plug 'amarakon/nvim-cmp-buffer-lines' " Buffer lines
	Plug 'hrsh7th/cmp-buffer'

	Plug 'hrsh7th/cmp-cmdline' " completion in command/search mode
	Plug 'dmitmel/cmp-cmdline-history' " Command Line History in completion menu

	Plug 'lukas-reineke/cmp-rg' " ripgrep source

	Plug 'petertriho/cmp-git' " git source (for issue,mention,PR completion, GitHub/GitLab CLI is required)
	" Plug 'Dosx001/cmp-commit' " completion for gitcommit filetype
	Plug 'davidsierradz/cmp-conventionalcommits' " Conventional Commit source

	Plug 'amarakon/nvim-cmp-fonts' " font name (fc-list) source
	Plug 'andersevenrud/cmp-tmux' " tmux source
	Plug 'tamago324/cmp-zsh' " zshell source

	Plug 'hrsh7th/cmp-emoji' " emoji source
	Plug 'chrisgrieser/cmp-nerdfont' " nerd font source

	" Has issues with Windows
	" Plug 'tzachar/fuzzy.nvim' " Abstraction layer between telescope-fzf-native and fuzzy cmp plugins
	" Plug 'tzachar/cmp-fuzzy-path' " source for filesystem paths. (Depends on fd, fuzzy.nvim and other fzf related plugins)
	" Plug 'tzachar/cmp-fuzzy-buffer' " source for buffers with fzf support

	" Snippets

	" For vsnip users.
	" Plug 'hrsh7th/cmp-vsnip'
	" Plug 'hrsh7th/vim-vsnip'
	" Plug 'hrsh7th/vim-vsnip-integ'

	" For LuaSnip users.
	Plug 'L3MON4D3/LuaSnip', {'tag': 'v2.*', 'do': 'make install_jsregexp'} " Replace <CurrentMajor> by the latest released major (first number of latest release)
	Plug 'saadparwaiz1/cmp_luasnip'
	Plug 'rafamadriz/friendly-snippets'

	Plug 'nvim-treesitter/nvim-treesitter', {'do': ':TSUpdate'} " Treesitter configurations and abstraction layer
	" Provides syntax highlighter, indentation
	" Plug 'nvim-treesitter/nvim-treesitter-textobjects'

	Plug 'ray-x/cmp-treesitter' " treesitter completion
else
	Plug 'Shougo/deoplete.nvim'
	Plug 'roxma/nvim-yarp'
	Plug 'roxma/vim-hug-neovim-rpc'
	" Plug 'dense-analysis/ale' "Asynchronous linting engine
	" Plug 'maximbaz/lightline-ale' "Lightline + ALE integration
endif


" Theme & Syntax Highlight {{{1

if has('nvim')
	Plug 'rktjmp/lush.nvim' " Color Scheme Tool
	Plug 'loganswartz/selenized.nvim' " Current colorscheme (Dep: lush.nvim)
	" Plug 'iCyMind/NeoSolarized

	Plug 'nvim-lualine/lualine.nvim' " Status Bar Customization
	Plug 'akinsho/bufferline.nvim', { 'tag': '*' } " Tabline (Buffers as Vim Tabs) Customization
	" Plug 'kdheepak/tabline.nvim' " Tabline Customizations, allows integration with lualine
	Plug 'tiagovla/scope.nvim'

	" Plug 'martineausimon/nvim-xresources' " XResources to Neovim (Deprecated, need testing in GNU/Linux)
	Plug 'hat0uma/csvview.nvim' " CSV Tabular Data Highlighter
else
	Plug 'itchyny/lightline.vim' " easy vim bar customization
	" Plug 'edkolev/promptline.vim' "integrates lightline with prompt line
	" Plug 'edkolev/tmuxline.vim' "integrates, uuhh nvm...
	" Plug 'preservim/vim-markdown' " Markdown, front matter highlight
endif
" Plug 'dylanaraps/wal.vim'

Plug 'darfink/vim-plist' "adds .plist support for readability
" Plug 'jamessan/vim-gnupg' "adds gnupg support

" Disable polyglot syntax highlighting in specific filetypes
" let g:polyglot_disabled = ['md','css','html','js']
" Plug 'sheerun/vim-polyglot' "adds support for almost every programming language exists

" CSS Related Syntax Plugins
" Plug 'hail2u/vim-css3-syntax' "css syntax highlighter
" Plug 'ap/vim-css-color' "color highlights
" Plug 'vim-scripts/CSSMinister' " Converts CSS colors
" Plug 'jaxbot/semantic-highlight.vim' "Highlights variable names
" Plug 'antonk52/vim-browserslist'

" Plug 'RRethy/vim-hexokinase' " Color highlighter (Archived)
if has('nvim')
	Plug 'NvChad/nvim-colorizer.lua' " Color highlighter
endif

" Converter {{{1

Plug 'joom/turkish-deasciifier.vim'
" Type <Space>tr to convert to Turkish characters in visual mode. <Space>rt to
" do reverse
Plug 'caglartoklu/tex_turkce.vim'
Plug 'dhruvasagar/vim-table-mode'


" Tab/Window/Buffer Management {{{1

Plug 'nvim-tree/nvim-tree.lua'
Plug 'nvim-tree/nvim-web-devicons'

if executable('fzf')
	if has('win32')
		" Scoop on Windows
		" set rtp+C:\Users\ege_e\scoop\apps\fzf\current\=
		Plug 'C:\Users\ege_e\scoop\apps\fzf\current\'
	else
		" Homebrew on Apple Intel
		" set rtp+=/usr/local/opt/fzf
		Plug '/usr/local/opt/fzf'
	endif
	" Check: https://github.com/junegunn/fzf/wiki/Windows
	Plug 'junegunn/fzf', { 'do': { -> fzf#install() } } "some integration between vim and fzf
	Plug 'junegunn/fzf.vim' "some integration between vim and fzf
endif

if has('nvim')
	Plug 'nvim-telescope/telescope.nvim', { 'tag': '0.1.6' }
	Plug 'nvim-telescope/telescope-ui-select.nvim'
	if has('win32')
		" Install mingw from Scoop -> scoop install mingw'
		Plug 'nvim-telescope/telescope-fzf-native.nvim', { 'do': 'make' }
	else
		Plug 'nvim-telescope/telescope-fzf-native.nvim', { 'do': 'cmake -S. -Bbuild -DCMAKE_BUILD_TYPE=Release && cmake --build build --config Release && cmake --install build --prefix build' }
	endif

	" Dependency: cmake in macOS and Windows
	Plug 'nvim-telescope/telescope-dap.nvim'

	Plug 'benfowler/telescope-luasnip.nvim'
	Plug 'debugloop/telescope-undo.nvim'

	Plug 'kkharji/sqlite.lua'
	Plug 'nvim-telescope/telescope-frecency.nvim'
	Plug 'AckslD/nvim-neoclip.lua'

	Plug 'nvim-telescope/telescope-symbols.nvim'
	" Plug 'xiyaowong/telescope-emoji.nvim' " Replaced by cmp plugins
	" Plug 'olacin/telescope-gitmoji.nvim'
	" Plug 'olacin/telescope-cc.nvim'

	Plug 'crispgm/telescope-heading.nvim'
	Plug 'paopaol/telescope-git-diffs.nvim'
	" Plug 'octarect/telescope-menu.nvim'

	Plug 'folke/trouble.nvim'
	" A pretty diagnostics, references, telescope results, quickfix and location
	" list to help you solve all the trouble your code is causing.

endif

" Plug 'mcchrish/nnn.vim' "nnn integration

" Plug 'lambdalisue/nerdfont.vim'
" Plug 'lambdalisue/fern-renderer-nerdfont.vim'
" Plug 'lambdalisue/glyph-palette.vim'

" CursorHold fixing - (Neovim only)
" Plug 'antoinemadec/FixCursorHold.nvim'

" Plug 'ryanoasis/vim-devicons'

" Plug 'scrooloose/nerdtree' " working directory tree in sidebar
" Plug 'Xuyuanp/nerdtree-git-plugin' " shows git status in nerdtree
" Plug 'tiagofumo/vim-nerdtree-syntax-highlight' "Syntax highlightning in NERDTree
" Plug 'unkiwii/vim-nerdtree-sync'

" Plug 'jlanzarotta/bufexplorer'
if has('nvim')
	" Plug 'jedrzejboczar/possession.nvim' " Requires plenary.nvim
else
	Plug 'xolox/vim-misc'
	Plug 'xolox/vim-session'
end

" Plug 'Shatur/neovim-session-manager'
" Plug 'zefei/vim-wintabs'
" Plug 'vim-scripts/po.vim'

" Miscellaneous {{{1

Plug 'folke/which-key.nvim' " Helper
" On-demand lazy load
" Plug 'liuchengxu/vim-which-key', { 'on': ['WhichKey', 'WhichKey!'] }

" Plug 'sjl/gundo.vim' "DEPRECATED advanced undoing stuff
Plug 'mbbill/undotree' "undo tree

" Plug 'vimwiki/vimwiki' "about wiki management, taking notes
" Plug 'will133/vim-dirdiff' "diffs files
" Plug 'mattn/vim-gist' "Vimscript for Gist
" Plug 'ntpeters/vim-better-whitespace' "Detect unnecessary whitespaces, type :ToggleWhitespace and to gid rid of whitespaces, type :StripWhitespace
" Plug 'itchyny/calendar.vim' "An advanced calendar application
Plug 'tpope/vim-characterize' "Shows character info | Type 'ga'
" Type <Leader><Leader>, then go wherever you want
" Plug 'vim-scripts/loremipsum' "A dummy text generator
Plug 'chrisbra/unicode.vim'

" dep: Linux: xclip/wl-clipboard - macOS: pngpaste - Windows: no dep
Plug 'HakonHarnes/img-clip.nvim' " Embed images into any markup lang like LaTeX, Markdown
" See if your emulator supports img drag drop here:
" https://github.com/HakonHarnes/img-clip.nvim#%EF%B8%8F-drag-and-drop

" Plug 'suan/vim-instant-markdown' "Instant Markdown previews from Vim! | dep: npm i -g instant-markdown-d
Plug 'mikeboiko/vim-markdown-folding' " Adds folding ability to Markdown files. Type :FoldToggle to start folding/unfolding.

" Plug 'vim-pandoc/vim-pandoc' " Advanced markdown syntax highlighter/Pandoc integration
" Plug 'vim-pandoc/vim-pandoc-syntax'

call plug#end()
