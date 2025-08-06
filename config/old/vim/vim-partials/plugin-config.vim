" ======= Plugin Settings
" Tip: Type :set wrap

" vim-session | Advanced session manager {{{1
"
let g:session_autosave = 'no'
let g:session_autoload = 'prompt'
let g:session_default_name = fnamemodify(getcwd(), ':t')

" fzf | Fuzzy finder {{{1
"

let g:fzf_layout = { 'down': '~40%' }
" neovim only
let g:fzf_layout = { 'window': 'enew' }
let g:fzf_layout = { 'window': '-tabnew' }

" Customize fzf colors to match your color scheme
let g:fzf_colors =
	\ { 'fg':      ['fg', 'Normal'],
	\ 'bg':      ['bg', 'Normal'],
	\ 'hl':      ['fg', 'Comment'],
	\ 'fg+':     ['fg', 'CursorLine', 'CursorColumn', 'Normal'],
	\ 'bg+':     ['bg', 'CursorLine', 'CursorColumn'],
	\ 'hl+':     ['fg', 'Statement'],
	\ 'info':    ['fg', 'PreProc'],
	\ 'prompt':  ['fg', 'Conditional'],
	\ 'pointer': ['fg', 'Exception'],
	\ 'marker':  ['fg', 'Keyword'],
	\ 'spinner': ['fg', 'Label'],
	\ 'header':  ['fg', 'Comment'] }

let g:fzf_history_dir = '~/.local/share/fzf-history'

" Ripgrep Integration
command! -bang -nargs=* Rg
	\ call fzf#vim#grep(
	\   'rg --column --line-number --no-heading --color=always '.shellescape(<q-args>), 1,
	\   <bang>0 ? fzf#vim#with_preview('up:60%')
	\           : fzf#vim#with_preview('right:50%:hidden', '?'),
	\   <bang>0)

" set grepprg=rg\ --vimgrep
set grepprg=rg\ --vimgrep\ $*

" Add fzf to statusline (Neovim-only)
function! s:fzf_statusline()
	" Override statusline as you like
	highlight fzf1 ctermfg=161 ctermbg=251
	highlight fzf2 ctermfg=23 ctermbg=251
	highlight fzf3 ctermfg=237 ctermbg=251
	setlocal statusline=%#fzf1#\ >\ %#fzf2#fz%#fzf3#f
endfunction

autocmd! User FzfStatusLine call <SID>fzf_statusline()



" vim-anzu | Search Status {{{1
" Integration with is.vim (Incremental Search Improved)
map n <Plug>(is-nohl)<Plug>(anzu-n-with-echo)
map N <Plug>(is-nohl)<Plug>(anzu-N-with-echo)
" nmap n <Plug>(anzu-mode-n)
" nmap N <Plug>(anzu-mode-N)
" nmap * <Plug>(anzu-star-with-echo)
" nmap # <Plug>(anzu-sharp-with-echo)
nmap <Esc><Esc> <Plug>(anzu-clear-search-status)
" clear status

" nvim-tree.lua | File Browser {{{1
noremap <silent> <Leader>n :NvimTreeToggle<CR><C-w>=
" Fern.vim | File Browser {{{1
"
" TODO: These Fern mappings doesn't work. Need investigating, comparison.
" function! s:fern_settings() abort
" 	nmap <silent> <buffer> p     <Plug>(fern-action-preview:toggle)
" 	nmap <silent> <buffer> <C-p> <Plug>(fern-action-preview:auto:toggle)
" 	nmap <silent> <buffer> <C-d> <Plug>(fern-action-preview:scroll:down:half)
" 	nmap <silent> <buffer> <C-u> <Plug>(fern-action-preview:scroll:up:half)
" endfunction
" augroup fern-settings
" 	autocmd!
" 	autocmd FileType fern call s:fern_settings()
" augroup END

let g:fern_disable_startup_warnings = 1
let g:fern#mapping#bookmark#disable_default_mappings = 0
let g:fern#disable_drawer_auto_quit   = 1
let g:fern#disable_viewer_hide_cursor = 1

" let g:fern#renderer = "nerdfont"

augroup my-glyph-palette
  autocmd! *
  autocmd FileType fern call glyph_palette#apply()
  autocmd FileType nerdtree,startify call glyph_palette#apply()
augroup END

" noremap <silent> <Leader>n :Fern %:h -drawer -reveal=% -width=32 -toggle<CR><C-w>=
" noremap <silent> <Leader>f :Fern . -drawer -reveal=% -width=35<CR><C-w>=
" noremap <silent> <Leader>. :Fern %:h -drawenzr -width=35<CR><C-w>=

" let g:fern#mark_symbol                       = '● '
let g:fern#mark_symbol                       = '○ '
let g:fern#renderer#default#collapsed_symbol = '▶ '
let g:fern#renderer#default#expanded_symbol  = '▼ '
let g:fern#renderer#default#leading          = '  '
let g:fern#renderer#default#leaf_symbol      = '  '
" let g:fern#renderer#default#root_symbol      = '~ '
let g:fern#renderer#default#root_symbol      = '◈ '


