# vim:ft=ps1
# Source: https://github.com/SARDONYX-sard/.dots/blob/main/windows/setup/symlink.ps1
# Warning: Make sure Param(...) is always in the first uncommented line!
Param([switch]$f, [switch]$force, [switch]$d, [switch]$isDebug)
$force = $f.IsPresent -or $force.IsPresent
$isDebug = $d.IsPresent -or $isDebug.IsPresent
<#
.SYNOPSIS
	Create Symlink format
.DESCRIPTION
	Create Symlink format and give formatted data to Set-Symlink function
.EXAMPLE
	# Debug mode. Output `result.txt` file not called Set-Symlink function.
	pwsh symlink.ps1 -d

	# Force mode.
	pwsh symlink.ps1 -f
.OUTPUTS
	Symlink files
#>

# Are you root?
if ($isDebug -eq $false) {
	if (-not ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole(
			[Security.Principal.WindowsBuiltInRole] "Administrator")) {
		Invoke-Expression "sudo $PsCommandPath $(if ($force) {"-force"})"
		exit $?
	}
}


# --------------------------------------------------------------------------------------------------
# Files
# --------------------------------------------------------------------------------------------------
<#
.NOTES
Specification

target(require):
	1. target is the actual directory or file. Relative from `$HOME/.dots` or absolute path.
	#! 2. A single string will be converted to target even if it is not specified as target.
	e.g.: @{"windows/config/.bashrc" } → @{ target= "$HOME/.dots/windows/config/.bashrc"; path= "$HOME/.bashrc"; name= ".bashrc" }
which one(optional):
	path(option):
		1. The path is relative to $HOME/.dots.
		(e.g.: "windows/config")
	fullpath(option):
		1. Path to derive path; if name is not specified, the last path will be used for name.
		(e.g.: "$HOME")

name(option):
	1. the name of the symbolic file
	(e.g.: ".bashrc")
#>
$files = @(
	# vim
	# @{ target = "config\vim"; path = ""; name = ".vimrc" }

	# Neovim
	@{ target = "config\old\nvim\vim-init"; fullpath = [IO.Path]::Combine($HOME, "AppData\Local\nvim\init.vim"); }
	@{ target = "config\old\nvim\vim-ftdetect"; fullpath = [IO.Path]::Combine($HOME, "AppData\Local\nvim\ftdetect"); }
	@{ target = "config\old\nvim\vim-ftplugin"; fullpath = [IO.Path]::Combine($HOME, "AppData\Local\nvim\ftplugin"); }
	@{ target = "config\old\nvim\vim-partials"; fullpath = [IO.Path]::Combine($HOME, "AppData\Local\nvim\partials"); }
  
	# LunarVim
	@{ target = "config\lunarvim"; fullpath = [IO.Path]::Combine($HOME, "AppData\Local\lvim\config.lua"); }

	# Helix
	@{ target = "config\helix-config"; fullpath = [IO.Path]::Combine($HOME, "AppData\Roaming\helix\config.toml"); }
	@{ target = "config\helix-langs"; fullpath = [IO.Path]::Combine($HOME, "AppData\Roaming\helix\languages.toml"); }
	@{ target = "config\helix-ext-snippets"; fullpath = [IO.Path]::Combine($HOME, "AppData\Roaming\helix\external-snippets.toml"); }
	
	# Terminal (Wezterm)
	@{ target = "config\wezterm"; fullpath = [IO.Path]::Combine($HOME, ".wezterm.lua"); }

	# Terminal (Alacritty)
	@{ target = "config\old\alacritty"; fullpath = [IO.Path]::Combine($HOME, "AppData\Roaming\alacritty\alacritty.toml"); }
	# $terminalPath = [IO.Path]::Combine($env:LocalAppData, "Packages\Microsoft.WindowsTerminal_8wekyb3d8bbwe\LocalState\settings.json")
	# $terminalPreviewPath = $terminalPath.Replace("Terminal", "TerminalPreview")
	# @{ target = "config\windows-terminal"; fullpath = $terminalPath; name = "settings.json" } # mode = "copy" }
	# @{ target = "config\windows-terminal-preview"; fullpath = $terminalPreviewPath; name = "settings.json" } # mode = "copy" }

	# global git
	@{ target = "config\gitignore"; fullpath = [IO.Path]::Combine($HOME, ".config\git\ignore"); name = "ignore" } # mode = "copy" }
	@{ target = "config\git"; path = ""; name = ".gitconfig" }

	# if (Test-Path navi) {
	# 	@{ target = "config\navi-config.yml"; fullpath = "$(navi info config-path | Write-Output)"; name = "config.yml" } #manual
	# }

	# @{ target = "scripts/startup.py"; fullpath = [IO.Path]::Combine($env:AppData, "Microsoft\Windows\Start Menu\Programs\Startup\startup.py"); name = "startup.py" }

	# msys2 HomeDir
	# if (Test-Path "$HOME\scoop\apps\msys2") {
	# 	$UserName = (Split-Path $HOME -Leaf)
	# 	$msys2HomeDir = [IO.Path]::Combine($HOME, "scoop\apps\msys2\current\home\$UserName")
	# 	if ($force) { Remove-Item -f $msys2HomeDir }
	# 	@{ target = $HOME; fullpath = $msys2HomeDir; }
	#
	# 	"linux/.bashrc"
	# 	"linux/.fihrc.fish"
	# 	"linux/.zshrc"
	# }
)

