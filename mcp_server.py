import os
from mcp.server.fastmcp import FastMCP

# Tạo app FastMCP
mcp = FastMCP("Superset AI Local", host="0.0.0.0", port=5008)

@mcp.tool()
def list_datasets() -> str:
    """Liệt kê các bảng và dataset hiện có trong hệ thống (Mock)."""
    # TODO: Khi có code Superset hoàn chỉnh, thêm logic import DAOs ở đây
    # from superset.app import create_app
    # app = create_app(); app.app_context().push()
    return "Danh sách datasets: 1. Sales_Data, 2. Marketing_Claims"

@mcp.tool()
def query_sql(sql: str) -> str:
    """Thực thi câu lệnh SQL (Mock)."""
    return f"Đã chạy SQL dưới quyền khai.dt: {sql}\nKết quả: [1000, 2000, 3000]"

if __name__ == "__main__":
    print("Starting Standalone MCP Server on port 5008...")
    # Chạy MCP server dạng SSE
    mcp.run("sse")
