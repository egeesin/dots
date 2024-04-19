-- vim: set ft=lua:

-- All Lua-based Plugin Setups {{{1
require"Comment".setup() -- auto comment toggle
require"git".setup() -- git commands inside vim  (fugitive)
require"gitsigns".setup() -- git commands inside vim  (fugitive)
require"leap".add_default_mappings() -- leap - Easier movement with max 4 keystrokes

require"mason".setup() -- lsp manager
require"mason-lspconfig".setup{ -- bridge between mason and lspconfig
	ensure_installed = {
		"lua_ls",
		-- "biome",
		"bashls",
		-- "cssls",
		-- "stylelint_lsp",
		-- "unocss",
		-- "denols",
		-- "rust_analyzer",
		-- "wgsl_analyzer",
		-- "gdscript",
		-- "clangd",
		-- "jsonnet_ls"
		"tsserver",
		"html",
		"jsonls",
		"emmet_ls",
		"taplo",
		"yamlls",
		"vimls",
		"marksman",
		"sqlls"
	},
	automatic_installation = true,
}
local handlers = {
	function (server_name) -- default handler (optional)
		require"lspconfig"[server_name].setup {}
	end,
	-- Next, you can provide a dedicated handler for specific servers.
	-- For example, a handler override for the `rust_analyzer`:
	["lua_ls"] = function ()
		require"lspconfig".lua_ls.setup {
			settings = {
				Lua = {
					diagnostics = {
						globals = { "vim" }
					}
				}
			}
		}
	end,
	["rust_analyzer"] = function ()
		require"rust-tools".setup {}
	end,
}
-- Mason {{{1
require"mason-lspconfig".setup_handlers(handlers)

-- local null_ls = require"null-ls"
--
-- null_ls.setup({
-- 	sources = {
-- 		null_ls.builtins.formatting.stylua,
-- 		null_ls.builtins.diagnostics.eslint,
-- 		null_ls.builtins.completion.spell,
-- 	},
-- })


-- LSP Colors {{{1
require"lsp-colors".setup({
	Error = "#db4b4b",
	Warning = "#e0af68",
	Information = "#0db9d7",
	Hint = "#10B981"
})

-- nvim-lspconfig & default global mappings (Using mason-lspconfig instead) {{{ 1
-- Set up lspconfig.
-- local capabilities = require'cmp_nvim_lsp'.default_capabilities()
-- require'lspconfig'['<YOUR_LSP_SERVER>'].setup {
-- 	capabilities = capabilities
-- }

-- require'lspconfig'.eslint.setup{
-- 	on_attach = function(client, bufnr)
-- 		vim.api.nvim_create_autocmd("BufWritePre", {
-- 			buffer = bufnr,
-- 			command = "EslintFixAll",
-- 		})
-- 	end,
-- }
-- require'lspconfig'.theme_check.setup {
	-- cmd = { "theme-check-language-server", "--stdio" }
	-- cmd = { 'theme-check-liquid-server' }
-- }

-- Global mappings.
-- See `:help vim.diagnostic.*` for documentation on any of the below functions
vim.keymap.set('n', '<space>e', vim.diagnostic.open_float)
vim.keymap.set('n', '[d', vim.diagnostic.goto_prev)
vim.keymap.set('n', ']d', vim.diagnostic.goto_next)
vim.keymap.set('n', '<space>q', vim.diagnostic.setloclist)

-- Use LspAttach autocommand to only map the following keys
-- after the language server attaches to the current buffer
vim.api.nvim_create_autocmd('LspAttach', {
group = vim.api.nvim_create_augroup('UserLspConfig', {}),
callback = function(ev)
	-- Enable completion triggered by <c-x><c-o>
	vim.bo[ev.buf].omnifunc = 'v:lua.vim.lsp.omnifunc'

	-- Buffer local mappings.
	-- See `:help vim.lsp.*` for documentation on any of the below functions
	local opts = { buffer = ev.buf }
	vim.keymap.set('n', 'gD', vim.lsp.buf.declaration, opts)
	vim.keymap.set('n', 'gd', vim.lsp.buf.definition, opts)
	vim.keymap.set('n', 'K', vim.lsp.buf.hover, opts)
	vim.keymap.set('n', 'gi', vim.lsp.buf.implementation, opts)
	-- vim.keymap.set('n', '<C-k>', vim.lsp.buf.signature_help, opts) -- Conflicting with Tmux+Vim shortcut
	vim.keymap.set('n', '<space>wa', vim.lsp.buf.add_workspace_folder, opts)
	vim.keymap.set('n', '<space>wr', vim.lsp.buf.remove_workspace_folder, opts)
	vim.keymap.set('n', '<space>wl', function()
	print(vim.inspect(vim.lsp.buf.list_workspace_folders()))
	end, opts)
	vim.keymap.set('n', '<space>D', vim.lsp.buf.type_definition, opts)
	vim.keymap.set('n', '<space>rn', vim.lsp.buf.rename, opts)
	vim.keymap.set({ 'n', 'v' }, '<space>ca', vim.lsp.buf.code_action, opts)
	vim.keymap.set('n', 'gr', vim.lsp.buf.references, opts)
	vim.keymap.set('n', '<space>f', function()
	vim.lsp.buf.format { async = true }
	end, opts)
end,
})

-- nvim-cmp | Autocompletion Plugin {{{1
-- Set up nvim-cmp.
local cmp = require'cmp'

-- cmp config for all filetypes
cmp.setup({
	preselect = cmp.PreselectMode.None,
	snippet = {
		-- REQUIRED - you must specify a snippet engine
		expand = function(args)
			-- vim.fn["vsnip#anonymous"](args.body) -- For `vsnip` users.
			require'luasnip'.lsp_expand(args.body) -- For `luasnip` users.
		end,
	},
	window = {
		-- completion = cmp.config.window.bordered(),
		-- documentation = cmp.config.window.bordered(),
	},
	mapping = cmp.mapping.preset.insert({
		['<C-b>'] = cmp.mapping.scroll_docs(-4),
		['<C-f>'] = cmp.mapping.scroll_docs(4),
		['<C-Space>'] = cmp.mapping.complete(),
		['<C-e>'] = cmp.mapping.abort(),
		-- ['<CR>'] = cmp.mapping.confirm({ select = true }),
		-- -- Accept currently selected item. Set `select` to `false` to only confirm explicitly selected items.
		["<CR>"] = cmp.mapping.confirm({
			behavior = cmp.ConfirmBehavior.Insert,
			select = false,
		}),
		["<Right>"] = cmp.mapping.confirm({
			behavior = cmp.ConfirmBehavior.Replace,
			select = true,
		}),
		["<Tab>"] = cmp.mapping(function(fallback)
			if require"luasnip".expand_or_jumpable() then
				require"luasnip".expand_or_jump()
			else
				fallback()
			end
		end, { "i", "s" }),
		["<S-Tab>"] = cmp.mapping(function(fallback)
			if require"luasnip".jumpable(-1) then
				require"luasnip".jump(-1)
			else
				fallback()
			end
		end, { "i", "s" }),
	}),
	sources = cmp.config.sources(
		{
			{ name = 'nvim_lsp' },
			-- { name = 'vsnip' }, -- For vsnip users.
			{ name = 'luasnip' }, -- For luasnip users.
		},
		{
			{ name = 'async_path' },
			-- { name = 'buffer' },
			{ name = 'treesitter' },
			{ name = 'buffer-lines' },
			{ name = 'zsh' },
			{ name = 'emoji' },
		}
	)
})

-- For gitcommit filetype only
cmp.setup.filetype('gitcommit', {
	sources = cmp.config.sources(
		{{ name = 'conventionalcommits' }},
		{{ name = 'buffer' }}
	)
})

-- For Command mode
for _, cmd_type in ipairs({':', '/', '?', '@'}) do
	cmp.setup.cmdline(cmd_type, {
		sources = {
		{ name = 'cmdline_history' },
		},
	})
end

-- For Command mode only (:)
-- Note: if you enabled `native_menu`, this won't work anymore.
cmp.setup.cmdline(':', {
	mapping = cmp.mapping.preset.cmdline(),
	sources = cmp.config.sources(
		-- {{ name = 'path' }},
		{{ name = 'fuzzy_path' }},
		{{
				name = 'cmdline',
				-- option = {
				-- 	ignore_cmds = { 'Man', '!' }
				-- }
			}
		}
	)
})

-- For Command mode search only (/)
cmp.setup.cmdline('/', {
	mapping = cmp.mapping.preset.cmdline(),
	sources = {
		{ name = 'fuzzy_buffer' },
		-- { name = 'buffer' }
	}
})

-- For "conf","config" filetypes
require'cmp'.setup.filetype({ 'conf', 'config' },
	{ sources = {
		{ name = 'fonts'},
		{ name = 'tmux' }
	} })

-- cmp Source Setups
require'cmp_zsh'.setup {
	zshrc = true,
	filetypes = { 'zsh' }
}
require'cmp_git'.setup()
-- default config: https://github.com/petertriho/cmp-git#config

-- nvim-treesitter {{{1

require'nvim-treesitter.configs'.setup {
	-- A list of parser names
	ensure_installed = {
		"c",
		"lua",
		"vim",
		"vimdoc",
		"query",
		"comment",
		"diff",
		"bash",
		-- "gdscript",
		"git_config",
		"gitattributes",
		-- "gitcommit",
		"gitignore",
		-- "glsl",
		-- "hlsl",
		"html",
		"jq",
		"json",
		"json5",
		"markdown",
		"markdown_inline",
		"toml",
		"yaml",
		"passwd",
		"php",
		"pug",
		"po",
		"regex",
		-- "wgsl",
		"todotxt"
	},

	-- Install parsers synchronously (only applied to `ensure_installed`)
	sync_install = true,

	-- Automatically install missing parsers when entering buffer
	-- Recommendation: set to false if you don't have `tree-sitter` CLI installed locally
	auto_install = false,

	-- List of parsers to ignore installing (for "all")
	-- ignore_install = { "javascript", "html", "css", "gdscript" },

	---- If you need to change the installation directory of the parsers (see -> Advanced Setup)
	-- parser_install_dir = "/some/path/to/store/parsers", -- Remember to run vim.opt.runtimepath:append("/some/path/to/store/parsers")!

	highlight = {
		enable = true,

		-- NOTE: these are the names of the parsers and not the filetype. (for example if you want to
		-- disable highlighting for the `tex` filetype, you need to include `latex` in this list as this is
		-- the name of the parser)
		-- list of language that will be disabled
		-- disable = { "c", "rust" },
		-- Or use a function for more flexibility, e.g. to disable slow treesitter highlight for large files
		disable = {"vim", "vimdoc", "lua"}, function(lang, buf)
			local max_filesize = 100 * 1024 -- 100 KB
			local ok, stats = pcall(vim.loop.fs_stat, vim.api.nvim_buf_get_name(buf))
			if ok and stats and stats.size > max_filesize then
				return true
			end
		end,

		-- Setting this to true will run `:h syntax` and tree-sitter at the same time.
		-- Set this to `true` if you depend on 'syntax' being enabled (like for indentation).
		-- Using this option may slow down your editor, and you may see some duplicate highlights.
		-- Instead of true it can also be a list of languages
		-- additional_vim_regex_highlighting = false,
		additional_vim_regex_highlighting = { "markdown" },
	},
}
--- lspkind.nvim | vscode-like pictograms for neovim lsp completion items
local lspkind = require'lspkind'
cmp.setup {
	formatting = {
		format = lspkind.cmp_format({
			mode = 'symbol_text', -- show only symbol annotations
			maxwidth = 50, -- prevent the popup from showing more than provided characters (e.g 50 will not show more than 50 characters)
			ellipsis_char = '…', -- when popup menu exceed maxwidth, the truncated part would show ellipsis_char instead (must define maxwidth first)
			-- The function below will be called before any actual modifications from lspkind
			-- so that you can provide more controls on popup customization. (See [#30](https://github.com/onsails/lspkind-nvim/pull/30))

			-- before = function (entry, vim_item)
			-- 	return vim_item
			-- end
		})
	}
}

-- nvim-autopairs {{{1
require"nvim-autopairs".setup {
	disable_filetype = { "TelescopePrompt" , "vim" },
	check_ts = true,
}
-- Check for autopairs with treesitter
local npairs = require"nvim-autopairs"
local Rule = require'nvim-autopairs.rule'

npairs.setup({
    check_ts = true,
    ts_config = {
        lua = {'string'},-- it will not add a pair on that treesitter node
        javascript = {'template_string'},
        java = false,-- don't check treesitter on java
    }
})

local ts_conds = require'nvim-autopairs.ts-conds'
-- press % => %% only while inside a comment or string
npairs.add_rules({
  Rule("%", "%", "lua")
    :with_pair(ts_conds.is_ts_node({'string','comment'})),
  Rule("$", "$", "lua")
    :with_pair(ts_conds.is_not_ts_node({'function'}))
})

-- Autopairs Completion Integration
local cmp_autopairs = require"nvim-autopairs.completion.cmp"
cmp.event:on("confirm_done", cmp_autopairs.on_confirm_done())


-- nvim-tree.lua | File Browser {{{1

-- disable netrw at the very start of your init.lua
vim.g.loaded_netrw = 1
vim.g.loaded_netrwPlugin = 1

-- set termguicolors to enable highlight groups
-- vim.opt.termguicolors = true

-- nvim-tree Functions
local function my_on_attach(bufnr)
	local api = require"nvim-tree.api"

	local function opts(desc)
		return { desc = "nvim-tree: " .. desc, buffer = bufnr, noremap = true, silent = true, nowait = true }
	end

	local function change_root_to_global_cwd()
		local api = require"nvim-tree.api"
		local global_cwd = vim.fn.getcwd(-1, -1)
		api.tree.change_root(global_cwd)
	end

	-- default mappings
	api.config.mappings.default_on_attach(bufnr)
	-- custom mappings
	vim.keymap.set('n', '<C-t>', api.tree.change_root_to_parent,        opts('Up'))
	vim.keymap.set('n', '?',     api.tree.toggle_help,                  opts('Help'))
	vim.keymap.set('n', '<C-c>', change_root_to_global_cwd, opts('Change Root To Global CWD'))
end
-- nvim-tree Setup
require"nvim-tree".setup({
	sort_by = "case_sensitive",
	sync_root_with_cwd = true,
	view = {
		width = 32,
	},
	actions = {
		expand_all = {
			exclude = { ".git", "target", "build", "dist", "vendor", }
		}
	},
	renderer = {
		-- highlight_git = true,
		group_empty = true,
		indent_markers = {
			enable = true
		},
		icons = {
			-- git_placement = 'sign_column',
			show = {
				folder = false,
				folder_arrow = false
			},
			glyphs = {
				symlink = '',
				bookmark = '◉',
				folder = {
					default = '',
					open = '',
					symlink = '',
					symlink_open = "",
					-- arrow_closed = "",
					-- arrow_open = "",
					empty = "",
					empty_open = "",
				},
				git = {
					unstaged = "󰲶",
					-- staged = "",
					staged = "",
					unmerged = "",
					-- renamed = "",
					renamed = "",
					-- untracked = "",
					-- untracked = "",
					untracked = "󰫣",
					deleted = "",
					ignored = "",
				}
			}
		},
		special_files = { "Cargo.toml", "Makefile", "README.md", "readme.md" },
	},
	filters = {
		dotfiles = true,
		custom = { "^.git$", "*.png$", "*.webp$", "*.jpg$", "*.jpeg$", "*.avif$", "*.jxl$", "*.gif$", "*.scap$" }
	},
	update_focused_file = {
		enable = true,
		update_root = true,
		ignore_list = {}
	},
	diagnostics = {
		enable = true,
		show_on_dirs = true,
	},
	on_attach = my_on_attach
})

-- lualine.nvim - Status Line Configuration {{{1

local indent = {
    function()
        local style = vim.bo.expandtab and "Spaces" or "Tab"
        local size = vim.bo.expandtab and vim.bo.tabstop or vim.bo.shiftwidth
        return style .. ": " .. size
    end,
    cond = function()
        return vim.bo.filetype ~= ""
    end,
}

require"lualine".setup { -- lualine - Status Line Customization
	options = {
		theme = "auto",
		icons_enabled = "true",
		section_separators = '',
		component_separators = '',
		extensions = {
			'quickfix',
			'nvim-tree',
			'nvim-dap-ui',
			'man',
			'fzf',
			'trouble',
			'fugitive',
		},
		disabled_filetypes = { 'NvimTree' }
	},
	sections = {
		lualine_x = { indent, 'encoding', 'fileformat', 'filetype' }
	},
	-- tabline = {
	-- 	lualine_a = {},
	-- 	lualine_b = {},
	-- 	lualine_c = { require'tabline'.tabline_buffers },
	-- 	lualine_x = { require'tabline'.tabline_tabs },
	-- 	lualine_y = {},
	-- 	lualine_z = {},
	-- }
}
-- Lualine + Goyo.vim Integration
-- Source: https://neovim.discourse.group/t/new-nvim-create-autocmd-for-user-custom-event-setup/2325/3
local Goyo_enter = function()
	require("lualine").hide({
		place = { "statusline", "tabline", "winbar" }, -- The segment this change applies to.
		unhide = false, -- whether to re-enable lualine again/
		hide = true,
	})
end
--return {
--
local function Goyo_leave()
	require("lualine").hide({
		place = { "statusline", "tabline", "winbar" }, -- The segment this change applies to.
		unhide = true, -- whether to re-enable lualine again/
	})
end
local GoyoGroup = vim.api.nvim_create_augroup("GoyoGroup", { clear = true })
vim.api.nvim_create_autocmd("User", {
	pattern = "GoyoEnter",
	callback = Goyo_enter,
	group = GoyoGroup,
})
vim.api.nvim_create_autocmd("User", {
	pattern = "GoyoLeave",
	callback = Goyo_leave,
	group = GoyoGroup,
})

-- bufferline.nvim - Tab Line Configuration {{{1
require"bufferline".setup{
	options = {
		diagnostics = "nvim_lsp",
		offsets = {
			{
				filetype = "NvimTree",
				text = "File Explorer",
				highlight = "Directory",
				separator = true -- use a "true" to enable the default, or set your own character
			}
		},
		-- separator_style = "slant",
		style_preset = require'bufferline'.style_preset.minimal,
		indicator = {
			style = 'underline'
		},
		hover = {
			enabled = true,
			delay = 200,
			reveal = {'close'}
		}
	}
}

-- require"tabline".setup {
-- 	enable = true,
-- 	options = {
-- 		-- If lualine is installed tabline will use separators configured in lualine by default.
-- 		-- These options can be used to override those settings.
-- 		-- section_separators = {'', ''},
-- 		-- component_separators = {'', ''},
-- 		-- modified_icon = "● ",
-- 		show_tabs_always = false,
-- 	},
-- }

-- telescope.nvim - All-in-one Search Tool {{{1

-- local teleactions = require"telescope.actions"
local teletrouble = require"trouble.providers.telescope"
local teleluasnip = require"telescope".extensions.luasnip
require"telescope".setup {
	defaults = {
		mappings = {
			-- Open Trouble results from Telescope by hitting Ctrl-T
			i = { ["<c-t>"] = teletrouble.open_with_trouble },
			n = { ["<c-t>"] = teletrouble.open_with_trouble },
		}
	},
	-- Telescope Extensions Config
	extensions = {
		fzf = {
			fuzzy = true,                    -- false will only do exact matching
			override_generic_sorter = true,  -- override the generic sorter
			override_file_sorter = true,     -- override the file sorter
			case_mode = "smart_case",        -- or "ignore_case" or "respect_case"
			                                 -- the default case_mode is "smart_case"
		},
		["ui-select"] = {
			require"telescope.themes".get_dropdown {
				-- even more opts
			}
		},
		luasnip = {
				search = function(entry)
						return teleluasnip.filter_null(entry.context.trigger) .. " " ..
							teleluasnip.filter_null(entry.context.name) .. " " ..
							entry.ft .. " " ..
							teleluasnip.filter_description(entry.context.name, entry.context.description) ..
							teleluasnip.get_docstring(require"luasnip", entry.ft, entry.context)[1]
				end
		},
		frecency = {
			-- auto delete missing indices
			auto_validate = true,
			db_safe_mode = false
		}
	}
}
require"neoclip".setup {
	default_register = { '"', '+', '*' }
}
-- To clear clipboard history from menu
-- :lua require'neoclip'.clear_history()

-- To get fzf loaded and working with telescope, you need to call
-- load_extension, somewhere after setup function:
require"telescope".load_extension('ui-select') -- Sets vim.ui.select to telescope
require"telescope".load_extension('undo') -- Undo Tree
require"telescope".load_extension('fzf') -- fzf integration
require"telescope".load_extension('dap') -- Debug Adapter Protocol integration
require"telescope".load_extension('git_diffs') -- Diff of previous commits
require"telescope".load_extension('frecency') -- List of frequent + recent files
require"telescope".load_extension('neoclip') -- Clipboard list of each registers
require'telescope'.load_extension('luasnip') -- List of Luasnip compatible snippets and misc
require'telescope'.load_extension('heading') -- List of headings in Markdown, LaTeX, Vimdoc files
require'telescope'.load_extension('scope') -- Extension to show all buffers from all tabs

-- require'telescope.builtin'.symbols{ sources = {'emoji', 'kaomoji', 'gitmoji'} }

-- Open Telescope with keymap (leader+leader in normal mode)
vim.api.nvim_set_keymap("n", "<leader><leader>", "<Cmd>lua require'telescope'.extensions.frecency.frecency()<CR>", {noremap = true, silent = true})
vim.keymap.set("n", "<leader>u", "<cmd>Telescope undo<cr>")

-- Trouble {{{1
-- Mappings
vim.keymap.set("n", "<leader>xx", function() require"trouble".open() end)
vim.keymap.set("n", "<leader>xw", function() require"trouble".open("workspace_diagnostics") end)
vim.keymap.set("n", "<leader>xd", function() require"trouble".open("document_diagnostics") end)
vim.keymap.set("n", "<leader>xq", function() require"trouble".open("quickfix") end)
vim.keymap.set("n", "<leader>xl", function() require"trouble".open("loclist") end)

-- Obsidian {{{1
-- require'obsidian'.setup {
-- 	dir = "~/Library/CloudStorage/Dropbox/post/",
-- 	completion = {
-- 		nvim_cmp = true,
-- 	},
-- 	mappings = {
-- 		-- Overrides the 'gf' mapping to work on markdown/wiki links within your vault.
-- 		["gf"] = require"obsidian.mapping".gf_passthrough(),
-- 	},
-- 	disable_frontmatter = false, -- switch to true if you're using vim-markdown's front-matter
-- }
