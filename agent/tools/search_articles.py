# def search_articles(keyword: str) -> list:
#     """
#     키워드를 기반으로 관련 뉴스 기사의 URL 목록을 반환합니다.
#     (현재는 Mock 데이터 반환)
#     """
#     print(f"[MCP] 기사 검색 중: {keyword}")
#     # 실제 구현에서는 외부 뉴스 API 또는 검색엔진 사용
#     return [
#         f"https://news.example.com/{keyword}-article-1",
#         f"https://news.example.com/{keyword}-article-2",
#         f"https://news.example.com/{keyword}-article-3",
#     ]
import os
import requests
from urllib.parse import quote
from dotenv import load_dotenv
import re

load_dotenv()

GNEWS_API_KEY = os.getenv("GNEWS_API_KEY")
GNEWS_ENDPOINT = "https://gnews.io/api/v4/search"


def search_articles(keyword: str, max_articles: int = 3) -> list:
    print(f"[MCP] 기사 검색 중: {keyword}")

    # 🚨 keyword 정리
    clean_keyword = re.sub(r"[\\r\\n]+", " ", keyword).strip()

    params = {
        "q": clean_keyword,
        "lang": "en",
        "max": max_articles,
        "token": GNEWS_API_KEY,
    }

    try:
        response = requests.get(GNEWS_ENDPOINT, params=params)
        response.raise_for_status()
        data = response.json()
        articles = data.get("articles", [])
        return [article["url"] for article in articles]
    except Exception as e:
        print(f"[ERROR] 뉴스 검색 실패: {e}")
        return []
