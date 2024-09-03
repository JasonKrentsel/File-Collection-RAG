import google.generativeai as genai
import numpy as np

def create_embedding(text: str) -> np.ndarray:
    embedding = genai.embed_content(model="models/text-embedding-004", content=text)['embedding']
    return np.array(embedding)
