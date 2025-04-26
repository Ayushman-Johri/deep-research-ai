from langchain_community.tools.tavily_search import TavilySearchResults

def get_tavily_tool():
    return TavilySearchResults(k=5)  # Fetch 5 search results per query
