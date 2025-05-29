# def summarize_text(text: str) -> str:
#     """
#     주어진 기사 본문을 간단히 요약합니다.
#     (현재는 Mock 요약 반환)
#     """
#     print(f"[MCP] 요약 중...")
#     return f"요약된 내용 (예시): '{text[:50]}...'을 요약한 결과입니다."

import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def summarize_text(text: str) -> str:
    """
    긴 본문 텍스트를 요약합니다. GPT-3.5 사용 (최신 openai SDK 기준).
    """
    print("[MCP] 요약 중...")

    prompt = (
        "다음은 뉴스 기사 본문입니다. 핵심 내용을 3~4줄로 요약해주세요.\n\n"
        f"{text}\n\n요약:"
    )

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.5,
            max_tokens=300,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"[ERROR] 요약 실패: {e}")
        return "요약 실패"
