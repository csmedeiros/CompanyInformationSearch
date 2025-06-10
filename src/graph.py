import sys
sys.path.insert(0, r"C:\Users\202203369008\Documents\CompanyInformationSearch")
from langgraph.graph import StateGraph, START, END
from src.state import State
from src.nodes.text_extractor import extract_text
from src.nodes.description_extractor import extract_description
from src.nodes.websearch_graph.query_generator import generate_queries
from src.nodes.websearch_graph.web_search import websearch
from src.nodes.websearch_graph.answer_extractor import extract_answer

graph_builder = StateGraph(State)
graph_builder.add_node("extract_text", extract_text)
graph_builder.add_node("extract_description", extract_description)
graph_builder.add_edge(START, "extract_text")
graph_builder.add_edge("extract_text", "extract_description")
graph_builder.add_node("generate_queries", generate_queries)
graph_builder.add_edge("extract_description", "generate_queries")
graph_builder.add_node("web_search", websearch)
graph_builder.add_edge("generate_queries", "web_search")
graph_builder.add_node("extract_answers", extract_answer)
graph_builder.add_edge("web_search", "extract_answers")
graph_builder.add_edge("extract_answers", END)

graph = graph_builder.compile()
input_state = {"url": "https://www.globo.com", "targets": ["if the company is publicly traded or not", "the company's revenue", "the company's number of employees"]}

res = graph.invoke(input_state)
print(res)
print("\n\n\n\n\n\n"+graph.get_graph().draw_mermaid()+"\n\n\n\n")
print(f"Capital aberto ou fechado: {res['answers'][0]}\n\nFaturamento: {res['answers'][1]}\nNumero de funcionarios: {res['answers'][2]}")