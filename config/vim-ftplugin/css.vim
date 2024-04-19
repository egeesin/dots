" setlocal iskeyword+=-
" setlocal foldmethod=marker
" setlocal foldmarker={,}

" {rtp}/fold/css-fold.vim
" [-- local settings --]               {{{1
setlocal foldexpr=CssFold(v:lnum)
setlocal foldtext=CssFoldText()

let b:width1 = 20
let b:width2 = 15

nnoremap <buffer> + :let b:width2+=1<cr><c-l>
nnoremap <buffer> - :let b:width2-=1<cr><c-l>

" [-- global definitions --]           {{{1
if exists('*CssFold')
	setlocal foldmethod=expr
	" finish
endif

function! CssFold(lnum)
	let cline = getline(a:lnum)
	if     cline =~ '{\s*$'
		return 'a1'
	elseif cline =~ '}\s*$'
		return 's1'
	else
		return '='
	endif
endfunction

function! s:Complete(txt, width)
	let length = strlen(a:txt)
	if length > a:width
		return a:txt
	endif
	return a:txt . repeat(' ', a:width - length)
endfunction

function! CssFoldText()
	let lnum = v:foldstart
	let txt = s:Complete(getline(lnum), b:width1)
	let lnum += 1
	while lnum < v:foldend
		let add = s:Complete(substitute(getline(lnum), '^\s*\(\S\+\)\s*:\s*\(.\{-}\)\s*;\s*$', '\1: \2;', ''), b:width2)
		if add !~ '^\s*$'
			let txt .= ' ' . add
		endif

		let lnum += 1
	endwhile
	return txt. '}'
endfunction
