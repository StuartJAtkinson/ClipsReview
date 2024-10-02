import os
from utils.download_vlc import download_vlc

def main():
    # Set the directory where VLC will be downloaded and extracted
    vlc_dir = os.path.join(os.path.dirname(__file__), "vlc")

    # Download and extract VLC
    try:
        download_vlc(vlc_dir)
    except Exception as e:
        print(f"Error during VLC setup: {e}")
        return

    print("VLC is ready to use.")

if __name__ == "__main__":
    main()