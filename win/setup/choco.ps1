# -*-mode:powershell-*- vim:ft=powershell
# Set-ExecutionPolicy Bypass -Scope Process -Force

if (-Not(Get-Command scoop -ErrorAction "Ignore")){
	[System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072
	Invoke-Expression ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
}

if (Get-Command "choco" -ErrorAction "Ignore") {
	Write-Host "Installing packages from Chocolatey..."
	Write-Host "Verifying the state of Chocolatey..."

	# Upgrade first
	cup -y chocolatey

	choco feature enable -n=useRememberedArgumentsForUpgrades

	# Install packages

	# $chocos = Get-Content "$PSScriptRoot\Chocofile"
	$chocos = @(
		# HARDWARE SPECIFIC PACKAGES

		# "amd-ryzen-chipset",
		# "realtek-hd-audio-driver",
		# "nvidia-display-driver",

		# "chatterino",
#		"discord",
#		# "spotify",
#		"hfsexplorer",
#		# "netfx-4.8",
#		# "wincommandpaste"
#		"activitywatch",
#		"virustotaluploader",
#		"virtualbox",
#		"fontforge",
#		"dropbox",
		"auto-dark-mode",
		"choco-cleaner"
		# "altserver.install",
#		"epicgameslauncher",
#		# "logitechgaming"
	)
	ForEach( $choco in $chocos ) {
		choco install -y $choco --limit-output
		# cinst -y $choco -r
	}
	# Do not update packages below
	$chocopins = @(
#		dropbox,
#		discord,
#		itunes
	)
	ForEach( $chocopin in $chocopins ) {
		choco pin add --name $chocopin -r
	}
	Write-Output "Packages from Chocolatey -> Done!"
	Write-Output "Don't forget to restart later!"
}
