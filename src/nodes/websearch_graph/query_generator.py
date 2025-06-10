import sys
sys.path.insert(0, r"C:\Users\202203369008\Documents\CompanyInformationSearch")
from dotenv import load_dotenv
load_dotenv(".env")
from langchain.prompts import PromptTemplate
from langchain_community.tools import DuckDuckGoSearchResults
import json
from duckduckgo_search import DDGS
from src.llms import OPENAI
from pydantic import BaseModel, Field
from src.state import State

# print(DuckDuckGoSearchRun().invoke("Quando o papa morreu?")):
# print(DuckDuckGoSearchResults().invoke("Quando o papa morreu?"))

prompt = PromptTemplate.from_template(
    """
    You are an assistant that generate queries for web search with DuckDuckGO SE.\n
    Your queries will be used to gather information in the web about a company.\n
    The company description is:\n{description}\n
    I know your training data is until 2023, but consider the year of 2024 for the queries.
    The target information that the queries must retrieve is {target}.\n"
    The queries must retrieve only the target information, DO NOT query anything else.\n
    Consider the description to ensure the information retrieved are really about the specified company\n
    You can generate more than one query and maximum of 5 queries.\n
    Minimize the number of queries. Generate more than one query only if you judge necessary to retrieve better results.\n
    The queries must be in brazilian portuguese language.\n
    """
)

class QueryList(BaseModel):
    query: str = Field(description="A query that will be used to retrieve information about a company")

chain = prompt | OPENAI.with_structured_output(QueryList)

def generate_queries(state: State):
    queries = []
    for target in state['targets']:
        res = chain.invoke({"description": state['company_description'], "target": target}).query
        queries.append(res)
    return {"queries": queries}