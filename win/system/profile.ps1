# -*-mode:powershell-*- vim:ft=powershell

# Determine user profile parent directory.
$ProfilePath=Split-Path -parent $profile

# Load alias definitions from separate configuration file.
if (Test-Path $ProfilePath\aliases.ps1) {
    . $ProfilePath\aliases.ps1
}

if (Test-Path "$env:AppData\gnupg") {
    $env:GNUPGHOME = "$env:AppData\gnupg"
    [System.Environment]::SetEnvironmentVariable('GNUPGHOME', $env:GNUPGHOME)
}

# Configure editor for various tasks
if (Get-Command "nvim" -ErrorAction "Ignore") {
    $env:EDITOR = "nvim"
    $env:VISUAL = "nvim"
}

$env:STARSHIP_CONFIG = "$HOME\.config\starship.toml"

Invoke-Expression (&starship init powershell)