import sys
sys.path.insert(0, r"C:\Users\202203369008\Documents\CompanyInformationSearch")
from dotenv import load_dotenv
load_dotenv(".env")
from langchain.prompts import PromptTemplate
from src.llms import OPENAI
from pydantic import BaseModel, Field
from src.state import State

# print(DuckDuckGoSearchRun().invoke("Quando o papa morreu?")):
# print(DuckDuckGoSearchResults().invoke("Quando o papa morreu?"))

from langchain.prompts import PromptTemplate

prompt = PromptTemplate.from_template(
    """
Você é um assistente especializado em gerar uma única query (consulta) de busca na web para o mecanismo de busca Tavily.

Sua tarefa é criar **uma única query altamente eficaz** para buscar uma informação específica sobre uma empresa na internet.

Descrição da empresa:
{description}

O ano-alvo para as informações é 2024 — leve isso em consideração ao formular a query.

A informação que deve ser buscada é a seguinte:
{target}

Regras para gerar a query:
- Gere **apenas uma query** que seja direta, clara e com alta chance de trazer exatamente a informação solicitada.
- Use **linguagem natural em português do Brasil**, como se estivesse fazendo a busca você mesmo no Google.
- Use termos comumente encontrados em sites confiáveis brasileiros (ex: portais de notícias, órgãos públicos, páginas institucionais).
- Certifique-se de que a query seja específica o suficiente para evitar resultados sobre empresas com nomes semelhantes.
- A query deve ter boa precisão sem ser excessivamente longa.

Formato de saída:
Uma única string representando a query.
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