This is customized fork based on [Disassembler0's](https://github.com/Disassembler0/Win10-Initial-Setup-Script) and [voruti's](https://github.com/voruti/Win10-Initial-Setup-Script) forks including my separate scripts for installing a preset of applications from Chocolatey and Scoop (based on klane's [dotfiles](https://github.com/klane/dotfiles/blob/master/scripts/install.ps1)).


## Quick Start

- Run init.cmd with Command Prompt (`cmd.exe`) as **administrator**.
- Run installScoop.ps1 (Non) with `powershell.exe` as **non-admin.** (Make sure PowerShell version is 5.1, higher or lower version are not guaranteed to work)
- Run installChoco.cmd with `powershell.exe` as **administrator**.

These scripts are tested on Windows 11 Pro 21H2.

&nbsp;

All detailed instructions and license information of original forks can be found in [here](https://github.com/Disassembler0/Win10-Initial-Setup-Script) and [here](https://github.com/voruti/Win10-Initial-Setup-Script)

# Important Notes for Further Development

- Nvim configuration path: `~/AppData/Local/nvim`/`:echo stdpath('config')` Plug.vim need detection for plugin path.
- 