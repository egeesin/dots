#Requires -Version 7.1

$neovidePath = "$env:UserProfile\scoop\apps\neovide\current\neovide.exe"

$env:XDG_DATA_HOME = $env:XDG_DATA_HOME ?? $env:APPDATA
$env:XDG_CONFIG_HOME = $env:XDG_CONFIG_HOME ?? $env:LOCALAPPDATA
$env:XDG_CACHE_HOME = $env:XDG_CACHE_HOME ?? $env:TEMP

$env:LUNARVIM_RUNTIME_DIR = $env:LUNARVIM_RUNTIME_DIR ?? "$env:XDG_DATA_HOME\lunarvim"
$env:LUNARVIM_CONFIG_DIR = $env:LUNARVIM_CONFIG_DIR ?? "$env:XDG_CONFIG_HOME\lvim"
$env:LUNARVIM_CACHE_DIR = $env:LUNARVIM_CACHE_DIR ?? "$env:XDG_CACHE_HOME\lvim"
$env:LUNARVIM_BASE_DIR = $env:LUNARVIM_BASE_DIR ?? "$env:LUNARVIM_RUNTIME_DIR\lvim"

$neovideArgs = "-- -u $($env:LUNARVIM_BASE_DIR\init.lua)"

# capture remaining arguments
$remainingArgs = $args -join " "

if ($remainingArgs) {
    $neovideArgs += " " + $remainingArgs
}

& $neovidePath $neovideArgs

# $env:neovidePath -u "$env:LUNARVIM_BASE_DIR\init.lua" @args