" Limelight | Focus on the paragraph {{{1
"

nmap <Leader>l <Plug>(Limelight)
xmap <Leader>l <Plug>(Limelight)

" Color name (:help cterm-colors) or ANSI code
let g:limelight_conceal_ctermfg = 10
let g:limelight_default_coefficient = 0.7
let g:limelight_paragraph_span = 1
" Beginning/end of paragraph
"   When there's no empty line between the paragraphs
"   and each paragraph starts with indentation
let g:limelight_bop = '^\s'
let g:limelight_eop = '\ze\n^\s'

" Limelight + Goyo.vim integration
" autocmd! User GoyoEnter Limelight
" autocmd! User GoyoLeave Limelight!

" The Prose Mode from <https://statico.github.io/vim3.html>
function! ProseMode()
	call goyo#execute(0, [])
	autocmd! BufEnter,FocusGained,InsertLeave *
	set wrap nonu nornu noci nosi noai nolist noshowmode noshowcmd nocursorline nocursorcolumn
	set complete+=s
	let g:ale_enabled=0
endfunction

command! ProseMode call ProseMode()
" nmap \p :ProseMode<CR>
nmap <leader>p :ProseMode<CR>


" GitGutter | Essential tools for Git {{{1
"
" Emoji Indicators
" let g:gitgutter_sign_added = emoji#for('small_blue_diamond')
" let g:gitgutter_sign_modified = emoji#for('small_orange_diamond')
" let g:gitgutter_sign_removed = emoji#for('small_red_triangle')
" let g:gitgutter_sign_modified_removed = emoji#for('collision')
" nmap ]h <Plug>GitGutterNextHunk
" nmap [h <Plug>GitGutterPrevHunk
" nmap <Leader>ha <Plug>GitGutterStageHunk
" nmap <Leader>hr <Plug>GitGutterUndoHunk
" nmap <Leader>hv <Plug>GitGutterPreviewHunk
" omap ih <Plug>GitGutterTextObjectInnerPending
" omap ah <Plug>GitGutterTextObjectOuterPending
" xmap ih <Plug>GitGutterTextObjectInnerVisual
" xmap ah <Plug>GitGutterTextObjectOuterVisual

" Disable all of them
"let g:gitgutter_map_keys = 0
" To get rid of lag:
" let g:gitgutter_realtime = 0
" let g:gitgutter_eager = 0
" let g:gitgutter_sign_added = 'xx'
" let g:gitgutter_sign_modified = 'yy'
" let g:gitgutter_sign_removed = 'zz'
" let g:gitgutter_sign_removed_first_line = '^^'
" let g:gitgutter_sign_modified_removed = 'ww'


" Translate Shell Integration
"
" set keywordprg=trans\ :tr
" Type K to translate selected word.

" Solarized Theme (Compatible with NeoVim)
" " let g:solarized_termcolors=256
" let g:neosolarized_contrast = "normal" "high / low / normal
" let g:neosolarized_visibility = "high"
" let g:neosolarized_vertSplitBgTrans = 0
" let g:neosolarized_bold = 1
" let g:neosolarized_underline = 1
" let g:neosolarized_italic = 1
" colorscheme NeoSolarized

" vim-visual-multi {{{1
let g:VM_default_mappings = 0
" All default mappings are disabled except C-n for selecting words

let g:VM_show_warnings = 0
let g:VM_leader = {}

" coc | Autocompletion with Language Server {{{1

" Color changes
" hi! link CocErrorSign WarningMsg
" hi! link CocWarningSign Number
" hi! link CocInfoSign Type

" nmap <silent> <leader>dd <Plug>(coc-definition)
" nmap <silent> <leader>dr <Plug>(coc-references)
" nmap <silent> <leader>dj <Plug>(coc-implementation)

" coc-git
" " navigate chunks of current buffer
" nmap [g <Plug>(coc-git-prevchunk)
" nmap ]g <Plug>(coc-git-nextchunk)
" " show chunk diff at current position
" nmap gs <Plug>(coc-git-chunkinfo)
" " show commit ad current position
" " nmap gc <Plug>(coc-git-commit)

" Polyglot | Syntax Highlighting / Better File Type Detector {{{1
"
" let g:polyglot_disabled = ['css']

" po.vim {{{1

" let g:po_translator='msgfmt'

let g:pandoc#modules#disabled = [ 'spell' ]
let g:pandoc#folding#fdc = 0
set conceallevel=0

" Emmet {{{1

let g:user_emmet_mode='in'
let g:user_emmet_install_global = 0
autocmd FileType html,liquid,md,haml,css,sass EmmetInstall

" Close Tag {{{1
" filenames like *.xml, *.html, *.xhtml, ...
" These are the file extensions where this plugin is enabled.
"
let g:closetag_filenames = '*.html,*.xhtml,*.phtml'

" filenames like *.xml, *.xhtml, ...
" This will make the list of non-closing tags self-closing in the specified files.
"
let g:closetag_xhtml_filenames = '*.xhtml,*.jsx'

