import sys
import logging
from time import sleep
import requests
import os
from src.state import State

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

TAVILY_API_KEY = "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"
TAVILY_API_URL = "https://api.tavily.com/search"

def websearch(state: State):
    answers = []
    headers = {
        "content-type": "application/json",
        "api-key": TAVILY_API_KEY
    }

    for query in state['queries']:
        try:
            logger.info(f"Searching query: {query}")
            
            params = {
                "query": query,
                "search_depth": "advanced",
                "max_results": 3
            }
            
            response = requests.get(
                TAVILY_API_URL,
                headers=headers,
                params=params
            )
            response.raise_for_status()  # Raises an exception for bad status codes
            
            search_results = response.json()
            logger.info(f"Got response: {search_results}")
            answers.append(search_results)
            
            # Add a small delay between requests
            sleep(1)
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Request error for query '{query}': {str(e)}")
            answers.append({"error": str(e)})
        except Exception as e:
            logger.error(f"Error searching for query '{query}': {str(e)}")
            answers.append({"error": str(e)})
    
    return {"search_answers": answers}