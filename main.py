from backend.mcp.McpService import mcp

if __name__ == "__main__":
    mcp.run(transport='sse',host='0.0.0.0',port=8888,log_level='debug')