" filetypes like xml, html, xhtml, ...
" These are the file types where this plugin is enabled.
"
let g:closetag_filetypes = 'html,xhtml,phtml,liquid,markdown'

" filetypes like xml, xhtml, ...
" This will make the list of non-closing tags self-closing in the specified files.
"
let g:closetag_xhtml_filetypes = 'xhtml,jsx'

" integer value [0|1]
" This will make the list of non-closing tags case-sensitive (e.g. `<Link>` will be closed while `<link>` won't.)
"
let g:closetag_emptyTags_caseSensitive = 1

" dict
" Disables auto-close if not in a "valid" region (based on filetype)
"
let g:closetag_regions = {
    \ 'typescript.tsx': 'jsxRegion,tsxRegion',
    \ 'javascript.jsx': 'jsxRegion',
    \ 'typescriptreact': 'jsxRegion,tsxRegion',
    \ 'javascriptreact': 'jsxRegion',
    \ }

" Shortcut for closing tags, default is '>'
"
let g:closetag_shortcut = '>'

" Add > at current position without closing the current tag, default is ''
"
let g:closetag_close_shortcut = '<leader>>'

" Gundo | Graphical Undo Tree {{{1

" nnoremap <leader>u :GundoToggle<CR> " Replaced by telescope-undo (nvim)

" Tagbar | C Companion {{{1

" CSS
let g:tagbar_type_css = {
\ 'ctagstype' : 'Css',
	\ 'kinds'     : [
		\ 'c:classes',
		\ 's:selectors',
		\ 'i:identities'
	\ ]
\ }
" Markdown
let g:tagbar_type_markdown = {
	\ 'ctagstype' : 'markdown',
	\ 'kinds' : [
		\ 'h:Heading_L1',
		\ 'i:Heading_L2',
		\ 'k:Heading_L3'
	\ ]
\ }


" Turkish-DeASCIIfier | Convert Turkish glyphs to ASCII characters {{{1
"

let g:turkish_deasciifier_path = 'deasciify'
vmap <Space>tr :<c-u>call Turkish_Deasciify()<CR>
vmap <Space>rt :<c-u>call Turkish_Asciify()<CR>

" Commentary | Comment text with shortcut {{{1
"
" Add apache integration
" autocmd FileType apache setlocal commentstring=#\ %s

" Add comment highlighting for jsonc files
autocmd FileType json syntax match Comment +\/\/.\+$+

" luasnip | Snippet engine for Neovim written in Lua {{{1
"
" press <Tab> to expand or jump in a snippet. These can also be mapped separately
" via <Plug>luasnip-expand-snippet and <Plug>luasnip-jump-next.
imap <silent><expr> <Tab> luasnip#expand_or_jumpable() ? '<Plug>luasnip-expand-or-jump' : '<Tab>'
" -1 for jumping backwards.
inoremap <silent> <S-Tab> <cmd>lua require'luasnip'.jump(-1)<Cr>

snoremap <silent> <Tab> <cmd>lua require('luasnip').jump(1)<Cr>
snoremap <silent> <S-Tab> <cmd>lua require('luasnip').jump(-1)<Cr>

" For changing choices in choiceNodes (not strictly necessary for a basic setup).
imap <silent><expr> <C-E> luasnip#choice_active() ? '<Plug>luasnip-next-choice' : '<C-E>'
smap <silent><expr> <C-E> luasnip#choice_active() ? '<Plug>luasnip-next-choice' : '<C-E>'


" Tabular.vim | text filtering and alignment {{{1
" http://vimcasts.org/episodes/aligning-text-with-tabular-vim/

" Align " =
if exists(":Tabularize")
	nmap <Leader>a= :Tabularize /=<CR>
	vmap <Leader>a= :Tabularize /=<CR>
	nmap <Leader>a: :Tabularize /:\zs<CR>
	vmap <Leader>a: :Tabularize /:\zs<CR>
endif

" Auto Cucumber Table in Insert Mode

" https://gist.github.com/tpope/287147
inoremap <silent> <Bar>   <Bar><Esc>:call <SID>align()<CR>a
function! s:align()
	let p = '^\s*|\s.*\s|\s*$'
	if exists(':Tabularize') && getline('.') =~# '^\s*|' && (getline(line('.')-1) =~# p || getline(line('.')+1) =~# p)
		let column = strlen(substitute(getline('.')[0:col('.')],'[^|]','','g'))
		let position = strlen(matchstr(getline('.')[0:col('.')],'.*|\s*\zs.*'))
		Tabularize/|/l1
		normal! 0
		call search(repeat('[^|]*|',column).'\s\{-\}'.repeat('.',position),'ce',line('.'))
	endif
endfunction


