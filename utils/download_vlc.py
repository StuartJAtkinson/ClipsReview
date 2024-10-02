import os
import urllib.request
import zipfile
import platform
import time

def download_vlc(vlc_dir, retries=3):
    """Download and extract VLC binaries to the specified directory."""
    system = platform.system()
    arch = platform.architecture()[0]

    # Determine the correct URL based on system and architecture
    if system == "Windows":
        if arch == "64bit":
            vlc_url = "https://get.videolan.org/vlc/3.0.18/win64/vlc-3.0.18-win64.zip"
        else:
            vlc_url = "https://get.videolan.org/vlc/3.0.18/win32/vlc-3.0.18-win32.zip"
    elif system == "Linux":
        vlc_url = "https://get.videolan.org/vlc/3.0.18/linux/vlc-3.0.18-linux.zip"
    else:
        raise Exception(f"Unsupported platform: {system}")

    zip_path = os.path.join(vlc_dir, "vlc.zip")
    
    if not os.path.exists(vlc_dir):
        os.makedirs(vlc_dir)

    # Download VLC binaries with retry logic
    for attempt in range(retries):
        try:
            print(f"Downloading VLC binaries (attempt {attempt + 1})...")
            urllib.request.urlretrieve(vlc_url, zip_path)
            if verify_download(zip_path):
                print(f"Download successful.")
                break
            else:
                print(f"Download incomplete or corrupt. Retrying...")
        except Exception as e:
            print(f"Error during download: {e}")
            time.sleep(2)  # Wait before retrying
    else:
        raise RuntimeError("Failed to download VLC binaries after multiple attempts.")

    # Extract VLC binaries
    print("Extracting VLC...")
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(vlc_dir)
    os.remove(zip_path)
    print("VLC setup complete.")

def verify_download(zip_path):
    """Verify if the downloaded file is valid."""
    try:
        with open(zip_path, 'rb') as f:
            if f.read(512):  # Read the first 512 bytes to check if it's a valid zip file
                return True
    except Exception as e:
        print(f"Verification failed: {e}")
    return False
