import os
import importlib
from typing import Dict, Callable


def load_tools_from_directory(directory: str) -> Dict[str, Callable]:
    """
    tools/ 디렉토리 내의 MCP 모듈들을 동적으로 로딩
    """
    tools = {}
    base_dir = os.path.dirname(
        os.path.dirname(os.path.dirname(__file__))
    )  # 프로젝트 루트
    tool_dir_path = os.path.join(base_dir, directory)

    for filename in os.listdir(tool_dir_path):
        if filename.endswith(".py") and not filename.startswith("__"):
            module_name = filename[:-3]
            module_path = f"agent.tools.{module_name}"  # 패키지 경로 기준 import
            module = importlib.import_module(module_path)
            tool_fn = getattr(module, module_name, None)
            if callable(tool_fn):
                tools[module_name] = tool_fn
            else:
                print(f"[WARN] '{module_name}.py'에서 '{module_name}()' 함수 없음")
    return tools
