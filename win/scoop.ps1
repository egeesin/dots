# vim:ft=ps1
# Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Install Scoop first if it doesn't exists

# if (!(Get-Command scoop -ErrorAction SilentlyContinue))
if (-Not(Get-Command scoop -ErrorAction "Ignore")){
    Write-Warning "Scoop not found. Installing..." -ForegroundColor "Yellow"
    # irm get.scoop.sh | iex
	# Invoke-WebRequest -useb get.scoop.sh | Invoke-Expression
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
#    	"psutils",
#    	"gawk",
#    	"grep",
#    	"lazygit",
#    	"sed",
#    	"sudo",
#    	"wget",
#    	"which",

    # CLI
#    	"fastfetch",
#    	"starship",
#    	"ripgrep",
#    	"pandoc",
#    	"gotop",
#    	"chafa",
#    	"pastel",
#    	"yazi",
#    	"zoxide",

    # Languages
#       # "nodejs",
#       # "nodejs-lts",
#       "vfox",
#       "uv",
#       "rustup",

    # Hardware and Peripherals
#    	"etcher",
#    	# "rufus",
#    	"nvidia-display-driver-dch-np",
#    	"cpu-z",
#    	"gpu-z",
#    	"crystaldiskinfo",
#    	"crystaldiskmark",
#       "wiztree",
#    	"openhardwaremonitor",
#    	"openrgb",
#    	"autohotkey",
#    	"sharpkeys",
#    	"flow-launcher",
#    	"windhawk",
#    	"powertoys",
#    	"text-grab",
#        "systeminformer",
#        "eartrumpet",
#       "magpie",
#    	"glogg", # log explorer
#       "rustdesk",
#       # "opentabletdriver"

    # Essentials
#       "pwsh",  
#    	"firefox",
#    	"thunderbird",
#    	"bitwarden",
#    	"syncthing",
#    	"winrar",
#    	"sumatrapdf",
#        "vcredist2022", "cmake", "zig", "mingw", "netcat"
#        # ^ dep of nvim
#    	"helix",
#    	"lua-language-server",
#    	"marksman",
#    	"shellcheck",
#    	"television",
#    	"zed",
#    	"kate",
#    	"krita",
#    	"obsidian",
#        "libreoffice",
#    	# "alacritty",
#    	"wezterm",
#    	"putty",
#    	"winscp",
#    	"ccleaner",
#    	"sharex",
#       "shutup10",
#    #    "pureref", no longer has 2.0 versions, might be unmantained
#    	"localsend",
#    	"deskflow",

    # Media
#    	"yt-dlp",
#    	"qview",
#    	"mpv",
#    	"syncplay",
#    	"musicbee",
#    	"quodlibet",
#    	"qbittorrent-enhanced",
#        "jackett",
#    	"ffmpeg",
#    	"lmms",
#    	"kdenlive",
#    	# "imagemagick",
#    	"graphicsmagick",
#       "rawtherapee",
#       "streamlink",
#    	"handbrake",
#    	"jexiftoolgui",
#    	"fork",
#    	"ungoogled-chromium",
#        "mp3tag",
#    	"f3d",

    # Communication
#       "element",
#    	"microsoft-teams",
#    	"telegram",
#    	"zoom",

    # Streaming
#    	"obs-studio",
#    	"livesplit",
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
#    	"blender",
#    	"rcedit", # for exporting Windows build in Godot
#    	# "betterjoy",

    # Misc
#        "act",
#        "vtm",
#        "gifsicle",
#        "iographica",
#        # "workspacer", # i3-like window manager, might not work perfect, requires learning curve
#
    	"msys2"

    # Wanted:
    #
    # 8bitdo ultimate software
    # outline client
    # debain wsl (uwp)
    # xbox (uwp)
    # minecraft for w10 (uwp)
    # nodejs installation from vfox
    )
    ForEach( $app in $apps ) {
        scoop install $app
    }

    # cleanup Scoop cache
    scoop cleanup *
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

