import os
import pandas as pd
from typing import List, Dict
from .Summarizer import summarize

class _FileManager:  
    def __init__(self, data_dir: str = 'Data', files_dir: str = 'Files'):
        self.data_dir = data_dir
        self.files_dir = files_dir
        self.db_file = os.path.join(self.data_dir, 'file_database.csv')
        self.df = self._load_database()

    def _load_database(self) -> pd.DataFrame:
        if os.path.exists(self.db_file):
            return pd.read_csv(self.db_file)
        else:
            return pd.DataFrame(columns=['filename', 'Embedding', 'Summary'])

    def _save_database(self):
        self.df.to_csv(self.db_file, index=False)

    def add_file(self, filename: str):
        if filename not in self.df['filename'].values:
            print(f"Adding file '{filename}' to the database...")
            print("Generating summary...")
            summary = summarize(filename)
            print("Summary generated successfully.")
            print("Generating embedding...")
            embedding_vector = None  # Placeholder for future embedding generation
            print("Embedding generated successfully.")
            new_row = pd.DataFrame({'filename': [filename], 'Embedding': [embedding_vector], 'Summary': [summary]})
            self.df = pd.concat([self.df, new_row], ignore_index=True)
            print("Saving database...")
            self._save_database()
            print(f"File '{filename}' added to the database successfully.")
        else:
            print(f"File '{filename}' already exists in the database.")

    def delete_file(self, filename: str):
        if filename in self.df['filename'].values:
            file_path = os.path.join(self.files_dir, filename)
            if os.path.exists(file_path):
                os.remove(file_path)
            self.df = self.df[self.df['filename'] != filename]
            self._save_database()
            print(f"File '{filename}' deleted from the database and file system.")
        else:
            print(f"File '{filename}' not found in the database.")

    def check_files(self) -> Dict[str, List[str]]:
        files_in_dir = set(os.listdir(self.files_dir))
        files_in_db = set(self.df['filename'])

        added_files = list(files_in_dir - files_in_db)
        deleted_files = list(files_in_db - files_in_dir)

        return {'added': added_files, 'deleted': deleted_files}

    def update_database(self):
        changes = self.check_files()
        
        if changes['added'] or changes['deleted']:
            print("The following changes were detected:")
            if changes['added']:
                print("Added files:", ', '.join(changes['added']))
            if changes['deleted']:
                print("Deleted files:", ', '.join(changes['deleted']))
            
            user_input = input("Do you want to update the database? (y/n): ").lower()
            if user_input == 'y':
                for file in changes['added']:
                    self.add_file(file) 
                for file in changes['deleted']:
                    self.delete_file(file)
                print("Database updated successfully.")
            else:
                print("Database update cancelled.")
        else:
            print("No changes detected. Database is up to date.")

FILE_MANAGER = _FileManager()
FILE_MANAGER.update_database()