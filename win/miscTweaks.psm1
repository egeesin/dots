# -*-mode:powershell-*- vim:ft=powershell
# Add secondary Hebrew keyboard
# Function AddHebrewKeyboard {
#     Write-Output 'Adding Turkish keyboard...'
#     $langs = Get-WinUserLanguageList
#     $langNames = $langs.EnglishName
#     if (-Not $langNames.Contains('Turkish')) {
#         $langs.Add('he')
#         Set-WinUserLanguageList $langs -Force
#     }
# }

# See https://stackoverflow.com/a/40033638/1014208
Function EnableDeveloperMode {
    Write-Output 'Enabling developer mode...'
    # Create AppModelUnlock if it doesn't exist, required for enabling Developer Mode
    $RegistryKeyPath = 'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\AppModelUnlock'
    if (-not(Test-Path -Path $RegistryKeyPath)) {
        New-Item -Path $RegistryKeyPath -ItemType Directory -Force
    }
    Set-ItemProperty -Path "$RegistryKeyPath" -Name AllowDevelopmentWithoutDevLicense -Value 1
}

# Disable transparency
Function DisableTransparency {
	Write-Output "Disabling transparency..."
	Set-ItemProperty -Path "HKCU:\Software\Microsoft\Windows\CurrentVersion\Themes\Personalize" -Name "EnableTransparency" -Type DWord -Value 0
}

# Enable transparency
Function EnableTransparency {
	Write-Output "Enabling transparency..."
	Set-ItemProperty -Path "HKCU:\Software\Microsoft\Windows\CurrentVersion\Themes\Personalize" -Name "EnableTransparency" -Type DWord -Value 1
}

Function UninstallMaybeBloat {
	Write-Output "Uninstalling maybe bloat apps..."
	Get-AppxPackage "Microsoft.AppConnector" | Remove-AppxPackage
	Get-AppxPackage "Microsoft.HelpAndTips" | Remove-AppxPackage
	Get-AppxPackage "Microsoft.MSPaint" | Remove-AppxPackage
	Get-AppxPackage "Microsoft.NetworkSpeedTest" | Remove-AppxPackage
	Get-AppxPackage "Microsoft.RemoteDesktop" | Remove-AppxPackage
	Get-AppxPackage "Microsoft.WindowsCamera" | Remove-AppxPackage
	Get-AppxPackage "Microsoft.YourPhone" | Remove-AppxPackage
}

# Install apps that may be useful but are considered as bloat in Win10.psm1.
Function InstallMaybeBloat {
	Write-Output "Installing maybe bloat apps..."
	Get-AppxPackage -AllUsers "Microsoft.AppConnector" | ForEach-Object {Add-AppxPackage -DisableDevelopmentMode -Register "$($_.InstallLocation)\AppXManifest.xml"}
	Get-AppxPackage -AllUsers "Microsoft.HelpAndTips" | ForEach-Object {Add-AppxPackage -DisableDevelopmentMode -Register "$($_.InstallLocation)\AppXManifest.xml"}
	Get-AppxPackage -AllUsers "Microsoft.MSPaint" | ForEach-Object {Add-AppxPackage -DisableDevelopmentMode -Register "$($_.InstallLocation)\AppXManifest.xml"}
	Get-AppxPackage -AllUsers "Microsoft.NetworkSpeedTest" | ForEach-Object {Add-AppxPackage -DisableDevelopmentMode -Register "$($_.InstallLocation)\AppXManifest.xml"}
	Get-AppxPackage -AllUsers "Microsoft.RemoteDesktop" | ForEach-Object {Add-AppxPackage -DisableDevelopmentMode -Register "$($_.InstallLocation)\AppXManifest.xml"}
	Get-AppxPackage -AllUsers "Microsoft.WindowsCamera" | ForEach-Object {Add-AppxPackage -DisableDevelopmentMode -Register "$($_.InstallLocation)\AppXManifest.xml"}
	Get-AppxPackage -AllUsers "Microsoft.YourPhone" | ForEach-Object {Add-AppxPackage -DisableDevelopmentMode -Register "$($_.InstallLocation)\AppXManifest.xml"}
}

Function SetKeyboardTypingSpeed {
	Write-Output 'Setting keyboard typing speed...'
  # Maximize repeat rate and minimize repeat delay.
	Set-ItemProperty -Path 'HKCU:\Control Panel\Keyboard' -Name 'KeyboardDelay' -Type DWord -Value 0
	Set-ItemProperty -Path 'HKCU:\Control Panel\Keyboard' -Name 'KeyboardSpeed' -Type String -Value '31'
}

# Enables sticky keys in order to work around the slow key repeat in Windows (even when maximizing the settings as above).
# See also: https://superuser.com/a/1223508/407543
# NOTE: As of 2020-01-07, using this causes issues with modifiers, so it's disabled.
Function EnableStickyKeysHack {
	Set-ItemProperty -Path 'HKCU:\Control Panel\Accessibility\Keyboard Response' -Name 'AutoRepeatDelay' -Type String -Value '200'
	Set-ItemProperty -Path 'HKCU:\Control Panel\Accessibility\Keyboard Response' -Name 'AutoRepeatRate' -Type String -Value '6'
	Set-ItemProperty -Path 'HKCU:\Control Panel\Accessibility\Keyboard Response' -Name 'DelayBeforeAcceptance' -Type String -Value '0'
	Set-ItemProperty -Path 'HKCU:\Control Panel\Accessibility\Keyboard Response' -Name 'BounceTime' -Type String -Value '0'
  # Reference for the flag values:
  # https://docs.microsoft.com/en-us/windows/win32/api/winuser/ns-winuser-filterkeys
  # Enabled flags:
  # - 0x01 : enable the filter keys feature
  # - 0x02 : make filter keys available 
  # - 0x08 : confirm hot key (Win 95/98/2000 only?)
  # - 0x20 : show a visual indicator when the FilterKeys features are on (Win 95/2000 only?)
	Set-ItemProperty -Path 'HKCU:\Control Panel\Accessibility\Keyboard Response' -Name 'Flags' -Type String -Value '43'
}

Function SetPointersMovement {
	Set-ItemProperty -Path 'HKCU:\Control Panel\Mouse' -Name 'MouseSensitivity' -Type String -Value '16'
	Set-ItemProperty -Path 'HKCU:\Software\Microsoft\Windows\CurrentVersion\PrecisionTouchPad' -Name 'CursorSpeed' -Type DWord -Value 18
}