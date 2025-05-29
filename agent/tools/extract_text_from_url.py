# def extract_text_from_url(url: str) -> str:
#     """
#     주어진 URL에서 기사 본문 텍스트를 추출합니다.
#     (현재는 Mock 텍스트 반환)
#     """
#     print(f"[MCP] 본문 추출 중: {url}")
#     return f"본문 내용 요약 예시: '{url}' 에 대한 샘플 기사 텍스트입니다. 실제 구현 시 크롤러나 API 연동 필요."

import requests


# def extract_text_from_url(url: str) -> str:
#     """
#     주어진 뉴스 기사 URL에서 본문 텍스트를 추출합니다.
#     현재는 Mercury Parser API 또는 유사 기능 사용.
#     """
#     print(f"[MCP] 본문 추출 중: {url}")
#     try:
#         # 비공식 Mercury 클론 엔드포인트 예시 (본인의 URL로 대체 가능)
#         api_url = "https://mercury-parser.vercel.app/parser"
#         params = {"url": url}
#         response = requests.get(api_url, params=params)
#         response.raise_for_status()
#         data = response.json()
#         return data.get("content", "")[:3000]  # 길이 제한 (필요시)
#     except Exception as e:
#         print(f"[ERROR] 본문 추출 실패: {e}")
#         return ""

from newspaper import Article


def extract_text_from_url(url: str) -> str:
    print(f"[MCP] 본문 추출 중: {url}")
    try:
        article = Article(url)
        article.download()
        article.parse()
        return article.text
    except Exception as e:
        print(f"[ERROR] 본문 추출 실패: {e}")
        return ""
