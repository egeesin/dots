" ======= Colorscheme

if has('syntax') && !exists('g:syntax_on')
	syntax enable " Enable syntax highlighting if it exists
endif

if has("termguicolors")
	set termguicolors " Enable 24-bit RGB colors
endif

try
	let g:selenized_variant = 'bw'
	colorscheme selenized
	" colorscheme wal
catch
	colorscheme blue
endtry

" hi Normal guibg=none ctermbg=none
" hi NonText guibg=none ctermbg=none
" hi! LineNr ctermbg=none guibg=none
"
" hi TabLine      ctermfg=White ctermbg=none cterm=none guibg=none
" hi TabLineFill  ctermfg=White ctermbg=none cterm=none guibg=none
" hi TabLineSel   ctermfg=Black ctermbg=DarkBlue cterm=none guibg=none

" hi! EndOfBuffer ctermbg=none ctermfg=none
" hi VertSplit ctermbg=Gray guibg=Gray ctermfg=Black guifg=Black
"
" set fillchars+=vert:│
" hi StatusLine   ctermbg=none
" hi StatusLineNC ctermbg=none
" hi WildMenu guibg=NONE ctermbg=NONE ctermfg=White
" hi! Conceal ctermbg=none guibg=none
" hi FoldColumn ctermbg=none guibg=none


" if has("mac") || has("macunix") || has("gui_macvim")
lua << EOF
local function change_background()
	local m = vim.fn.system("defaults read -g AppleInterfaceStyle")
	m = m:gsub("%s+", "") -- trim whitespace
	if m == "Dark" then
		vim.o.background = "dark"
	else
		-- vim.o.background = "light"
	end
end
change_background()
EOF
" endif

" --------- Below is unused

" hi VertSplit ctermbg=none guibg=none ctermfg=gray guifg=gray
" hi VertSplit cterm=reverse
" hi Visual       ctermfg=White  ctermbg=none
" hi User1 ctermbg=none
" hi User2 ctermbg=none
" hi User3 ctermbg=none
" hi User4 ctermbg=none
" hi User5 ctermbg=none
" hi User6 ctermbg=none
" hi User7 ctermbg=none
" hi User8 ctermbg=none

" highlight GitGutterAdd    guifg=#009900 guibg=none ctermfg=2 ctermbg=none
" highlight GitGutterChange guifg=#bbbb00 guibg=none ctermfg=3 ctermbg=none
" highlight GitGutterDelete guifg=#ff2222 guibg=none ctermfg=1 ctermbg=none

" au Colorscheme * hi! link Conceal Number
" au Colorscheme * hi! link LineNr Normal
" au Colorscheme * hi link FoldColumn Normal
" hi TabLine ctermbg=none guibg=none
