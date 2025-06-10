import sys
sys.path.insert(0, r"C:\Users\202203369008\Documents\CompanyInformationSearch")
from duckduckgo_search import DDGS
from src.state import State
from time import sleep
from tavily import TavilyClient

client = TavilyClient(api_key="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")
# res = client.search("Qual o faturamento da Globo.com?")
# print(res)

def websearch(state: State):
    answers = []
    for query in state['queries']:
        answers.append(client.search(query))
    return {"search_answers": answers}