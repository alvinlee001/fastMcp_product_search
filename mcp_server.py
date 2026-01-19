import os
import requests
from fastmcp import FastMCP

# 1. Instantiate FastMCP
# The name and description are used to identify the MCP server.
mcp = FastMCP(
    name="SemanticSearchClient",
    description="An MCP server that provides a tool to query an external semantic search API."
)

# 2. Configure the search service URL
# The tool will call this external HTTP endpoint for the search.
# It can be overridden by setting the SEARCH_SERVICE_URL environment variable.
SEARCH_SERVICE_URL = os.environ.get("SEARCH_SERVICE_URL", "http://localhost:8000/search")

# 3. Define the tool
@mcp.tool
def semantic_search(q: str) -> dict:
    """
    Performs a semantic search by querying an external search service.

    Args:
        q: The search query string.

    Returns:
        A dictionary containing the search results from the service.
    """
    print(f"Executing 'semantic_search' tool with query: '{q}'")
    print(f"Calling external search service at: {SEARCH_SERVICE_URL}")

    try:
        response = requests.get(SEARCH_SERVICE_URL, params={"q": q}, timeout=10)
        response.raise_for_status()  # Raise an exception for bad status codes
        results = response.json()
        print("Successfully received results from search service.")
        return results
    except requests.exceptions.RequestException as e:
        print(f"Error calling search service: {e}")
        # Return a structured error that an LLM can understand.
        return {"error": f"Failed to connect to the search service at {SEARCH_SERVICE_URL}. Details: {e}"}

# 4. Run the server
if __name__ == "__main__":
    print(f"Starting FastMCP server '{mcp.name}'...")
    print(f"Registered tool: 'semantic_search'")
    print(f"Search service URL: {SEARCH_SERVICE_URL}")
    print("The server is now running and exposing the tool via the MCP protocol.")
    mcp.run()