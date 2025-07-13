#!/usr/bin/env bash
# Based on https://gitlab.com/Zaney/zaneyos/-/blob/main/install-zaneyos.sh

if [ -n "$(grep -i nixos < /etc/os-release)" ]; then
  echo "Verified this is NixOS."
  echo "-----"
else
  echo "This is not NixOS or the distribution information is not available."
  exit
fi

if command -v git &> /dev/null; then
  echo "Git is installed, continuing with installation."
  echo "-----"
else
  echo "Git is not installed. Please install Git and try again."
  echo "Example: nix-shell -p git"
  exit
fi

echo "Default options are in brackets []"
echo "Just press enter to select the default"
sleep 2

echo "-----"

echo "Ensure In Home Directory"
cd || exit

echo "-----"

read -rp "Enter your new hostname: [ default ] " hostName
if [ -z "$hostName" ]; then
  hostName="default"
fi

echo "-----"

read -rp "Enter your hardware profile (GPU)
Options:
[ nvidia ]
vm
Please type out your choice: " profile
if [ -z "$profile" ]; then
  profile="nvidia"
fi

echo "-----"

# backupname=$(date "+%Y-%m-%d-%H-%M-%S")
# if [ -d "zaneyos" ]; then
#   echo "ZaneyOS exists, backing up to .config/zaneyos-backups folder."
#   if [ -d ".config/zaneyos-backups" ]; then
#     echo "Moving current version of ZaneyOS to backups folder."
#     mv "$HOME"/zaneyos .config/zaneyos-backups/"$backupname"
#     sleep 1
#   else
#     echo "Creating the backups folder & moving ZaneyOS to it."
#     mkdir -p .config/zaneyos-backups
#     mv "$HOME"/zaneyos .config/zaneyos-backups/"$backupname"
#     sleep 1
#   fi
# else
#   echo "Thank you for choosing ZaneyOS."
#   echo "I hope you find your time here enjoyable!"
# fi

echo "-----"

echo "Cloning & entering .dots repository"
git clone https://github.com/egeesin/dots.git
cd .dots || exit
mkdir host/"$hostName"
cp host/default/*.nix host/"$hostName"
installusername=$(echo $USER)
git config --global user.name "$installusername"
# git config --global user.email "$installusername@gmail.com" # it's too assuming
git add .
git config --global --unset-all user.name
git config --global --unset-all user.email
sed -i "/^\s*host[[:space:]]*=[[:space:]]*\"/s/\"\(.*\)\"/\"$hostName\"/" ./flake.nix
sed -i "/^\s*profile[[:space:]]*=[[:space:]]*\"/s/\"\(.*\)\"/\"$profile\"/" ./flake.nix


read -rp "Enter your keyboard layout: [ us ] " keyboardLayout
if [ -z "$keyboardLayout" ]; then
  keyboardLayout="us"
fi

sed -i "/^\s*keyboardLayout[[:space:]]*=[[:space:]]*\"/s/\"\(.*\)\"/\"$keyboardLayout\"/" ./host/$hostName/variables.nix

echo "-----"

# read -rp "Enter your console keymap: [ us ] " consoleKeyMap
# if [ -z "$consoleKeyMap" ]; then
#   consoleKeyMap="us"
# fi
# sed -i "/^\s*consoleKeyMap[[:space:]]*=[[:space:]]*\"/s/\"\(.*\)\"/\"$consoleKeyMap\"/" ./host/$hostName/variables.nix

echo "-----"

sed -i "/^\s*username[[:space:]]*=[[:space:]]*\"/s/\"\(.*\)\"/\"$installusername\"/" ./flake.nix

echo "-----"

echo "Generating The Hardware Configuration"
sudo nixos-generate-config --show-hardware-config > ./nix/host/$hostName/hardware.nix

echo "-----"

echo "Setting Required Nix Settings Then Going To Install"
NIX_CONFIG="experimental-features = nix-command flakes"

echo "-----"

sudo nixos-rebuild switch --flake ~/.dots#${profile}
