import google.generativeai as genai

client = genai.GenerativeModel('gemini-1.5-flash')

prompt = open('Source/prompt.txt', 'r').read()

def summarize(filename: str) -> str:
	file = genai.upload_file(path=f"Files/{filename}", name="temp")
	response = client.generate_content([prompt, file])
	genai.delete_file(file.name)
	return response.text

