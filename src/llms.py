from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import os

OPENAI = ChatOpenAI(api_key=os.getenv("OPENAI_API_KEY"), model='gpt-4o', temperature=0.3)