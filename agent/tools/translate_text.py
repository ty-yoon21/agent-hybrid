# def translate_text(text: str, target_lang: str = "ko") -> str:
#     """
#     주어진 텍스트를 지정한 언어로 번역합니다.
#     (현재는 Mock 번역 결과 반환)
#     """
#     print(f"[MCP] 번역 중... 대상 언어: {target_lang}")
#     return f"[{target_lang.upper()} 번역]: '{text}' (번역된 예시 결과입니다)"

import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def translate_text(text: str, target_lang: str = "ko") -> str:
    """
    주어진 텍스트를 지정된 언어로 번역합니다. 기본은 한국어. (최신 openai SDK 기준)
    """
    print(f"[MCP] 번역 중... 대상 언어: {target_lang}")

    prompt = (
        f"다음 문장을 {target_lang} 언어로 자연스럽게 번역해 주세요:\n\n{text}\n\n번역:"
    )

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.5,
            max_tokens=500,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"[ERROR] 번역 실패: {e}")
        return "번역 실패"
