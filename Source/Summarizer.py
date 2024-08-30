import google.generativeai as genai
from config import GOOGLE_API_KEY

genai.configure(api_key=GOOGLE_API_KEY)
client = genai.GenerativeModel('gemini-1.5-flash')

prompt = open('Source/prompt.txt', 'r').read()

def summarize(filename: str) -> str:
    file = genai.upload_file(path=f"Files/{filename}", name="temp")
    response = client.generate_content([prompt, file])
    genai.delete_file(file.name)
    return response.text

