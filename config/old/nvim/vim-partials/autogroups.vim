" ======= Autogroups & GUI Settings


augroup configgroup
	autocmd!
	au VimEnter * highlight clear SignColumn
	au BufEnter *.cls setlocal filetype=java
	au BufEnter *.zsh-theme setlocal filetype=zsh
    au BufRead,BufNewFile *mutt-* setfiletype mail
	au BufEnter *i3/config setlocal filetype=i3
augroup END

" Save pointer location between sessions.
if has("autocmd")
  au BufReadPost * if line("'\"") > 1 && line("'\"") <= line("$") | exe "normal! g'\"" | endif
endif


if has('gui_running')
	" let s:uname = system("uname")
 "    if s:uname == "Darwin\n"
	" 	set guifont=CommitMono\ Nerd\ Font:h15
 "    endif
	" set guifont=CommitMono\ Nerd\ Font:h14
	set guifont=CommitMono\ Nerd\ Font:#e-antialias:h12
	" set guifont=Iosevka\ Aegean:h14
	set guioptions-=T  "remove menu bar
	set guicursor+=a:block-blinkon0      " Use non-blinking block cursor.

	let g:neovide_padding_top = 4
	let g:neovide_padding_bottom = 4
	let g:neovide_padding_right = 16
	let g:neovide_padding_left = 16

	set linespace=4

	let g:neovide_refresh_rate = 24
	let g:neovide_refresh_rate_idle = 5

	set guioptions-=e " Use showtabline in gui vim (This is coming from tabline.nvim docs)
endif

lua << EOF
if vim.g.neovide then
	vim.keymap.set('n', '<C-S-s>', ':w<CR>') -- Save
	vim.keymap.set('v', '<C-S-c>', '"+y') -- Copy
	vim.keymap.set('n', '<C-S-v>', '"+P') -- Paste normal mode
	vim.keymap.set('v', '<C-S-v>', '"+P') -- Paste visual mode
	vim.keymap.set('c', '<C-S-v>', '<C-R>+') -- Paste command mode
	vim.keymap.set('i', '<C-S-v>', '<ESC>l"+Pli') -- Paste insert mode
end

vim.api.nvim_set_keymap('', '<C-S-v>', '+p<CR>', { noremap = true, silent = true})
vim.api.nvim_set_keymap('!', '<C-S-v>', '<C-R>+', { noremap = true, silent = true})
vim.api.nvim_set_keymap('t', '<C-S-v>', '<C-R>+', { noremap = true, silent = true})
vim.api.nvim_set_keymap('v', '<C-S-v>', '<C-R>+', { noremap = true, silent = true})
EOF

" Dynamically Change The Scale At Runtime (Neovide)
let g:neovide_scale_factor=1.0
function! ChangeScaleFactor(delta)
  let g:neovide_scale_factor = g:neovide_scale_factor * a:delta
endfunction
nnoremap <expr><C-=> ChangeScaleFactor(1.25)
nnoremap <expr><C--> ChangeScaleFactor(1/1.25)

if ! has('gui_running') && has('gui_vimr')
    set ttimeoutlen=10
    augroup FastEscape
        autocmd!
        au InsertEnter * set timeoutlen=0
        au InsertLeave * set timeoutlen=1000
    augroup END
	inoremap <silent> <S-Insert> <Esc>"*p`]a
	inoremap <silent> <M-v> <Esc>"+p`]a
endif


" Mksession with relative paths

function! MakeSession()
	let b:sessiondir = getcwd()
	let b:filename = b:sessiondir . '/session.vim'
	exe "mksession! " . b:filename
	exe "edit! " . b:filename
	exe "g:^cd :d"
	exe "x"
endfunction


function! DeleteHiddenBuffers ()
    let tpbl=[]
    call map(range(1, tabpagenr('$')), 'extend(tpbl, tabpagebuflist(v:val))')
    for buf in filter(range(1, bufnr('$')), 'bufexists(v:val) && index(tpbl, v:val)==-1')
        silent execute 'bwipeout' buf
    endfor
endfunction

function! ClearRegisters()
    let regs='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789/-="*+'
    let i=0
    while (i<strlen(regs))
        exec 'let @'.regs[i].'=""'
        let i=i+1
    endwhile
endfunction

command! ClearRegisters call ClearRegisters()


