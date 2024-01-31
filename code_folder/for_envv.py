from dotenv import load_dotenv
load_dotenv()
import os

host = os.environ.get("HOST")
port = int(os.environ.get("PORT"))
api_key = os.environ.get("OPENAI_API_KEY")