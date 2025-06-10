{pkgs, ...}: {
  programs.mpv = { # lightweight media player
    enable = true;
    scripts = with pkgs.mpvScripts; [
      mpris # Add support for media keybinds
      uosc # Feature-rich minimalist proximity-based UI
      thumbfast # High-performance on-the-fly thumbnailer for mpv
      visualizer # various audio visualization
      youtube-chat # overlay youtube chat on top of a video using yt-dlp
      youtube-upnext # Userscript that allows you to play 'up next'/recommended youtube videos
      twitch-chat # Show Twitch chat messages as subtitles when watching Twitch VOD with mpv.
      videoclip # Easily create videoclips with mpv
      # blacklistExtensions # Automatically remove entries based on extensions
      autodeint # Automatically deinterlace videos
      autoload # Automatically load playlist entries
      # chapterskip # Automatically skips chapters based on title
      # mpv-notify-send # send notifications with notify-send
      mpv-playlistmanager # Create and manage playlists
      mpv-discord # Cross-platform Discord Rich Presence integration for mpv with no external dependencies
      vr-reversal # Script for mpv to play VR video with optional saving of head tracking data
      sponsorblock-minimal # SponsorBlock with minimal deps
      skipsilence # Increase playback speed during silence
      reload # Manual & automatic relaoding of videos
      quality-menu # Switch video quality from YT on-the-go
      mpv-subtitle-lines # Skip to subtitle lines
      memo # REcent files menu
      evafast # Seeking and hybrid fastforwarding like VHS
      quack # Reduce audio volume after seeking
      autosub # Fully automatic subtitle downloading
      manga-reader # Title.
      mpv-image-viewer.minimap # Adds a minimap that displays the position of the image relative to the view
      mpv-image-viewer.ruler # Adds a ruler command that lets you measure positions, distances and angles in the image. Can be configured through ruler.conf
      # mpv-image-viewer.status-line # Adds a status line that can show different properties in the corner of the window
      mpv-image-viewer.freeze-window # By default, mpv automatically resizes the window when the current file changes to fit its size. This script freezes the window so that this does not happen
      mpv-image-viewer.image-positioning # Adds several high-level commands to zoom and pan
      occivink.crop # Crop the current video in a visual manner
      # webtorrent-mpv-hook # Torrent streamer
    ];
  };
}
