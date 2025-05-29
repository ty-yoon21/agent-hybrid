from typing import Dict, Callable, List
from agent.registry.tool_spec_loader import load_tools_from_directory
from agent.core.config import TOOL_SPEC_DIR


class ToolRegistry:
    """
    모든 MCP Tool의 메타 정보를 등록하고 검색하는 클래스
    """

    def __init__(self):
        self.tools: Dict[str, Callable] = {}

    def load(self, directory: str = TOOL_SPEC_DIR):
        self.tools = load_tools_from_directory(directory)

    def list_tools(self) -> List[str]:
        return list(self.tools.keys())

    def get_tool(self, name: str) -> Callable:
        return self.tools.get(name)

    def find_tool_by_keyword(self, keyword: str) -> List[str]:
        """
        키워드를 기준으로 Tool 이름에서 간단히 검색
        (향후 embedding + metadata 기반 hybrid search로 확장 가능)
        """
        return [tool for tool in self.tools if keyword.lower() in tool.lower()]
