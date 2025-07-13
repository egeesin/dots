{host, ...}: {
  imports = [
    ../../host/${host}
    ../../module/drivers
    ../../module/core
  ];
  # Enable GPU Drivers
  drivers.amdgpu.enable = false;
  drivers.nvidia.enable = true;
  vm.guest-services.enable = false;
}
