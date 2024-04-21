# vim:ft=ps1

# Useful sources:
# https://github.com/xeho91/.dotfiles/blob/main/Windows/install.ps1
# https://github.com/SARDONYX-sard/dotfiles/blob/main/install-win.ps1

# Are you root?
if (-not ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole(
		[Security.Principal.WindowsBuiltInRole] "Administrator")) {
	Write-Error "This script must be run as an administrator."
	exit $?
}

# Receive dots
Set-Location $HOME
if (!(Test-Path $HOME/.dots)) {
	git clone https://github.com/egeesin/dots $HOME/.dots
}

# Install packages from Chocolatey and Scoop
Invoke-Expression "$HOME\.dots\setup\choco.ps1"
Invoke-Expression "$HOME\.dots\setup\scoop.ps1"

# winget import "$HOME/dots/setup/winget.json"

# Connect each file (or directory) to dotfiles with a symbolic link.
Invoke-Expression "$HOME\.dots\link.ps1"

Write-Host "Dotfiles installation is done." -ForegroundColor Green
