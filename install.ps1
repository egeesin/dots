# -*-mode:powershell-*- vim:ft=powershell
# Source: https://github.com/xeho91/.dotfiles/blob/main/Windows/install.ps1
#         https://github.com/SARDONYX-sard/dotfiles/blob/main/install-win.ps1

# Are you root?
if (-not ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole(`
		[Security.Principal.WindowsBuiltInRole] "Administrator")) {
	Write-Error "This script must be run as an administrator."
	exit $?
}

$DotfilesRepositoryURL = "https://github.com/egeesin/dots.git"

# ============================================================================ #
# Helpers
# ============================================================================ #

$StartingLocation = (Get-Location).Path
# $DotfilesDirName = [System.IO.Path]::GetFileNameWithoutExtension("$DotfilesRepositoryURL")
$DotfilesDirName = ".dots"

# Wrapper for logging the colored output messages based on type
function Log {
	param(
		[String]$logType,
		[String]$message
	)

	$colors = @(
		[PSCustomObject]@{
			name  = "info"
			color = "DarkBlue"
		}
		[PSCustomObject]@{
			name  = "error"
			color = "DarkRed"
		}
		[PSCustomObject]@{
			name  = "warning"
			color = "DarkYellow"
		}
		[PSCustomObject]@{
			name  = "success"
			color = "DarkGreen"
		}
		[PSCustomObject]@{
			name  = "note"
			color = "DarkMagenta"
		}
	)
	$logTypeColor = ($colors | Where-Object { $_.name -eq $logType }).color

	Write-Host "$($logType.ToUpper()):" -BackgroundColor $logTypeColor -ForegroundColor White -NoNewline
	Write-Host " $message" -ForegroundColor $logTypeColor
}

# Receive dots
function Receive-Dots {
	Log info "Verifying if command ``git`` exists..."

	if (Get-Command "git" -errorAction SilentlyContinue) {
		Log note "Program ``git`` exists."

		Log info "Cloning dotfiles from the '$DotfilesRepositoryURL' repository..."
		# Invoke-Expression("git clone $DotfilesRepositoryURL")
		Invoke-Expression("git clone $DotfilesRepositoryURL $DotfilesDirName")
	} else {
		Log error "Program Git (``git``) doesn't exist and is required to complete this installation."
		Exit 1
	}
}

# Set pre-configured Windows defaults
function InitialScript {
	cmd /c "$Env:USERPROFILE\$DotfilesDirName\setup\init.cmd"
}

# Install packages from Chocolatey and Scoop
function InstallPkgs {
	. "$PSScriptRoot\win\setup\choco.ps1"
	. "$PSScriptRoot\win\setup\scoop.ps1"
}

# Enable WSL2 support
function EnableWSL2 {
  dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
  dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
  wsl --set-default-version 2
}

function New-Symlink {
	param(
		$fileName,
		$locationInDotfiles
	)
	$options = @{
		ItemType = "SymbolicLink"
		Target   = "$Env:USERPROFILE\$DotfilesDirName\$locationInDotfiles"
		Path     = "$Env:USERPROFILE\$fileName"
	}
	New-Item @options
}

function Set-Links {
	Log info "Creating symbolic links to configurations from the dotfiles..."
	# New-Symlink ".gitconfig" "Git/.gitconfig"
	# New-Symlink ".editorconfig" "Editors/.editorconfig"
	Log success "Successfully created symlinks."
}

function Set-SourcingToPowershellProfile {
	$profilePath = "$Env:USERPROFILE\$DotfilesDirName\win\system\profile.ps1"

	(-Join (
		"`$PROFILE = $profilePath`n",
		'. $PROFILE'
	))| Out-File -FilePath "$PROFILE"
}
Set-SourcingToPowershellProfile

# ============================================================================ #
# Main runtime
# ============================================================================ #
function Main {
	# Check if current working directory is User's home and change if not
	if (-Not ($StartingLocation -eq $Env:USERPROFILE)) {
		Log info "Changing location to '$Env:USERPROFILE'..."
		Set-Location $Env:USERPROFILE
		Log success "Successfully changed to user's home directory."
	}
	Log note "You are in User's home directory."

	Receive-Dots
	Set-Links
	Set-SourcingToPowershellProfile

	# Return to previous working location
	if (-Not ($StartingLocation -eq $Env:USERPROFILE)) {
		Log info "Returning to previous location '$StartingLocation..."
		Set-Location $StartingLocation
		Log note "Changed to previous (starting) location."
	}
}

Log info "Starting the installation..."
Main
Log success "Installation finished."