import os
import sys
import subprocess

def uninstall_all_packages():
    print("Starting uninstallation of all packages...")
    try:
        installed_packages = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze']).decode().split('\n')
    except subprocess.CalledProcessError as e:
        print(f"Error listing installed packages: {e}")
        return
    
    for package in installed_packages:
        if package:
            package_name = package.split('==')[0]
            try:
                subprocess.call([sys.executable, '-m', 'pip', 'uninstall', package_name, '-y'])
                print(f"Package {package_name} uninstalled successfully.")
            except Exception as e:
                print(f"Error uninstalling package {package_name}: {e}")

def clear_pip_cache():
    try:
        subprocess.call([sys.executable, '-m', 'pip', 'cache', 'purge'])
        print("Pip cache cleared successfully.")
    except Exception as e:
        print(f"Error clearing pip cache: {e}")

if __name__ == "__main__":
    uninstall_all_packages()
    clear_pip_cache()
    print("All packages uninstalled and cache cleared.")
