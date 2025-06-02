{pkgs, ...}: {
  environment.systemPackages = with pkgs; [
    shopify-cli
  ];
}
