import os
import sys
from Source.FileManager import FILE_MANAGER

def main():
    # Check if the config file exists
    if not os.path.exists('config.py'):
        print("Error: config.py not found. Please create it from config.py.example.")
        sys.exit(1)

    # Import the configuration
    try:
        from config import GOOGLE_API_KEY
    except ImportError:
        print("Error: GOOGLE_API_KEY not found in config.py.")
        sys.exit(1)

    # Your main code logic here
    print("Starting the application...")

    # Add your application's main functionality here
    file_manager = FILE_MANAGER

if __name__ == "__main__":
    main()
