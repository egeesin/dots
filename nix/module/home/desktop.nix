{
  # lib,
  # inputs,
  # pkgs,
  ...
}:{
# }: let
#   inherit (lib.modules) mkMerge;

#   mapAutostart = { pkg, desktopFile, }: {
#     xdg.configFile."autostart/${desktopFile}".source = "${pkg}/share/applications/${desktopFile}";
#   };
#   autostarts = [
#     {
#       pkg = pkgs.discord;
#       desktopFile = "discord.desktop";
#     }
#     {
#       pkg = pkgs.discord;
#       desktopFile = "discord.desktop";
#     }
#   ];

# in {
#   mkMerge (map mapAutostart autostarts);
  xdg = {
    mimeApps = rec {
      enable = true;
      defaultApplications = {
        "application/x-extension-htm"="zen-beta.desktop";
        "application/x-extension-html"="zen-beta.desktop";
        "application/x-extension-ics"="userapp-Thunderbird-IR3452.desktop";
        "application/x-extension-shtml"="zen-beta.desktop";
        "application/x-extension-xht"="zen-beta.desktop";
        "application/x-extension-xhtml"="zen-beta.desktop";
        "application/xhtml+xml"="zen-beta.desktop";
        "application/x-msdownload"="com.heroicgameslauncher.hgl.desktop";
        "application/x-shellscript"="org.kde.kate.desktop";
        "application/vnd.appimage"="it.mijorus.gearlever.desktop";
        "application/json"="org.kde.kate.desktop";
        "x-scheme-handler/discord"="vesktop.desktop";
        "x-scheme-handler/http " = ["zen-beta.desktop" " firefox.desktop" "chromium-browser.desktop" ];
        "x-scheme-handler/chrome " = ["zen-beta.desktop" " firefox.desktop" "chromium-browser.desktop" ];
        "x-scheme-handler/https" = ["zen-beta.desktop" "firefox.desktop" "chromium-browser.desktop" ];
        "x-scheme-handler/about" = ["zen-beta.desktop" "firefox.desktop" "chromium-browser.desktop" ];
        "x-scheme-handler/unknown" = ["zen-beta.desktop" "firefox.desktop" "chromium-browser.desktop" ];

        "text/txt"="org.kde.kate.desktop";
        "text/md"="org.kde.kate.desktop";
        "text/html"="org.kde.kate.desktop";
        "text/css"="org.kde.kate.desktop";
        "text/js"="org.kde.kate.desktop";
        "text/toml"="org.kde.kate.desktop";
        "text/conf"="org.kde.kate.desktop";
        "text/ini"="org.kde.kate.desktop";
        "text/plain"="org.kde.kate.desktop";
        "text/x-readme"="org.kde.kate.desktop";
        "text/calendar"="userapp-Thunderbird-IR3452.desktop";
        "image/png"="com.interversehq.qView.desktop";
        "image/gif"="com.interversehq.qView.desktop";
        "image/jpeg"="com.interversehq.qView.desktop";
        "image/avif" = "com.interversehq.qView.desktop";
        "image/bmp" = "com.interversehq.qView.desktop";
        "image/heif" = "com.interversehq.qView.desktop";
        "image/jpg" = "com.interversehq.qView.desktop";
        "image/pjpeg" = "com.interversehq.qView.desktop";
        "image/svg+xml" = "librewolf.desktop";
        "image/tiff" = "com.interversehq.qView.desktop";
        "image/x-bmp" = "com.interversehq.qView.desktop";
        "image/x-pcx" = "com.interversehq.qView.desktop";
        "image/x-png" = "com.interversehq.qView.desktop";
        "image/x-portable-anymap" = "com.interversehq.qView.desktop";
        "image/x-portable-bitmap" = "com.interversehq.qView.desktop";
        "image/x-portable-graymap" = "com.interversehq.qView.desktop";
        "image/x-portable-pixmap" = "com.interversehq.qView.desktop";
        "image/x-tga" = "com.interversehq.qView.desktop";
        "image/x-xbitmap" = "com.interversehq.qView.desktop";
        "video/mp4"="mpv.desktop";
        "video/mkv"="mpv.desktop";
        "video/x-matroska"="mpv.desktop";
        "message/rfc822"="userapp-Thunderbird-EKC552.desktop";
        "x-scheme-handler/mailto"="userapp-Thunderbird-EKC552.desktop";
        "x-scheme-handler/mid"="userapp-Thunderbird-EKC552.desktop";
        "x-scheme-handler/webcal"="userapp-Thunderbird-IR3452.desktop";
        "x-scheme-handler/webcals"="userapp-Thunderbird-IR3452.desktop";
      };
      addedAssociations = defaultApplications;
      };
    };
    # configFile = {
    #   "qt5ct/qt5ct.conf".text = ''
    #     [Appearance]
    #     icon_theme=${iconTheme.name}
    #     style=Breeze
    #     standard_dialogs=Default

    #     [Fonts]
    #     fixed="Fantasque Sans Mono"
    #     general="Alegreya Sans,14"
    #   '';
    #   "qt6ct/qt6ct.conf".text = ''
    #   [Appearance]
    #   icon_theme=${iconTheme.name}
    #   style=Breeze
    #   standard_dialogs=Default

    #   [Fonts]
    #   fixed="Fantasque Sans Mono"
    #   general="Alegreya Sans,13"
    #   '';

    # };
}