" vim-vsnip | Snippet plugin that supports LSP/VSCode's snippet format (Unused){{{1
"
" " Expand
" imap <expr> <C-j>   vsnip#expandable()  ? '<Plug>(vsnip-expand)'         : '<C-j>'
" smap <expr> <C-j>   vsnip#expandable()  ? '<Plug>(vsnip-expand)'         : '<C-j>'
"
" " Expand or jump
" imap <expr> <C-l>   vsnip#available(1)  ? '<Plug>(vsnip-expand-or-jump)' : '<C-l>'
" smap <expr> <C-l>   vsnip#available(1)  ? '<Plug>(vsnip-expand-or-jump)' : '<C-l>'
"
" " Jump forward or backward
" imap <expr> <Tab>   vsnip#jumpable(1)   ? '<Plug>(vsnip-jump-next)'      : '<Tab>'
" smap <expr> <Tab>   vsnip#jumpable(1)   ? '<Plug>(vsnip-jump-next)'      : '<Tab>'
" imap <expr> <S-Tab> vsnip#jumpable(-1)  ? '<Plug>(vsnip-jump-prev)'      : '<S-Tab>'
" smap <expr> <S-Tab> vsnip#jumpable(-1)  ? '<Plug>(vsnip-jump-prev)'      : '<S-Tab>'
"
" " Select or cut text to use as $TM_SELECTED_TEXT in the next snippet.
" " See https://github.com/hrsh7th/vim-vsnip/pull/50
" " Added Leader because of conflicted leap.nvim shortcut
" nmap <Leader>s <Plug>(vsnip-select-text)
" xmap <Leader>s <Plug>(vsnip-select-text)
" nmap <Leader>S <Plug>(vsnip-cut-text)
" xmap <Leader>S <Plug>(vsnip-cut-text)
"
" " If you want to use snippet for multiple filetypes, you can `g:vsnip_filetypes` for it.
" let g:vsnip_filetypes = {}
" let g:vsnip_filetypes.javascriptreact = ['javascript']
" let g:vsnip_filetypes.typescriptreact = ['typescript']

" vim-markdown-preview (Unused) {{{1

" let vim_markdown_preview_browser='Firefox'
" let vim_markdown_preview_github=0
" let vim_markdown_preview_pandoc=1

" Deoplete | Autocompletion Plugin (Unused) {{{1
" Dependency: pip2/pip3 install neovim

" set omnifunc=syntaxcomplete#Complete

" set omnifunc=webcompelete#complete
" set completefunc=webcomplete#complete

" let g:deoplete#enable_at_startup = 1
" Disable completion plugins
" let g:deoplete#ignore_sources = get(g:, 'deoplete#ignore_sources', {})
" let g:deoplete#ignore_sources.php = ['omni']

" ALE | Async Linting Engine (Unused) {{{1

let g:ale_sign_column_always = 2
let g:ale_completion_enabled = 2
let g:ale_completon_autoimport = 1
set omnifunc=ale#completion#OmniFunc


" let g:ale_sign_error = '>>'
" let g:ale_sign_warning = '--'
let g:ale_sign_error = '❌'
let g:ale_sign_warning = '❕'
highlight clear ALEErrorSign
highlight clear ALEWarningSign
highlight ALEWarning ctermbg=DarkMagenta
" For jsx, install stylelint-processor-styled-components
let g:ale_linter_aliases = {
\   'jsx': ['css', 'javascript'],
\   'vue': ['vue', 'javascript']
\}
let g:ale_linters = {
\   'javascript':  ['eslint'],
\   'json':        ['jq'],
\   'jsx':         ['stylelint', 'eslint'],
\   'typescript':  ['tsserver'],
\   'vue':         ['eslint', 'vls'],
\	'less':        ['stylelint'],
\   'html':        ['alex'],
\	'xhtml':       ['alex'],
\	'haml':        ['haml-lint'],
\	'glsl':        ['glslang'],
\	'dockerfile':  ['dockerfile_lint'],
\	'desktop':     ['desktop-file-validate'],
\	'css':         ['stylelint'],
\	'cmake':       ['cmake-format'],
\	'cpp':         ['uncrustify'],
\	'c':           ['uncrustify'],
\	'csharp':      ['uncrustify'],
\   'bash':        ['shellcheck'],
\   'bats':        ['shellcheck'],
\	'gitcommit':   ['gitlint'],
\	'yaml':        ['prettier'],
\	'po':          ['msgfmt'],
\	'powershell':  ['powershell'],
\	'pug':         ['puglint'],
\	'python':      ['pytlint'],
\	'ruby':        ['ruby'],
\	'rust':        ['cargo'],
\	'sass':        ['stylelint'],
\	'scss':        ['stylelint'],
\	'sugarcss':    ['stylelint'],
\	'stylus':      ['stylelint'],
\	'vim':         ['vint']
\}
let g:ale_pattern_options_enabled = 1
let g:ale_pattern_options = {
\   '\.min\.js$': {'ale_linters': [], 'ale_fixers': []},
\   '\.min\.css$': {'ale_linters': [], 'ale_fixers': []},
\}
let g:ale_list_window_size = 5

" let g:ale_fix_on_save = 1

" Comfortable Motion | Smooth Scrolling in Vim (Unused) {{{1

" Advanced options
" let g:comfortable_motion_friction = 80.0
" let g:comfortable_motion_air_drag = 2.0
" Smooth Mouse Scrolling (If mouse support is available)
" noremap <silent> <ScrollWheelDown> :call comfortable_motion#flick(40)<CR>
" noremap <silent> <ScrollWheelUp>   :call comfortable_motion#flick(-40)<CR>
" nnn.vim | CLI File Manager inside Vim (Unused){{{1

