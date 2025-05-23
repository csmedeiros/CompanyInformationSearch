import sys
sys.path.insert(0, r"C:\Users\caiosmedeiros\Documents\Ibmec\Metodos e Aplicacoes de IA\CompanyInformationSearch")
from selenium.webdriver import Chrome, ChromeOptions
from time import sleep
from bs4 import BeautifulSoup
from src.llms import OPENAI

url = "https://globo.com"

options = ChromeOptions()
options.add_argument("--headless")
webdriver = Chrome(options=options)
def get_dom(url):
    webdriver.get(url)
    h = webdriver.page_source
    soup = BeautifulSoup(h, "html.parser")
    webdriver.close()
    return soup

def clean_dom(dom):
    soup = dom
    soup.get("body")
    for script in soup(["script", "noscript", "style"]):
        script.extract()
    soup = soup.get_text("\n")
    soup = "\n".join(line.strip() for line in soup.splitlines())  
    return soup

def split_dom(dom, max_len:int):
    return [dom[i: i+max_len] for i in range(0, len(dom), max_len)]

dom = get_dom(url)
cleaned_dom = clean_dom(dom)
splited_dom = split_dom(cleaned_dom, 2000)

print(splited_dom)
for i in splited_dom:
    print(len(i))

# description = OPENAI.invoke(f"Seu dever é extrair a partir de um html uma descrição da empresa.\nhtml:\n{soup}").content
# print(f"\n\n\n{description}")