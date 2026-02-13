import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv('d:/NexusSignal/.env')
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

model = genai.GenerativeModel('gemini-2.0-flash')
try:
    response = model.generate_content("Hello, this is a test. Reply with 'READY'.")
    print(response.text)
except Exception as e:
    print(f"FAILED: {e}")
