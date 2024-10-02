import os
from utils.check_vlc import check_vlc_instance

def main():
    # Get the base directory of the codebase
    codebase_dir = os.path.dirname(os.path.abspath(__file__))

    # Check for VLC instance in the codebase folders
    check_vlc_instance(codebase_dir)

if __name__ == "__main__":
    main()