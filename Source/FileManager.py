import os
import pandas as pd
import numpy as np
from typing import List, Dict
from .Summarizer import summarize
from .EmbeddingUtility import create_embedding

class _FileManager:  
	def __init__(self, files_dir: str = 'Files'):
		self.files_dir = files_dir
		self.db_file = 'file_database.json'  # Changed from .csv to .json
		self.df = self._load_database()

	def _load_database(self) -> pd.DataFrame:
		if os.path.exists(self.db_file):
			return pd.read_json(self.db_file)  # Changed from pd.read_csv to pd.read_json
		else:
			return pd.DataFrame(columns=['filename', 'Embedding', 'Summary'])

	def _save_database(self):
		self.df.to_json(self.db_file, orient='records', lines=False)

	def add_file(self, filename: str):
		if filename not in self.df['filename'].values:
			print(f"Adding file '{filename}' to the database...")
			print("Generating summary...")
			summary = summarize(filename)
			print("Summary generated successfully.")
			print("Generating embedding...")
			embedding_vector : np.ndarray = create_embedding(summary)
			print("Embedding generated successfully.")
			new_row = pd.DataFrame({'filename': [filename], 'Embedding': [embedding_vector], 'Summary': [summary]})
			self.df = pd.concat([self.df, new_row], ignore_index=True)
			print("Saving database...")
			print(f"File '{filename}' added to the database successfully.")
		else:
			print(f"File '{filename}' already exists in the database.")

	def delete_file(self, filename: str):
		if filename in self.df['filename'].values:
			file_path = os.path.join(self.files_dir, filename)
			if os.path.exists(file_path):
				os.remove(file_path)
			self.df = self.df[self.df['filename'] != filename]
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
				self._save_database()
			else:
				print("Database update cancelled.")
		else:
			print("No changes detected. Database is up to date.")

	def top_k_cosine_similarity(self, query: str, k: int = 5) -> List[str]:
		query_embedding = create_embedding(query)
		
		# Calculate cosine similarity between the query embedding and all embeddings in the database
		similarities = self.df['Embedding'].apply(lambda x: np.dot(query_embedding, x) / (np.linalg.norm(query_embedding) * np.linalg.norm(x)))

		# Handle edge case where k is greater than the number of entries
		k = min(k, len(self.df))
		
		# Get the top k entries based on similarity
		top_k_indices = similarities.argsort()[-k:][::-1]
		top_k_files = self.df.iloc[top_k_indices]
		top_k_files['similarity'] = similarities.iloc[top_k_indices]
		return top_k_files

FILE_MANAGER = _FileManager()
FILE_MANAGER.update_database()