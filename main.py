import os
import sys

# Create the Files directory if it doesn't exist
files_dir = 'Files'
if not os.path.exists(files_dir):
	os.makedirs(files_dir)
	print(f"Created '{files_dir}' directory.")
else:
	print(f"'{files_dir}' directory already exists.")

# Configure the Google API key
import google.generativeai as genai
from config import GOOGLE_API_KEY

genai.configure(api_key=GOOGLE_API_KEY)

# remaining imports
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

	query = input("Enter a query: ")

	results = file_manager.top_k_cosine_similarity(query)

	print(results)


if __name__ == "__main__":
	main()
