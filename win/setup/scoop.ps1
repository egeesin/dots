# -*-mode:powershell-*- vim:ft=powershell
# Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Install Scoop first if it doesn't exists

if (-Not(Get-Command scoop -ErrorAction "Ignore")){
    Write-Warning "Scoop not found. Installing..." -ForegroundColor "Yellow"
    # irm get.scoop.sh | iex
    Invoke-Expression (New-Object System.Net.WebClient).DownloadString('https://get.scoop.sh')
}
if (Get-Command "scoop" -ErrorAction "Stop") {
    Write-Host "Installing packages from Scoop..." -ForegroundColor "Yellow"
    Write-Host "Verifying the state of Scoop..."
    Invoke-Command -ScriptBlock { scoop checkup }

    # Install packages necessary for installations
    scoop install 7zip innounp dark git

    # Add Buckets
    $scoopbuckets = @(
        "extras",
        "versions",
        "nonportable",
        "java",
        "games"
    )
    ForEach( $scoopbucket in $scoopbuckets ) {
        scoop bucket add $scoopbucket
    }

    # Install packages
    $scoops = @(
    # Core
    	"coreutils",
    	"curl",
#    	"diffutils",
#    	"findutils",
#    	"gawk",
#    	"git",
#    	"gradle",
#    	"grep",
#    	"lazygit",
#    	"git-delta",
#    	"sed",
#    	"sudo",
#    	"wget",
#    	"which",

    # CLI
#    	"neofetch",
#    	"starship",
#    	"ripgrep",
#    	"pandoc",
#    	"shellcheck",
#    	"psfzf",
#    	"fzf",
#    	"fd",
#    	"gotop",
#    	"chafa",
#    	"pastel",
#    	"yazi",

    # Languages
#    	"oraclejre8",
#    	"temurin17-jre",
#    	"temurin-jre",
#       "nodejs",
#       # "nodejs-lts",
#       "pnpm",
#    	"pyenv",

    # Hardware and Peripherals
#    	"nvidia-display-driver-dch-np",
#    	"cpu-z",
#    	"gpu-z",
#    	"crystaldiskinfo",
#    	"crystaldiskmark",
#    	"twinkle-tray",
#    	"rufus",
#    	#"windirstat",
#        "wiztree",
#    	"openhardwaremonitor",
#    	"autohotkey",
#    	"sharpkeys",
#    	"powertoys",
#        "processhacker",
#        "eartrumpet",
#       "magpie",
#    	"glogg", # log explorer

    # Essentials
#    	"firefox",
#    	"bitwarden",
#        "authy",
#    	"winrar",
#    	"sumatrapdf",
#        "vcredist2022", "cmake", "zig", "mingw", "netcat"
#        # ^ dep of nvim
#    	"neovim",
#    	"neovide",
#    	"sublime-text",
#    	"obsidian",
#        "libreoffice",
#    	"alacritty",
#    	"putty",
#    	"winscp",
#    	"ccleaner",
#    	"sharex",
#       "rssguard",
#    	"advancedrenamer",
#        "shutup10",
#        "pureref",
#    	"localsend",

    # Media
#    	"yt-dlp",
#    	"imageglass",
#    	"mpv",
#    	"quodlibet",
#    	"qbittorrent-enhanced",
#        "jackett",
#    	"ffmpeg",
#    	"imagemagick",
#       "rawtherapee",
#        "streamlink",
#    	"handbrake",
#    	"jexiftoolgui",
#    	"fork",
#    	"ungoogled-chromium",
#        "mp3tag",
#        # "mpd",
#    	"f3d",

    # Communication
#        "element",
#    	"microsoft-teams",
#    	"telegram",
#    	"zoom",

    # Streaming
#    	"obs-studio",
#    	"livesplit",
#    	# "chatterino",
#    	"chatterino7",

    # Games, Game Development, Helpers
#    	"playnite",
#    	"uplay",
#    	"steam",
#        "itch",
#    	"prismlauncher",
#       "blockbench",
#        "amulet-map-editor",
#    	"godot",
#    	"rcedit", # for exporting Windows build in Godot
#    	# "betterjoy",

    # Misc
#        "gifsicle",
#        "iographica",
#        # "mypaint",
#        # "workplacer", # i3-like window manager, might not work perfect, requires learning curve
#
    	"msys2"

    # Wanted:
    #
    # 8bitdo ultimate software
    # outline client
    # debain wsl (uwp)
    # xbox (uwp)
    # minecraft for w10 (uwp)
    )
    ForEach( $app in $apps ) {
        scoop install $app
    }

    # cleanup Scoop cache
    scoop cache rm *

    Write-Output "Packages from Scoop -> Done!" -ForegroundColor "Green"
    Write-Output "Don't forget to restart later!"
}

# set MSYS2 environment variable
$MSYS2_ROOT = scoop info msys2 | sed -n '/Installed/{n;p}' | tr -d "[:space:]"
[System.Environment]::SetEnvironmentVariable('MSYS2_ROOT', $MSYS2_ROOT,
[System.EnvironmentVariableTarget]::User)

# sync MSYS2 and Windows home directories
$MSYS2_HOME = "$MSYS2_ROOT\home\$env:USERNAME"
New-Item -ItemType Junction -Path $MSYS2_HOME -Value $env:USERPROFILE

# start MSYS2 to continue installation
msys2

