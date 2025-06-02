{
  pkgs,
  host,
  options,
  ...
}: {
  networking = {
    hostName = "${host}"; # Define your hostname.
    nameservers = ["127.0.0.1" "::1"];
    # Pick only one of the below networking options.
    # wireless.enable = true;  # Enables wireless support via wpa_supplicant.
    networkmanager.enable = true;  # Easiest to use and most distros use this by default.

    # https://www.ntppool.org/en/use.html
    # timeServers = options.networking.timeServers.default ++ ["pool.ntp.org"];
    timeServers = options.networking.timeServers.default ++ ["tr.pool.ntp.org"];

    # Open ports in the firewall.
    firewall = {
      enable = true;
      allowedTCPPorts = [
        22
        80
        443
        59010
        59011
        8080
        3000
        3001
      ];
      allowedUDPPorts = [
        59010
        59011
      ];
    };

    
  
    # Configure network proxy if necessary
    # proxy.default = "http://user:password@proxy:port/";
    # proxy.noProxy = "127.0.0.1,localhost,internal.domain";
  };
  environment.systemPackages = with pkgs; [
    networkmanagerapplet
  ];
}
