from agent.registry.tool_registry import ToolRegistry
from agent.services.tool_executor import execute_tool
from agent.core.prompt import SYSTEM_PROMPT, USER_PROMPT_TEMPLATE
from agent.models.schema import InferRequest, InferResponse, StepResult
import time

# MCP Tool을 등록하고 관리하는 객체
tool_registry = ToolRegistry()
tool_registry.load(directory="agent/tools")


def run_reasoning_pipeline(request: InferRequest) -> InferResponse:
    query = request.query
    steps = []
    tools_used = []

    # 1. 기사 검색
    step_name = "기사 검색"
    steps.append(StepResult(step=step_name, status="진행중"))
    search_fn = tool_registry.get_tool("search_articles")
    search_result = execute_tool(search_fn, query)
    steps[-1].status = "완료"
    steps[-1].result = f"{len(search_result)}건 검색됨"
    tools_used.append("search_articles")
    time.sleep(0.5)

    # 2. 본문 추출
    step_name = "본문 추출"
    steps.append(StepResult(step=step_name, status="진행중"))
    extract_fn = tool_registry.get_tool("extract_text_from_url")
    extracted_text = execute_tool(extract_fn, search_result[0])
    steps[-1].status = "완료"
    steps[-1].result = f"본문 길이: {len(extracted_text)}자"
    tools_used.append("extract_text_from_url")
    time.sleep(0.5)

    # 3. 요약
    step_name = "요약"
    steps.append(StepResult(step=step_name, status="진행중"))
    summarize_fn = tool_registry.get_tool("summarize_text")
    summary = execute_tool(summarize_fn, extracted_text)
    steps[-1].status = "완료"
    steps[-1].result = summary
    tools_used.append("summarize_text")
    time.sleep(0.5)

    # 4. 번역
    step_name = "번역"
    steps.append(StepResult(step=step_name, status="진행중"))
    translate_fn = tool_registry.get_tool("translate_text")
    translation = execute_tool(translate_fn, summary, target_lang="ko")
    steps[-1].status = "완료"
    steps[-1].result = translation
    tools_used.append("translate_text")
    time.sleep(0.5)

    return InferResponse(steps=steps, final_output=translation, tool_used=tools_used)
