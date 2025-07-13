{host, ...}: {
  imports = [
    ../../host/${host}
    ../../module/driver
    ../../module/core
  ];
  # Enable GPU Drivers
  drivers.amdgpu.enable = true;
  drivers.nvidia.enable = false;
  vm.guest-services.enable = false;
}
