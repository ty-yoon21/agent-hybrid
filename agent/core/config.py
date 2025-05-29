import os
from dotenv import load_dotenv

# .env 파일 로딩
load_dotenv()

# OpenAI API Key (필수)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# OpenAI 모델 설정
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4")

# 추론 최대 토큰
MAX_TOKENS = int(os.getenv("MAX_TOKENS", 1024))

# Tool Spec 경로
TOOL_SPEC_DIR = os.getenv("TOOL_SPEC_DIR", "tool_specs")

# 기타 설정들 (확장 가능)
