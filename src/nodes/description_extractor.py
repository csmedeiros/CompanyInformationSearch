import sys
sys.path.insert(0, r"C:\Users\202203369008\Documents\CompanyInformationSearch")
from src.llms import OPENAI
from src.state import State

def extract_description(state: State):
    description = OPENAI.invoke(f"Seu dever é extrair a partir de um html uma descrição da empresa. Descreva o que a empresa faz, qual o mercado que ela pertence, quais os diferentes serviços que ela presta e seu aparente público alvo.\nhtml:\n{state['main_page_text']}").content
    return {"company_description": description}