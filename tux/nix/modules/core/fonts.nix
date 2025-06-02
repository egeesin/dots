{
pkgs,
# pkgs-unstable,
 ... }: {
  fonts = {
    fontDir.enable = true;
    fontconfig.enable = true;
    packages = (with pkgs; [
      inter-nerdfont
      # fantasque-sans-mono
      # nerdfonts.symbols-only # attribute deosn't exist for some reason
      # nerdfonts # (Includes all patched fonts)
      commit-mono
      # twemoji-color-font
      # font-awesome 
      # ultimate-oldschool-pc-font-pack
      # twemoji-color-font   
      # gelasio # Font which is metric-compatible with Microsoft's Georgia
      comic-neue # Casual type face: Make your lemonade stand look like a fortune 500 company
      comic-relief # Font metric-compatible with Microsoft Comic Sans
      garamond-libre
      # alegreya-sans # Humanist sans serif family with a calligraphic feeling
      minecraftia # First we mine, then we craftia. Let's Minecraftia!
      xkcd-font # title.
      corefonts # Microsoft's TrueType core fonts for the Web
      open-fonts # Collection of beautiful free and open source fonts
      kreative-square # Fullwidth scalable monospace font designed specifically to support pseudographics, semigraphics, and private use characters
      nerd-fonts.symbols-only # (Only includes symbols) available in unstable/25.05
    # ]) ++ (with pkgs-unstable; [
    ]);
  };
}