" let g:nnn#set_default_mappings = 0
" nnoremap <Leader>n :NnnPicker '%:p:h'<CR>
" let g:nnn#layout = 'new' " or vnew, tabnew etc.
" let g:nnn#layout = { 'left': '~20%' }
" let g:nnn#command = 'nnn'

" NERDTree | File Browser (Unused){{{1
"

" Automatically opens NERDTree if no files specified
autocmd StdinReadPre * let s:std_in=1
"autocmd VimEnter * if argc() == 0 && !exists("s:std_in") | NERDTree | endif
map <Leader>N :NERDTreeToggle<CR>
"map <C-o> :NERDTreeToggle<CR>
let NERDTreeShowHidden=1
let NERDTreeMinimalUI=1
let NERDTreeIgnore=['\.pyc', '\~$', '\.swo$', '\.swp$', '\.git', '\.hg', '\.svn', '\.bzr', '^.DS_Store$']

let g:NERDTreeDirArrowExpandable = ''
let g:NERDTreeDirArrowCollapsible = ''
" let g:NERDTreeDirArrowExpandable = ''
" let g:NERDTreeDirArrowCollapsible = ''

let g:NERDTreeIndicatorMapCustom = {
	\ "Modified"  : "✹",
	\ "Staged"    : "✚",
	\ "Untracked" : "✭",
	\ "Renamed"   : "➜",
	\ "Unmerged"  : "═",
	\ "Deleted"   : "✖",
	\ "Dirty"     : "✗",
	\ "Clean"     : "✔︎",
	\ 'Ignored'   : '☒',
	\ "Unknown"   : "?"
	\ }
let g:NERDTreeShowIgnoredStatus = 1
let g:NERDTreeHighlightCursorline = 1

let g:NERDTreeHighlightFolders = 1 " enables folder icon highlighting using exact match
let g:NERDTreeHighlightFoldersFullName = 1 " highlights the folder name
let g:NERDTreeLimitedSyntax = 1

let g:WebDevIconsNerdTreeGitPluginForceVAlign = 1

" Automaticaly close nvim if NERDTree is only thing left open
autocmd bufenter * if (winnr("$") == 1 && exists("b:NERDTree") && b:NERDTree.isTabTree()) | q | endif

" vim:foldmethod=marker:foldlevel=0

" defx | File Browser (Unused){{{1
"
"
" map <silent> <Leader>n :Defx `getcwd()`<CR>

" wintabs | Buffer and tab management (Unused) {{{1

" map <silent> tk <Plug>(wintabs_next)
" map <silent> tj <Plug>(wintabs_previous)
" map <silent> td <Plug>(wintabs_close)
" map <silent> tu <Plug>(wintabs_undo)
" map <silent> to <Plug>(wintabs_only)

" let g:wintabs_ui_modified= ' ●'
" let g:wintabs_ui_readonly= ' '
" let g:wintabs_ui_sep_leftmost= ' '
" let g:wintabs_ui_sep_inbetween= '│'
" let g:wintabs_ui_sep_rightmost= ' '


" Lightline | vim+tmux Status and shell prompt customization (Unused) {{{1

" Vim Status | Reload Vimrc to apply customization

try

let g:powerline_symbols = {}
if get(g:, 'lightline_powerline', 1)
	let g:powerline_symbols.separator    = { 'left': "", 'right': "" }
	let g:powerline_symbols.subseparator = { 'left': "│", 'right': "│" }
	let g:powerline_symbols.linenr       = ""
	let g:powerline_symbols.branch       = "\ue0a0 "
	let g:powerline_symbols.readonly     = "\ue0a2"
	let g:powerline_symbols.clipboard    = " ©"
else
	let g:powerline_symbols.separator    = { 'left': '', 'right': '' }
	let g:powerline_symbols.subseparator = { 'left': '│', 'right': '│' }
	let g:powerline_symbols.linenr       = ''
	let g:powerline_symbols.branch       = ''
	let g:powerline_symbols.readonly     = 'RO'
	let g:powerline_symbols.clipboard    = ' @'
endif

let g:lightline#ale#indicator_checking = "\uf110 "
let g:lightline#ale#indicator_warnings = "\uf071  "
let g:lightline#ale#indicator_errors = "\uf05e  "
let g:lightline#ale#indicator_ok = "\uf00c "

" if get(g:, 'lightline_powerline', 1)
"     let g:powerline_symbols.separator    = { 'left': "\ue0b8", 'right': "\ue0ba" }
"     let g:powerline_symbols.subseparator = { 'left': "\ue0b9", 'right': "\ue0bb" }
"     let g:powerline_symbols.linenr       = "\ue0a1"
"     let g:powerline_symbols.branch       = "\ue0a0 "
"     let g:powerline_symbols.readonly     = "\ue0a2"
"     let g:powerline_symbols.clipboard    = " ©"
" else
"     let g:powerline_symbols.separator    = { 'left': '', 'right': '' }
"     let g:powerline_symbols.subseparator = { 'left': '|', 'right': '|' }
"     let g:powerline_symbols.linenr       = ''
"     let g:powerline_symbols.branch       = ''
"     let g:powerline_symbols.readonly     = 'RO'
"     let g:powerline_symbols.clipboard    = ' @'
" endif

