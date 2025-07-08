import os
import subprocess
import sys


def run_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        return True, result.stdout
    except subprocess.CalledProcessError as e:
        return False, e.stderr


def enable_spotlight():
    print("Enabling new Spotlight feature...")
    
    success, output = run_command("sudo mkdir -p /Library/Preferences/FeatureFlags/Domain")
    if not success:
        print(f"Error creating directory: {output}")
        return False
    
    command = "sudo defaults write /Library/Preferences/FeatureFlags/Domain/SpotlightUI.plist SpotlightPlus -dict Enabled -bool true"
    success, output = run_command(command)
    if not success:
        print(f"Error enabling Spotlight: {output}")
        return False

    print("New Spotlight and Launchpad has been enabled!")
    return True


def disable_spotlight():
    print("Disabling new Spotlight and Launchpad ...")
    
    success, output = run_command("sudo mkdir -p /Library/Preferences/FeatureFlags/Domain")
    if not success:
        print(f"Error creating directory: {output}")
        return False
    
    command = "sudo defaults write /Library/Preferences/FeatureFlags/Domain/SpotlightUI.plist SpotlightPlus -dict Enabled -bool false"
    success, output = run_command(command)
    if not success:
        print(f"Error disabling Spotlight: {output}")
        return False

    print("New Spotlight and Launchpad have been disabled!")
    return True


def get_user_choice():
    while True:
        print("\nSpotlight and Launchpad redesign Manager")
        print("=" * 30)
        choice = input("Would you like to (E)nable or (D)isable the new Spotlight and Launchpad? [E/D]: ").strip().upper()

        if choice in ['E', 'ENABLE']:
            return 'enable'
        elif choice in ['D', 'DISABLE']:
            return 'disable'
        else:
            print("Invalid input. Please enter 'E' for Enable or 'D' for Disable.")


def check_macos():
    if sys.platform != 'darwin':
        print(" This script is designed for macOS only.")
        return False
    return True


def main():
    if not check_macos():
        sys.exit(1)
    
    try:
        choice = get_user_choice()
        
        if choice == 'enable':
            success = enable_spotlight()
        else:
            success = disable_spotlight()
        
        if success:
            print("\nPlease restart your computer for the changes to take effect.")
        else:
            print("\nOperation failed. Please check the error messages above.")
            sys.exit(1)
            
    except KeyboardInterrupt:
        print("\n\nOperation cancelled by user.")
        sys.exit(0)
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
