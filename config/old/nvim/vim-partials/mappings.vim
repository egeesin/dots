" ======= Mappings
" Tip: Type ':map' to see all mappings. ':nmap' for normal mode,
" ':imap' for insert mode etc...

" Leader {{{1

let mapleader = "\<space>"
" let maplocalleader = "\<space>"
" https://www.reddit.com/r/vim/comments/39jtib/what_is_the_difference_between_mapleader_and/
"
" NOTE: Must happen before plugins are required (otherwise wrong leader will be used)

nnoremap <Space> <Nop>

" General {{{1

" Movement
nmap H ^
nmap L $

" Cursor Highlight

" set cursorline                " highlight current line
" set cursorcolumn              " highlight current column
" hi CursorLine   cterm=NONE ctermbg=darkred ctermfg=white guibg=darkred guifg=white
" hi CursorColumn cterm=NONE ctermbg=darkred ctermfg=white guibg=darkred guifg=white
" Note: Toggle <Leader>c(olumn)
nnoremap <leader>c :set cursorcolumn!<CR>

" Exit from Terminal Mode with ESC
tnoremap <Esc> <C-\><C-n>

" Semi-colon is also colon.
" nnoremap ; :
" vnoremap ; :
" Note: This is not good idea since ;'s default behaviour is repeat 'f' 'F'
" things.

" Easy S&R shortcuts
" noremap <leader>/ :%s###g<Left><Left><Left> # Easy delete
" noremap "' :%s###gn<Left><Left><Left><Left>

" fzf.vim shortcuts
nmap <leader>f :Files<CR>
nmap <leader>b :Buffers<CR>

" Browse search history in Command Mode without arrow keys
cnoremap <C-N> <Down>
cnoremap <C-P> <Up>

" Don't copy the contents of an overwritten selection.
vnoremap p "_dP

" Allows you to save files you opened without write permissions via sudo
" cmap w!! w !sudo tee %
cmap w!! w suda://%

" quickly close quickfix
map <silent><Leader>C :ccl<CR><CR>

" nnoremap <space> za

" Move lines in Visual Mode
vnoremap J :m '>+1<CR>gv=gv
vnoremap K :m '<-2<CR>gv=gv

" Insert new line without entering insert mode (keeping cursor position)
" inoremap <C-j> <Esc>m`o<Esc>``i
" inoremap <C-k> <Esc>m`O<Esc>``i

" Unfortunately, the rebind below doesn't working because it conflicts with
" tmux-friendly pane focusing bindings. I will put it Normal version here just
" in case...
" nnoremap <C-J> m`o<Esc>``
" nnoremap <C-K> m`O<Esc>``

" Move cursor vertically by visual line
" nnoremap j gj
" nnoremap k gk
" nnoremap gV `[v`]

" Buffer/Tab Management {{{1
"
" nnoremap <silent> TT :tabnew<CR>
" nnoremap <silent> TK :tabnext<CR>
" nnoremap <silent> TJ :tabprev<CR>
" nnoremap <silent> TD :tabclose<CR>

nnoremap <leader>tk :BufferLineCycleNext<CR>
nnoremap <leader>tj :BufferLineCyclePrev<CR>
" nnoremap <leader>tk :bnext<CR>
" nnoremap <leader>tj :bprev<CR>
nnoremap <leader>tl :BufferLineMoveNext<CR>
nnoremap <leader>th :BufferLineMovePrev<CR>
" nnoremap <leader>tt :BufferLinePick<CR>
nnoremap <leader>gt :BufferLinePick<CR>
nnoremap <leader>tp :BufferLineTogglePin<CR>

" nnoremap <leader>dt :BufferLinePickClose<CR>
nnoremap <leader>td :bdelete<CR>

nnoremap <leader>t1 <cmd>lua require("bufferline").go_to(1, true)<cr>
nnoremap <leader>t2 <cmd>lua require("bufferline").go_to(2, true)<cr>
nnoremap <leader>t3 <cmd>lua require("bufferline").go_to(3, true)<cr>
nnoremap <leader>t4 <cmd>lua require("bufferline").go_to(4, true)<cr>
nnoremap <leader>t5 <cmd>lua require("bufferline").go_to(5, true)<cr>
nnoremap <leader>t6 <cmd>lua require("bufferline").go_to(6, true)<cr>
nnoremap <leader>t7 <cmd>lua require("bufferline").go_to(7, true)<cr>
nnoremap <leader>t8 <cmd>lua require("bufferline").go_to(8, true)<cr>
nnoremap <leader>t9 <cmd>lua require("bufferline").go_to(9, true)<cr>
nnoremap <leader>t$ <cmd>lua require("bufferline").go_to(-1, true)<cr>

" nnoremap <silent> BK :TablineBufferNext<CR>
" nnoremap <silent> BJ :TablineBufferPrev<CR>

" nnoremap <silent> BN :tabnew<CR>
" nnoremap <silent> BD :tabclose<CR>

" nnoremap <silent> th :tabfirst<CR>
" nnoremap <silent> tl :tablast<CR>
" nnoremap <silent> tm :tabm<Space>

" Pane Management {{{1
"
" Splitting
nnoremap <silent> \\ <C-w>v
nnoremap <silent> -- <C-w>s
" Splitting but for opening terminals
nnoremap <silent> <Leader>\ :vnew term://zsh<CR>
nnoremap <silent> <Leader>+ :split term://zsh<CR>
" Resizing
nnoremap <silent> <Leader>= :exe "resize " . (winheight(0) * 3/2)<CR>
nnoremap <silent> <Leader>- :exe "resize " . (winheight(0) * 2/3)<CR>
nnoremap <silent> <Leader>> :exe "vertical resize " . (winwidth(0) * 3/2)<CR>
nnoremap <silent> <Leader>< :exe "vertical resize " . (winwidth(0) * 2/3)<CR>

" Focusing | Requirements vim-tmux-navigator (Recommended)
let g:tmux_navigator_no_mappings = 1
nnoremap <silent> <C-h> :TmuxNavigateLeft<cr>
nnoremap <silent> <C-j> :TmuxNavigateDown<cr>
nnoremap <silent> <C-k> :TmuxNavigateUp<cr>
nnoremap <silent> <C-l> :TmuxNavigateRight<cr>
nnoremap <silent> <C-\> :TmuxNavigatePrevious<cr>

" Focusing without Tmux
"nnoremap <C-j> <C-W><C-j>
"nnoremap <C-k> <C-W><C-k>
"nnoremap <C-l> <C-W><C-l>
"nnoremap <C-h> <C-W><C-h>

nmap <leader>u <cmd>Telescope undo<cr>

" Modeline Generator {{{1
" Append modeline after last line in buffer.
" Use substitute() instead of printf() to handle '%%s' modeline in LaTeX
" files.
function! AppendModeline()
  let l:modeline = printf(" vim: set ts=%d sw=%d tw=%d %set :",
        \ &tabstop, &shiftwidth, &textwidth, &expandtab ? '' : 'no')
  let l:modeline = substitute(&commentstring, "%s", l:modeline, "")
  call append(line("$"), l:modeline)
endfunction
nnoremap <silent> <Leader>ml :call AppendModeline()<CR>
" }}}