if get(g:, 'lightline_set_noshowmode', 1)
	set noshowmode
endif

let g:lightline#bufferline#unicode_symbols   = get(g:, 'lightline_powerline', 0)
let g:lightline#bufferline#filename_modifier = ':t'
let g:lightline#bufferline#show_number       = 1
let g:lightline#bufferline#shorten_path      = 1
let g:lightline#bufferline#unnamed = '[No Name]'

let g:lightline = {
	\ 'colorscheme': 'wal',
	\ 'enable': {
	\ 'statusline': 1,
	\ 'tabline': 1,
	\ },
	\ 'tab': {
	\   'active':   ['tabnum', 'readonly', 'filename', 'modified'],
	\   'inactive': ['tabnum', 'readonly', 'filename', 'modified']
	\ },
	\ 'mode_map': { 'c': 'NORMAL' },
	\ 'active': {
	\   'left': [ [ 'mode', 'paste' ], [ 'fugitive', 'filename' ] ],
	\   'right': [ ['currentfunction'], [ 'lineinfo' ], ['percent'], [ 'fileformat', 'fileencoding', 'spaces', 'filetype' ], [ 'linter_checking', 'linter_errors', 'linter_warnings', 'linter_ok' ], [ 'gitstatus' ]  ]
	\ },
	\ 'inactive': {
	\   'left':  [['inactivefilename']],
	\   'right': [['fileformat', 'fileencoding', 'filetype']]
	\ },
	\ 'component_function': {
	\   'tablabel':         'LightlineTabLabel',
	\   'mode':             'LightlineModeAndClipboard',
	\   'fugitive':         'LightlineFugitive',
	\   'filename':         'LightlineFilename',
	\   'inactivefilename': 'LightlineInactiveFilename',
	\   'lineinfo':         'LightlineLineinfo',
	\   'percent':          'LightlinePercent',
	\   'fileformat':       'LightlineFileformat',
	\   'fileencoding':     'LightlineFileencoding',
	\   'filetype':         'LightlineFiletype',
	\   'spaces':           'LightlineTabsOrSpacesStatus',
	\   'gitstatus':        'LightlineGitStatus',
	\   'cocstatus':        'coc#status',
	\   'currentfunction':  'CocCurrentFunction'
	\ },
	\ 'component_expand': {
	\  'linter_checking': 'lightline#ale#checking',
	\  'linter_warnings': 'lightline#ale#warnings',
	\  'linter_errors': 'lightline#ale#errors',
	\  'linter_ok': 'lightline#ale#ok',
	\ },
	\ 'component_type': {
	\     'linter_checking': 'left',
	\     'linter_warnings': 'warning',
	\     'linter_errors': 'error',
	\     'linter_ok': 'left',
	\ },
	\ 'tab_component_function': {
	\   'tabnum':   'LightlineTabnum',
	\   'filename': 'LightlineTabFilename',
	\   'readonly': 'LightlineTabReadonly',
	\ },
	\ 'separator': g:powerline_symbols.separator,
	\ 'subseparator': g:powerline_symbols.subseparator,
	\ }

let s:filename_modes = {
	\ 'ControlP':             'CtrlP',
	\ '__Tagbar__':           'Tagbar',
	\ '__Gundo__':            'Gundo',
	\ '__Gundo_Preview__':    'Gundo Preview',
	\ '[BufExplorer]':        'BufExplorer',
	\ 'NERD_tree':            'NERDTree',
	\ 'NERD_tree_1':          'NERDTree',
	\ '[Command Line]':       'Command Line',
	\ '[Plugins]':            'Plugins',
	\ '__committia_status__': 'Committia Status',
	\ '__committia_diff__':   'Committia Diff',
	\ }

let s:filetype_modes = {
	\ 'netrw':         'NetrwTree',
	\ 'nerdtree':      'NERDTree',
	\ 'startify':      'Startify',
	\ 'vim-plug':      'Plug',
	\ 'unite':         'Unite',
	\ 'vimfiler':      'VimFiler',
	\ 'vimshell':      'VimShell',
	\ 'help':          'Help',
	\ 'qf':            'Quickfix',
	\ 'godoc':         'GoDoc',
	\ 'gedoc':         'GeDoc',
	\ 'gitcommit':     'Commit Message',
	\ 'fugitiveblame': 'FugitiveBlame',
	\ 'agit':          'Agit',
	\ 'agit_diff':     'Agit',
	\ 'agit_stat':     'Agit',
	\ }

let s:short_modes = {
	\ 'NORMAL':   'N',
	\ 'INSERT':   'I',
	\ 'VISUAL':   'V',
	\ 'V-LINE':   'L',
	\ 'V-BLOCK':  'B',
	\ 'COMMAND':  'C',
	\ 'SELECT':   'S',
	\ 'S-LINE':   'S-L',
	\ 'S-BLOCK':  'S-B',
	\ 'TERMINAL': 'T',
	\ }

