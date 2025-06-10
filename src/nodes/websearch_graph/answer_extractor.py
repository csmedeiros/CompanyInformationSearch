import sys
sys.path.insert(0, r"C:\Users\202203369008\Documents\CompanyInformationSearch")
from src.llms import OPENAI
from pydantic import BaseModel, Field
from typing import List
from langchain.prompts import ChatPromptTemplate
from src.state import State
from selenium.webdriver import Chrome, ChromeOptions
from bs4 import BeautifulSoup


prompt = ChatPromptTemplate.from_messages([
    ("system", 
    """
    Your job is to extract the target information based on the web search results for the information.\n
    Will receive as input the target informatio and the web search results to output the answer in brazilian portuguese.\n
    If you can not find the answer in the results, you must output that the information has not been found.\n 
    """),
    ("user", "Target information: {target}\n\nWeb Search results:\n{results}\n")
])

chain = prompt | OPENAI

def extract_answer(state: State):
    answers = []
    for i, target in enumerate(state['targets']):
        res = chain.invoke({"target": target, "results": state['search_answers'][i]}).content
        answers.append(res)
    return {"answers": answers}