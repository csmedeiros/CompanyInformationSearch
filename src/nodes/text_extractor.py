import sys
sys.path.insert(0, r"C:\Users\202203369008\Documents\CompanyInformationSearch")
from selenium.webdriver import Chrome, ChromeOptions
from dotenv import load_dotenv
load_dotenv(".env")
from time import sleep
from bs4 import BeautifulSoup
from src.llms import OPENAI
from src.state import State

url = "https://globo.com"

options = ChromeOptions()
options.add_argument("--headless")
webdriver = Chrome(options=options)

def extract_text(state: State):
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

    # print(splited_dom)
    # for i in splited_dom:
    #     print(len(i))
    return {"main_page_text": cleaned_dom}

# print(f"{cleaned_dom}\n\n\n{description}")