from typing import Callable, Any
from agent.tools.search_articles import search_articles
from agent.tools.extract_text_from_url import extract_text_from_url
from agent.tools.summarize_text import summarize_text
from agent.tools.translate_text import translate_text


def execute_tool(tool_fn: Callable, *args, **kwargs) -> Any:
    """
    단일 MCP 함수 실행기
    """
    try:
        print(f"[EXECUTOR] Tool 실행: {tool_fn.__name__}")
        result = tool_fn(*args, **kwargs)
        return result
    except Exception as e:
        print(f"[ERROR] Tool 실행 실패: {tool_fn.__name__} → {str(e)}")
        return f"❌ Tool 실행 중 오류 발생: {str(e)}"


def run_pipeline(query: str) -> dict:
    steps = []

    # 1. 뉴스 검색
    urls = search_articles(query)
    steps.append(
        {
            "step": "기사 검색",
            "status": "완료" if urls else "실패",
            "result": f"{len(urls)}건 검색됨" if urls else "검색 실패",
        }
    )
    if not urls:
        return {"steps": steps, "final_output": "❌ 뉴스 검색 실패"}

    # 2. 본문 추출 (여러 URL 중 하나라도 성공하면 사용)
    article_text = ""
    article_url = ""
    for url in urls:
        text = extract_text_from_url(url)
        if text:
            article_text = text
            article_url = url
            break

    steps.append(
        {
            "step": "본문 추출",
            "status": "완료" if article_text else "실패",
            "result": (
                f"본문 길이: {len(article_text)}자"
                if article_text
                else "본문 추출 실패"
            ),
        }
    )
    if not article_text:
        return {"steps": steps, "final_output": "❌ 본문 추출 실패"}

    # 3. 요약
    summary = summarize_text(article_text)
    steps.append(
        {
            "step": "요약",
            "status": "완료" if summary else "실패",
            "result": summary[:200] if summary else "요약 실패",
        }
    )
    if not summary:
        return {"steps": steps, "final_output": "❌ 요약 실패"}

    # 4. 번역
    translated = translate_text(summary, target_lang="ko")
    steps.append(
        {
            "step": "번역",
            "status": "완료" if translated else "실패",
            "result": translated[:200] if translated else "번역 실패",
        }
    )

    return {
        "steps": steps,
        "final_output": translated,
        "tool_used": [
            "search_articles",
            "extract_text_from_url",
            "summarize_text",
            "translate_text",
        ],
    }
