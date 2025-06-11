import sys
sys.path.insert(0, r"C:\Users\202203369008\Documents\CompanyInformationSearch")
from dotenv import load_dotenv
load_dotenv(".env")
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