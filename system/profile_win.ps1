# vim:ft=ps1

[System.Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSUseDeclaredVarsMoreThanAssignments', '')]
$executionTime = $(Measure-Command {
		$DotsDir = "$HOME\.dots\";
		#! These files could not be lazily loaded.
		# . "$($DotsDir)\index.ps1"
		. "$($DotsDir)\system\alias_win.ps1"
		function prompt {
			# This function is lazy load. Put off heavy processing to speed up startup.
			. "$($DotsDir)\system\function_win.ps1"
			# . "$($DotsDir)/shell-design.ps1"
			# . "$($DotsDir)/index.lazy.ps1"
		}
		# . "$($DotsDir)/enhanced-lazy.ps1" # Enable lazy loading for some modules where lazy loading does not work in the prompt function.
	}).TotalMilliseconds

# Determine user profile parent directory.
# $ProfilePath=Split-Path -parent $profile

# Load alias and function definitions from separate configuration file.
# if (Test-Path $ProfilePath\alias_win) {
#     . $ProfilePath\alias_win
# }


# if (Test-Path "$env:AppData\gnupg") {
#     $env:GNUPGHOME = "$env:AppData\gnupg"
#     [System.Environment]::SetEnvironmentVariable('GNUPGHOME', $env:GNUPGHOME)
# }

# Configure editor for various tasks
if (Get-Command "nvim" -ErrorAction "Ignore") {
    $env:EDITOR = "nvim"
    $env:VISUAL = "nvim"
}

$env:STARSHIP_CONFIG = "$HOME\.config\starship.toml"

Invoke-Expression (&starship init powershell)
Invoke-Expression "$(vfox activate pwsh)"
Invoke-Expression (& { (zoxide init powershell | Out-String) })
$env:_ZO_ECHO = '1'


Set-Alias lvim 'C:\Users\ege_e\.local\bin\lvim.ps1'
Set-Alias neovide 'C:\Users\ege_e\scoop\apps\neovide\current\neovide.exe"'
# Set-Alias pn 'C:\Users\ege_e\scoop\shims\pnpm.EXE'
Set-Alias pn 'C:\Users\ege_e\.version-fox\cache\nodejs\current\pnpm.ps1'


