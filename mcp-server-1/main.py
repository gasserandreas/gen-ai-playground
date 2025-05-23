from server import mcp

# Import tools so they get registered via decorators
import tools.csv_tools
import tools.parquet_tools

if __name__ == "__main__":
    mcp.run()
