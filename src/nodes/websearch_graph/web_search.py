import sys
import logging
from time import sleep
from tavily import TavilyClient
from src.state import State

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

client = TavilyClient(api_key="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")

def websearch(state: State):
    answers = []
    for query in state['queries']:
        try:
            logger.info(f"Searching query: {query}")
            response = client.search(
                query=query,
                search_depth="advanced",
                max_results=3
            )
            logger.info(f"Got response: {response}")
            answers.append(response)
            # Add a small delay between requests
            sleep(1)
        except Exception as e:
            logger.error(f"Error searching for query '{query}': {str(e)}")
            answers.append({"error": str(e)})
    
    return {"search_answers": answers}