function! LightlineWinWidth() abort
	return winwidth(0)
endfunction

function! LightlineDisplayFilename() abort
	if LightlineWinWidth() >= 50 && &filetype =~? 'help\|gedoc'
		return 1
	endif
	return LightlineDisplayFileinfo()
endfunction

function! LightlineDisplayFileinfo() abort
	if LightlineWinWidth() < 50 || expand('%:t') =~? '^NrrwRgn' || has_key(s:filename_modes, expand('%:t')) || has_key(s:filetype_modes, &filetype)
		return 0
	endif
	return 1
endfunction

function! LightlineDisplayLineinfo() abort
	if LightlineWinWidth() >= 50 && &filetype =~? 'help\|qf\|godoc\|gedoc'
		return 1
	endif
	return LightlineDisplayFileinfo()
endfunction

function! LightlineModified() abort
	return &ft =~ 'help\|vimfiler\|gundo' ? '' : &modified ? '●' : &modifiable ? '' : '-'
endfunction

function! LightlineReadonly() abort
	return &ft !~? 'help\|vimfiler\|gundo' && &readonly ? '' : ''
endfunction

function! LightlineClipboard() abort
	return match(&clipboard, 'unnamed') > -1 ? g:powerline_symbols.clipboard : ''
endfunction

function! LightlineShortMode(mode) abort
	if LightlineWinWidth() > 75
		return a:mode
	endif
	return get(s:short_modes, a:mode, a:mode)
endfunction

