---
orphan: true
---
# BitLocker Instructions for Unclassified Laptops

BitLocker is a full volume encryption feature included with Microsoft Windows. It is designed to protect data by
providing encryption for entire volumes. Drive encryption is a security requirement mandated by Defence Information
Security.

When appropriately used, Microsoft BitLocker and BitLocker To Go may be used to reduce the physical storage and handling
requirements of storage media classified PROTECTED (and below) to UNCLASSIFIED. See
[this page](https://www.cyber.gov.au/publications/epl/microsoft-bitlocker-and-bitlocker-go) for more details.

The process below is adapted from "BitLocker instructions for unclassified laptops" prescribed by Matt Thyer and
Christos Sioutis. This was retrieved from the GovTeams channel 'DST WCSD Int. Combat Cloud > Tools and Infrastructure >
Files' on 22 July 2020. The instructions have been followed, verified and translated into this Markdown document,
and are accurate at time of writing - September 2020 Windows 10 Version 1909 (OS build 18363.1082).

## Prepare Security Group Policies

1) Decrypt the drive (If Previously Encrypted)

    If BitLocker is already enabled for main system drive, you'll need to turn it off (decrypt the drive) and start
    again because the keys will have been potentially compromised.

    - Open Windows Explorer, right-clicking the C-drive and chose "Manage BitLocker"
    - Choose "Turn off BitLocker".

2) Run group policy editor

    - `Start → Run → gpedit.msc`

3) Change Encryption Method to AES 256

    Note if the drive is already encrypted, you'll need to decrypt and re-encrypt for this setting to take effect, which
   should be done regardless.

    - Go to Computer Configuration, Administrative Templates, Windows Components, **BitLocker Drive Encryption**.
    - Open 'Choose drive encryption method and cipher strength (Windows 8...)'.
      - Enable it.
      - Set to AES 256.
      - Close dialog.
    - Open 'Choose drive encryption method and cipher strength (Windows 10...)'.
      - Enable it.
      - Set to 'XTS-AES 256' for 'OS' and 'Fixed drives'.
      - Set to 'AES-CBC 256' for 'Removable drives'.

4) Set to Allow Pre-Boot Keyboard on Slates (e.g. Microsoft Surface Devices)

    - Go to Computer Configuration, Administrative Templates, Windows Components, BitLocker Drive Encryption,
     **Operating System Drives**.
    - Open Enable use of BitLocker authentication requiring pre-boot keyboard input on slates.
      - Enable it.
      - Close dialog.

5) Set 13 Digit Minimum PIN Strength

    - Still in Computer Configuration, Administrative Templates, Windows Components, BitLocker Drive Encryption,
     **Operating System Drives**.
    - Open Configure minimum PIN length for startup.
      - Enable it.
      - Set to 13 character minimum.
      - Close dialog.

6) Force Full-Drive Encryption on System Drive

    - Still in Computer Configuration, Administrative Templates, Windows Components, BitLocker Drive Encryption,
     **Operating System Drives**.
    - Open 'Enforce drive encryption type on operating system drives'.
      - Enable it.
      - Set to 'Full encryption'.
      - Close dialog.

7) Force Full-Drive Encryption on Additional Fixed Data Drives

    - Still in Computer Configuration, Administrative Templates, Windows Components, BitLocker Drive Encryption,
      **Fixed Data Drives**.
    - Open 'Enforce drive encryption type on fixed data drives'.
      - Enable it.
      - Set to Full encryption.
      - Close dialog.

8) Enforce Passwords for Fixed Data Drives

    - Still in Computer Configuration, Administrative Templates, Windows Components, BitLocker Drive Encryption,
      **Fixed Data Drives**.
    - Open 'Configure use of passwords for fixed data drives'.
      - Enable it.
      - Check 'Require password for fixed data drives'.
      - Select 'Allow password complexity' in the drop-down box. The require option is for enforcing that the password
        fits requirements excluding the minimum password length (such as using numbers, special characters,
        uppercase/lowercase etc.). It's worth considering that a long and memorable password is more secure than a short
        highly complex password that is hard to remember... (<https://xkcd.com/936/>).
      - If you do wish to enforce password complexity, go to Computer Configuration, Windows Settings, Security
        Settings, Account Policies, **Password Policy**.
         - Enable 'Passwords must meet complexity requirements'.
         - Close dialog.
    - Select 13 as the minimum password length.
    - Click 'Apply', then 'OK'.

9) Enforce the TPM+PIN Option

    - Go to Computer Configuration, Administrative Templates, Windows Components, BitLocker Drive Encryption,
     **Operating System Drives**.
    - Open 'Require additional authentication at startup'.
      - Enable it.
      - The option "Allow BitLocker without a compatible TPM" can remain checked.
      - Under 'Configure TPM startup PIN:', select 'Require startup PIN with TPM'.
    - Change all the other options to 'Do not allow...' (failure to do this will prevent BitLocker setup from starting
      due to conflicting settings).
    - Close dialog.

    Note: If above options come up as conflicting, instead use:

    - Allow TPM.
    - Allow startup PIN with TPM.
    - Allow startup key with TPM.
    - Allow startup key and PIN with TPM.

