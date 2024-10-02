import os
import platform

def check_vlc_instance(base_dir):
    """Recursively check for VLC instance in the codebase folders."""
    vlc_found = False
    system = platform.system()

    # Determine the correct VLC library file name based on the system
    if system == "Windows":
        vlc_lib_files = ["libvlc.dll", "libvlccore.dll", "vlc.exe"]
    elif system == "Linux":
        vlc_lib_files = ["libvlc.so", "libvlccore.so", "vlc"]
    else:
        raise Exception(f"Unsupported platform: {system}")

    # Recursively search for VLC library files in the codebase folders
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file in vlc_lib_files:
                vlc_found = True
                vlc_path = os.path.join(root, file)
                print(f"VLC library found: {vlc_path}")

                # Load the VLC library
                import ctypes
                try:
                    ctypes.CDLL(vlc_path)
                    print("VLC library loaded successfully.")
                except Exception as e:
                    print(f"Failed to load VLC library: {e}")

    if not vlc_found:
        print("VLC library not found in the codebase folders.")

if __name__ == "__main__":
    codebase_dir = os.path.dirname(os.path.abspath(__file__))
    check_vlc_instance(codebase_dir)