$pwshProfilePath = @($(pwsh -NoProfile -Command "`$profile"))[0]
$powerShellProfilePath = @($(powerShell -NoProfile -Command "`$profile"))[0]

# If you have a profile, add it and add it to $files.
if ( (Get-Command pwsh -ea 0) -and (pwsh -NoProfile -Command "`$profile")) {
	$files += @(@{target = "system\profile_win.ps1"; fullpath = $pwshProfilePath })

	# create symlink from `pwsh's modules` to `powershell's modules`
	$pwshModulePath = [IO.Path]::Combine(($pwshProfilePath | Split-Path), "Modules")
	$powershellModulePath = [IO.Path]::Combine(($powerShellProfilePath | Split-Path), "Modules")
	$files += @(@{ target = $pwshModulePath; fullpath = $powershellModulePath; })
}

if ( (Get-Command powershell -ea 0) -and (powershell -NoProfile -Command "`$profile")) {
	$files += @(@{target = "system\profile_win.ps1"; fullpath = $powerShellProfilePath })
}

# --------------------------------------------------------------------------------------------------
# Create Symbolic link
# --------------------------------------------------------------------------------------------------
function Set-Symlink {
	[CmdletBinding()]
	param (
		[string]$FromFileOrDirPath,
		[string]$ToFileOrDirPath,
		[hashtable]$Hash,
		[switch]$Force
	)
	$file = $null # Does not use ternary operators for `powershell compatibility`
	if ($Hash) { $file = $Hash }

	if ($file) {
		$PathName = [IO.Path]::Combine($file.path, $file.name)
		Write-Host ""
		Write-Host "now: $($PathName)"

		$fullPathName = $PathName
		if (Test-Path $fullPathName) {
			Write-Host "Already exists." -ForegroundColor Blue
			if ($force) {
				Write-Host "Recreating..." -ForegroundColor Yellow
			(Get-Item $fullPathName).Delete()
			}
			else { return }
		}

		if (!(Test-Path $fullPathName)) {

			if (!(Test-Path ($file.path))) {
				mkdir ($file.path)
			}

			# Copy or SymbolicLink
			if ($file.mode -eq "copy") {
				Write-Host "Copying..." -ForegroundColor Green
				Copy-Item $file.target -Destination $file.path -Force
			}
			else {
				Write-Host "Making symbolic link..." -ForegroundColor Green

				#? Passing whitespace as a whole object will not result in a path error.
				New-Item -ItemType SymbolicLink @file | Out-Null
			}
			if (!$?) { Write-Error "${@file} is null. Failed to create symbolic link." }
		}

		return
	}

	Write-Host ""
	Write-Host "now: $FromFileOrDirPath"

	if (Test-Path $ToFileOrDirPath) {
		Write-Host "Already exists." -ForegroundColor Blue
		if ($force) {
			Write-Host "Recreating..." -ForegroundColor Yellow
				(Get-Item $fullPathName).Delete()
		}
		else { return }
	}

	if (!(Test-Path $ToFileOrDirPath)) {
		if (!(Test-Path ($ToDirPath))) { mkdir ($ToDirPath) }

		$name = Split-Path $ToFileOrDirPath -Leaf
		$ToDirPath = Split-Path $ToFileOrDirPath
		Write-Host "Making symbolic link..." -ForegroundColor Green
		New-Item -Value $FromFileOrDirPath -Path $ToDirPath -Name $Name -ItemType SymbolicLink | Out-Null
		if (!$?) { Write-Error "${@file} is null. Failed to create symbolic link." }
	}
}

function create_symlink($files) {
	if ($isDebug) {
		Write-Host "Debug mode is running..." -ForegroundColor Blue
		if (Test-Path result.txt) {
			Write-Host "result.txt already exists. Delete it." -ForegroundColor Yellow
			Remove-Item result.txt -Force
		}
	}
	else {
		Write-Host "Symbolic links mode is running..." -ForegroundColor Green
	}

	foreach ($file in $files) {
		if ($file.GetType() -eq [string]) {
			if (!$file) { continue }

			$file = @{target = $file; path = "" }
		}

		$isDrive = (Split-Path $file.target) -match "^[A-Z]:\\"
		if ($isDrive -eq $false) {
			$file.target = [IO.Path]::Combine("$HOME/.dots", $file.target)
			if (!$file.name) { $file.name = Split-Path $file.target -Leaf }
		}


		if ( !$file.path ) { $file.path = "$HOME" }
		else { $file.path = [IO.Path]::Combine($HOME, $file.path) }

		if (!$file.name) { $file.name = Split-Path $file.path -Leaf }

		# Overwrite `path`& `name` property if `fullpath` is specified.
		if ($file.fullpath) {
			$file.name = Split-Path $file.fullpath -Leaf
			$file.path = Split-Path $file.fullpath
			$file.Remove("fullpath")
		}


		if ($isDebug) {
			Write-Output @file "`n" | Out-File result.txt -Append # for debug
			Write-Host @file "`n"
			continue
		}

		# Make symlink
		if (!(Test-Path $file.path)) {
			mkdir $file.path
		}
		if ($Force) { Set-SymLink -Hash $file -Force }
		else { Set-SymLink -Hash $file }
	}
}

create_symlink $files
