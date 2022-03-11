---
orphan: true
---
# Installing Tactical Console on Windows OS

These instructions will guide a user through creating a virtual Linux Ubuntu environment on a Windows 10 host machine
using VirtualBox. This becomes the environment in which other Integrated Centre services may be deployed and operated.

These instructions are provided under the following assumptions:
- Running Windows 10 Operating System. Earlier Windows versions are unsupported and untested.
- BitLocker has been configured, as detailed in [this readme](windows_bitlocker_instructions.md).

## Virtual Machine Installation & Configuration

1) Download an Ubuntu image

   - Navigate to https://releases.ubuntu.com/.
   - Identify an appropriate, stable `(i.e. xx.04)` Ubuntu release at the top of the page and click on it.
   - Select the Desktop image and save the ISO file to the local machine.

2) Download and Install VirtualBox

   - Navigate to https://www.virtualbox.org/wiki/Downloads.
   - Locate the latest `(i.e. 6.x.x)` VirtualBox platform packages section.
   - Select ‘Windows hosts’ to download latest version executable.
   - Once download is completed, proceed with VirtualBox installation process.

3) Create a new VirtualBox Virtual Machine

   - In toolbar menu, select 'Machine' > 'New...'.
   - Name the VM 'Ubuntu ...' or 'UB ...' to correctly populate the remaining fields.
   - Set appropriate memory allocation `(i.e. 4096-8192MB)`, and click 'Next'.
   - Select 'Create a virtual hard disk now' and click 'Create'.
   - Leave on 'VDI (VirtualBox Disk Image)' and click 'Next'.
   - Select 'Fixed size' and click 'Next'.
   - Set hard disk size `(i.e. 10-20GB)`, and click 'Create'.
   - Once VM setup is complete and visible in VirtualBox menu, select VM and click 'Settings' to update the following:
     - 'System' > 'Processor' > Set Processor count to 2-4 CPUs.
     - 'Display' > Set Video Memory to 64-128 MB.
     - Click 'OK'.

4) Install Ubuntu Operating System

   - Select the newly created VM in VirtualBox and click 'Start'.
   - Select your Ubuntu image from the drop-down and click 'Start'.
     - If the Ubuntu image is not available here, click the folder icon and location your image file manually.
   - Select preferred language and click 'Install Ubuntu'.
   - Select keyboard layout and click 'Continue'.
   - Select 'Minimal Installation' and leave other settings as they are. Click 'Continue'.
   - Leave on 'Erase disk and install Ubuntu' and click 'Install Now', and the 'Continue' at the prompt.
   - Set timezone and click 'Continue'.
   - Input appropriate login credentials and click 'Continue'.
   - Click 'Restart Now', when prompted.
      - If prompted to remove disk, select 'Devices' > 'Optical Drive' > 'Remove disk from Virtual Drive'.
   - Skip creation of online account.
   - Click 'Next' or 'Done' at remaining prompts (No inputs required).

5) Perform System Updates

   There will likely be pending updates following installation of a new Operating System. When prompted, select 'Install
   Now' and restart Ubuntu as required.

6) Install Guest Additions

   Installation of 'Guest Additions' will allow for higher screen resolution, and other features that may be required,
   such as sharing folders with the Windows host OS.

   - In the VirtualBox window select 'Devices' > 'Insert Guest Additions CD Image...'.  
   - Click 'Run', when prompted in the Ubuntu desktop screen.
   - Press the return key, when prompted.
   - In the VirtualBox window select 'Machine' > 'Reset'.

   The video resolution for the VM can now be increased in the VirtualBox menu 'Machine' > 'Virtual Screen 1'.

7) Install Required Applications

   - From Ubuntu desktop screen, click 'Show Applications' and open 'Terminal'.
   - Enter the below commands in to the terminal to install required applications.
   - Update package tool: `sudo apt-get update && sudo apt-get upgrade`.
   - Install Git: `sudo apt-get install git`.
   - Install Chromium browser, installed from the 'Show Applications' menu.

## Virtual Machine Setup via Vagrant

HashiCorp Vagrant is a tool for building and managing virtual machine environments. The Vagrantfile to automate the
above workflow has been included in this directory within the repository. Usage instructions are located as comments
within the Vagrantfile itself (open as a text file to view).

More information about Vagrant is accessible via their [website](https://www.vagrantup.com/).