10) Disable Sleep Mode

    - Go to Computer Configuration, Administrative Templates, System, Power Management, *Sleep Settings*.
    - Set two settings as follows:
      - Allow Standby States (S1-S3) When Sleeping (Plugged In) -- Disabled.
      - Allow Standby States (S1-S3) When Sleeping (On Battery) -- Disabled.

11) Set Maximum Logon Attempts

    - Go to Computer Configuration, Windows Settings, Security Settings, Local Policies, **Security Options**.
      - Under "Interactive logon: Machine account lockout threshold", set "invalid logon attempts" to **8**.

    This will cause BitLocker to enter recovery mode if the Windows user password is entered incorrectly eight times in
    a row.

12) Set User Account Controls

    - Go to Computer Configuration, Windows Settings, Security Settings, Local Security Policy, Local Policies,
     **Security Options**.
      - User Account Control: Use Admin Approval Mode for the built-in Administrator account - Enabled.
      - User Account Control: Behaviour of the elevation prompt for administrators in Admin Approval Mode - Prompt for
        Credentials.
      - User Account Control: Behaviour of the elevation prompt for standard users - Prompt for Credentials.
      - User Account Control: Detect application installations and prompt for elevation - Enabled.
      - User Account Control: Only elevate executable files that are signed and validated - Enabled (**NOTE:** keep
        disabled if installing unsigned open source software).
      - User Account Control: Run all administrators in Admin Approval Mode - Enabled.

13) Finish Policy Updates

    - Close group policy editor.
    - Run `gpupdate` on the command line.

14) Restart the Computer

    If a restart is not performed, the BIOS, MBR & OS tamper detection system of the TPM may get a non-clean snapshot of
    the machine's initial state and lock-out on reboot, requiring use of the recovery key to get back in.

## Encrypt Computer Drive(s)

Note - If BitLocker is already enabled for the main drive, you'll need to turn it off (decrypt the drive) and start
again because the keys will have been potentially compromised. Instructions to do this are at top of document.

1) Setting the PIN

   - Open Windows Explorer, right-clicking the C-drive and chose "Turn on BitLocker".
   - Set your PIN
   - Type your chosen PIN; numbers only - unless your machine doesn't have a TPM, in which case go with a strong
     password.
   - Enter it again to confirm.
   - No need to write your PIN down; if you forget it then the recovery key can get you back in.
   - If you don't have a TPM you *might* get stuck at this point. Try to pick a strong, enhanced password should be used
     *instead of a simple 7 digit PIN* (noting that on some keyboards, enhanced characters aren't available pre-boot!).
   - Let the wizard auto-select the Recovery Key password (and TPM Owner if it asks).

2) Store a Copy of the Recovery Key

   - Print 1 hard-copy of the Recovery Key (and TPM Owner if it offers), plus one electronic copy on the USB key.
   - Regarding the screen where BitLocker offers to save or print the recovery key, it stays on that screen until you
     click next, so you can choose multiple options.
   - Keep one hard copy and the USB key in a safe place you can get to - ideally, literally in a safe. The hard copy is
     in case the USB key dies; the electronic copy on the USB key is easier to use if you need it.
   - Alternatively, use the print option to save to PDF and then save or upload this document somewhere secure such as
     your GovTeams OneDrive for safe keeping before proceeding with encryption.

3) Start Encryption

   - Select "Full Drive Encryption". Do not select used-space-only encryption as deleted files are not protected.
      - Note, you may not get asked this question due to group policy setting from previous section.
   - Select 'Run BitLocker system check'
   - Go! It'll reboot, then automatically start encrypting. Once you're logged back in you can see progress via the
     system tray.
   - Reboot and check you can get back in!

4) Notes for Tablets

   - If you're using a slate/tablet with a detachable keyboard with Windows 8, you need to attach the keyboard before
     you power up. Under Windows 10, there is an on-screen keyboard you can use if your keyboard is detached.
   - If you get stuck with the keyboard thing on a Surface Pro, there is apparently some trick where you hold the volume
     down key while booting up.

5) Changing the PIN

   - Change your PIN any time by running `manage-bde --changepin c:` on the command line as Administrator.
      - To run as admin:
         - Press the 'Start' button
         - Type `cmd` in the prompt
         - Right-click the Command Prompt option that appears
         - Click 'Run as Administrator'.
   - Alternatively, change via the Manage BitLocker GUI.

6) Finishing Up

   - Don't travel anywhere until the background encryption process is complete. Could take days. Took a couple of days
     on a 256GB SSD in a circa 2014 Surface Pro 2. Significantly faster on a Surface Pro 3.
   - How to tell: run `manage-bde --status` on the command line as administrator.

7) Encrypt Fixed DATA Drives

   - Open Windows Explorer, right-clicking the C-drive and chose 'Turn on BitLocker'.
   - Set a strong encryption password.
   - Keep a copy of the recovery key.