function! LightlineMode() abort
	let fname = expand('%:t')
	if fname =~? '^NrrwRgn' && exists('b:nrrw_instn')
		return printf('%s#%d', 'NrrwRgn', b:nrrw_instn)
	endif
	return get(s:filename_modes, fname, get(s:filetype_modes, &filetype, LightlineShortMode(lightline#mode())))
endfunction
" function! LightlineMode()
"     return winwidth(0) > 60 ? lightline#mode() : ''
" endfunction

function! LightlineModeAndClipboard() abort
	return LightlineMode() . LightlineClipboard()
endfunction

function! LightlineTabnum(n) abort
	return printf('%d', a:n)
endfunction

function! LightlineTabLabel() abort
	return 'Tabs'
endfunction

function! LightlineTabReadonly(n) abort
	let winnr = tabpagewinnr(a:n)
	return gettabwinvar(a:n, winnr, '&readonly') ? g:powerline_symbols.readonly : ''
endfunction

function! LightlineTabFilename(n) abort
	let bufnr = tabpagebuflist(a:n)[tabpagewinnr(a:n) - 1]
	let bufname = expand('#' . bufnr . ':t')
	let buffullname = expand('#' . bufnr . ':p')
	let bufnrs = filter(range(1, bufnr('$')), 'v:val != bufnr && len(bufname(v:val)) && bufexists(v:val) && buflisted(v:val)')
	let i = index(map(copy(bufnrs), 'expand("#" . v:val . ":t")'), bufname)
	let ft = gettabwinvar(a:n, tabpagewinnr(a:n), '&ft')
	if strlen(bufname) && i >= 0 && map(bufnrs, 'expand("#" . v:val . ":p")')[i] != buffullname
		let fname = substitute(buffullname, '.*/\([^/]\+/\)', '\1', '')
	else
		let fname = bufname
	endif
	return fname =~# '^\[preview' ? 'Preview' : get(s:filename_modes, fname, get(s:filetype_modes, ft, fname))
endfunction

function! LightlineFugitive() abort
	if LightlineDisplayFileinfo() && LightlineWinWidth() > 100 && exists('*fugitive#head')
		let mark = g:powerline_symbols.branch
		try
			let branch = fugitive#head()
			if strlen(branch) > 30
				let branch = strcharpart(branch, 0, 20) . '...'
			endif
			return mark . branch
		catch
		endtry
	endif
	return ''
endfunction

function! LightlineGitStatus() abort
	let gitstatus = get(g:, 'coc_git_status', '')
	return winwidth(0) > 120 ? gitstatus : ''
endfunction
function! CocCurrentFunction()
	return get(b:, 'coc_current_function', '')
endfunction

function! LightlineAlternateFilename(fname) abort
    if a:fname ==# 'ControlP'
        return LightlineCtrlPMark()
    elseif a:fname ==# '__Tagbar__'
        return g:lightline.fname
    elseif a:fname =~ '__Gundo\|NERD_tree'
        return ''
    elseif a:fname =~? '^NrrwRgn'
        let bufname = (get(b:, 'orig_buf', 0) ? bufname(b:orig_buf) : substitute(bufname('%'), '^Nrrwrgn_\zs.*\ze_\d\+$', submatch(0), ''))
        return bufname
    elseif &filetype ==# 'qf'
        return get(w:, 'quickfix_title', a:fname)
    elseif &filetype ==# 'unite'
        return unite#get_status_string()
    elseif &filetype ==# 'vimfiler'
        return vimfiler#get_status_string()
    elseif &filetype ==# 'vimshell'
        return vimshell#get_status_string()
    endif
    return ''
endfunction

function! LightlineFilenameWithFlags(fname) abort
    if LightlineDisplayFilename()
        let str = (LightlineReadonly() != '' ? LightlineReadonly() . ' ' : '')
        if strlen(a:fname)
            let path = expand('%:~:.')
            if strlen(path) > 60
                let path = substitute(path, '\v\w\zs.{-}\ze(\\|/)', '', 'g')
            endif
            if strlen(path) > 60
                let path = a:fname
            endif
            let str .= path
        else
            let str .= '[No Name]'
        endif
        let str .= (LightlineModified() != '' ? ' ' . LightlineModified() : '')
        return str
    endif
    return ''
endfunction

function! LightlineFilename() abort
    let fname = expand('%:t')

    let str = LightlineAlternateFilename(fname)

    if strlen(str)
        return str
    endif

    return LightlineFilenameWithFlags(fname)
endfunction

function! LightlineInactiveFilename() abort
    let fname = expand('%:t')

    let str = LightlineAlternateFilename(fname)

    if strlen(str)
        return str
    endif

    let str = get(s:filename_modes, fname, get(s:filetype_modes, &filetype, ''))
    if strlen(str)
        if &filetype ==? 'help'
            let str .= ' ' .  expand('%:~:.')
        endif

        return str
    endif

    return LightlineFilenameWithFlags(fname)
endfunction

function! LightlineLineinfo() abort
    if LightlineDisplayLineinfo()
        return printf('%s%4d:%3d', g:powerline_symbols.linenr, line('.'), col('.'))
    endif
    return ''
endfunction

function! LightlinePercent() abort
    if LightlineDisplayLineinfo()
        return printf('%3d%%', line('.') * 100 / line('$'))
    endif
    return ''
endfunction

function! LightlineFileformat() abort
    return LightlineDisplayFileinfo() && &fileformat !=? 'unix' ? &fileformat : ''
endfunction

function! LightlineFileencoding() abort
    if LightlineDisplayFileinfo()
        let encoding = strlen(&fenc) ? &fenc : &enc
        if encoding !=? 'utf-8'
            return encoding
        endif
    endif
    return ''
endfunction

function! LightlineFiletype() abort
    return LightlineDisplayFileinfo() ? &filetype : ''
endfunction

function! LightlineTabsOrSpacesStatus() abort
    if LightlineDisplayFileinfo()
        let shiftwidth = exists('*shiftwidth') ? shiftwidth() : &shiftwidth
        return (&expandtab ? 'Spaces' : 'Tab') . ': ' . shiftwidth
    endif
    return ''
endfunction

catch
	echo 'Lightline not installed. It should work after running :PlugInstall'
endtry
" Shell Prompt | Type ':PromptlineSnapshot! ~/.dots/system/promptline' to reload customization

" To update theme, :PromptlineSnapshot! ~/.dots/system/.promptline
" Note: MB4 has not battery, if you're using MB4, comment battery slice.
" let g:promptline_theme = 'lightline'
" let g:promptline_powerline_symbols = 0
" let g:promptline_preset = {
"     \'a' : [ promptline#slices#user() ],
"     \'c' : [ promptline#slices#cwd() ],
"     \'y' : [ promptline#slices#vcs_branch() ],
"     \'z' : [ promptline#slices#battery() ],
"     \'warn' : [ promptline#slices#last_exit_code() ]}
" let g:promptline_symbols = {
"     \ 'left'       : '',
"     \ 'left_alt'   : '│',
"     \ 'dir_sep'    : ' / ',
"     \ 'truncation' : '…',
"     \ 'vcs_branch' : '',
"     \ 'space'      : ' '}

"" Tmux / Tmuxline.vim" | Type ':Tmuxline' to preview, type ':TmuxlineSnapshot! ~/.dots/system/promptline' to reload
" Note: In long term, status utf8 errors may disturb you. After you saved your
" customization, delete this line.

" let g:tmuxline_theme = 'lightline'
" let g:tmuxline_separators = {
"     \ 'left' : '',
"     \ 'left_alt': '│',
"     \ 'right' : '',
"     \ 'right_alt' : '│',
"     \ 'space' : ' '}
" " #I => Window Number
" " #W => Window Name
" " #S => Session Name
" " #H => Local Name
" let g:tmuxline_preset = {
" 	\'a'    : '#([[ "$(uname)" == "Linux" ]] && echo "   "; [[ "$(uname)" == "Darwin" ]] && echo "   " )',
"     \'win'  : '#W',
"     \'cwin' : ['#W#F'],
" 	\'x'    : ["⚡ #(battery-level)  #(uptime | awk '{print $3}'|sed 's/,//')"],
"     \'y'    : ['ʷ%W %a %d/%m  %I:%M'],
"     \'z'    : '  #H'}
" Note: Delete battery-level if you don't have battery.

if has('win32')
	let g:sqlite_clib_path = 'C:/Users/ege_e/.extra/win/nvim-dep/sqlite-dll-win-x64-3440200/sqlite3.dll'
endif
