# FastMCP Semantic Search Client

This project implements a `FastMCP` server that acts as a client to an external semantic search API. It exposes a `semantic_search` tool that can be called by a Large Language Model (LLM) or other MCP clients.

## Project Overview

The core of this project is `mcp_server.py`, which uses the `FastMCP` framework to create an MCP server. This server defines a single tool, `semantic_search`, which takes a search query and forwards it to a pre-existing REST API for processing.

## Key Technologies

*   **Python 3:** The programming language used for the project.
*   **FastMCP:** The framework used to create the MCP server and tools.
*   **Requests:** The library used to make HTTP calls to the external search API.

## Setup and Installation

To get the server running, follow these steps. It is highly recommended to use a Python virtual environment to manage dependencies.

1.  **Create a Virtual Environment:**
    Open your terminal in the project root directory and run the following command to create a virtual environment named `venv`:
    ```bash
    python3 -m venv venv
    ```

2.  **Activate the Virtual Environment:**
    Before installing dependencies, you need to activate the virtual environment.

    *   **On macOS and Linux:**
        ```bash
        source venv/bin/activate
        ```
    *   **On Windows:**
        ```bash
        .\venv\Scripts\activate
        ```
    Your terminal prompt should change to indicate that you are now in the `venv` environment.

3.  **Install Dependencies:**
    With the virtual environment active, install the required Python packages from `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```

## Running the Server

To run the FastMCP server, execute the `mcp_server.py` script. You must provide the URL of your existing semantic search API by setting the `SEARCH_SERVICE_URL` environment variable.

```bash
SEARCH_SERVICE_URL="http://your-api-endpoint/search" python mcp_server.py
```

The server will start and register the `semantic_search` tool, which will then be available for MCP clients to use.

## Project Structure

*   `mcp_server.py`: The main application file containing the FastMCP server and the `semantic_search` tool definition.
*   `requirements.txt`: A list of the Python dependencies required for this project.
*   `GEMINI.md`: This file, providing context and documentation for the project.
*   `.idea/`: Directory for JetBrains IDEs project-specific settings.