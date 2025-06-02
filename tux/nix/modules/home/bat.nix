{pkgs, ...}: {
  programs.bat = {
    enable = true;
    config = {
      pager = "less -FR";
    };
    extraPackages = with pkgs.bat-extras; [
      batman # Read system manual pages (man) using bat as the manual page formatter.
      batpipe # A less (and bat) preprocessor for viewing more types of files in the terminal.
      batgrep
      prettybat # Pretty-print source code and highlight it with bat.
      batdiff # Diff a file against the current git index, or display the diff between two files.
      batwatch # Watch for changes in one or more files, and print them with bat.
    ];
  };
}
