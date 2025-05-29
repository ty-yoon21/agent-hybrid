# 🤖 AI Agent Backend (FastAPI + LangChain)

이 프로젝트는 사용자의 자연어 요청을 기반으로 여러 MCP Tool을 조합하여 복잡한 작업을 수행하는 AI Agent 백엔드 시스템입니다.  
LangChain 기반 Reasoning, Function Calling, Tool Registry, YAML 기반 MCP 등록 등을 포함하며, 확장성과 유연성을 목표로 합니다.

---

## 📁 디렉토리 구조

```
.
├── agent/                         # AI Agent 백엔드 코드
│   ├── main.py                    # FastAPI 진입점
│   ├── api/
│   │   └── infer.py              # /agent/infer 엔드포인트
│   ├── core/
│   │   ├── config.py             # 환경 변수 로딩 및 설정
│   │   └── prompt.py             # System/User Prompt 템플릿 정의
│   ├── services/
│   │   ├── reasoner.py           # LangChain 기반 Reasoning / Tool 선택 로직
│   │   └── tool_executor.py      # 선택된 Tool 실행 로직 (Function Calling)
│   ├── tools/
│   │   ├── search_articles.py    # 뉴스 검색 MCP Tool
│   │   ├── extract_text_from_url.py  # 기사 본문 추출 MCP Tool
│   │   ├── summarize_text.py     # 요약 Tool
│   │   └── translate_text.py     # 번역 Tool
│   ├── registry/
│   │   ├── tool_registry.py      # 등록된 Tool 메타 관리 및 선택
│   │   └── tool_spec_loader.py   # YAML 기반 MCP 자동 등록 로직
│   ├── models/
│   │   └── schema.py             # Request/Response 데이터 모델 정의
│   └── test_data/
│       └── example_inputs.json   # 테스트용 예제 입력 파일
├── .env                          # OpenAI 키, 환경 변수 등 설정
├── pyproject.toml                # Poetry 프로젝트 정의 및 의존성
├── poetry.lock                   # Poetry 의존성 잠금 파일
├── Dockerfile                    # Docker 이미지 빌드 설정
├── docker-compose.yaml           # Docker Compose 설정
└── README.md                     # 프로젝트 설명
```

---

## 🚀 구동 방법

### 🧪 로컬 실행

```bash
# 1. Poetry 설치 (최초 1회)
linux
curl -sSL https://install.python-poetry.org | python3 -
window
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -

# 2. 프로젝트 디렉토리 이동
cd agent

# 3. 의존성 설치
poetry install

# 4. 환경 변수 설정 (.env)
echo "OPENAI_API_KEY=your-openai-key" > .env

# 5. 서버 실행
poetry run uvicorn agent.main:app --reload --port 8000
```

### 🐳 Docker 실행

```bash
# Dockerfile이 포함된 위치에서 실행
docker build -t ai-agent .

# 환경 변수 파일 적용하여 실행
docker run --env-file .env -p 8000:8000 ai-agent
```

---

## 🧠 핵심 기술

| 항목 | 설명 |
|------|------|
| FastAPI | API 서버 및 inference 엔드포인트 |
| LangChain | Reasoner 구조, Tool 연동, Function calling |
| LangGraph (옵션) | Node 기반 실행 흐름 확장 가능 |
| Function Calling | LLM이 Tool을 선택하고 실행 |
| YAML Tool Spec | 툴을 별도 등록 없이 자동 인식 및 실행 가능 |
| Structured Output | Pydantic 모델을 통한 명확한 입출력 처리 |
| Chain of Thought | 복합 reasoning 수행 기반 |

---

## 🧪 테스트 예시

`POST /agent/infer`

```json
{
  "query": "테슬라 관련 뉴스 요약해서 번역해줘",
  "session_id": "abc123"
}
```

### 예상 처리 흐름

1. Tool 선택: `search_articles`
2. 결과 → `extract_text_from_url`
3. 결과 → `summarize_text`
4. 결과 → `translate_text`
5. 최종 응답 반환

---

## 🔧 Tool 추가 방법

1. `tools/`에 Python 함수로 Tool 추가  
2. 또는 `mcp_specs/`에 YAML 스펙 정의 추가  
3. 서버 재시작 시 자동 등록됨

예: `tools/sentiment_analysis.py`

```python
def sentiment_analysis(text: str) -> str:
    return "positive"
```

---

## 📝 TODO

- [ ] LangGraph 노드 플로우 확장
- [ ] Tool 호출 시 에러 리커버리 처리
- [ ] Slack 또는 Email 등 외부 연동 MCP 추가

---

## 📄 라이선스

본 프로젝트는 실험/PoC 목적의 AI Agent 백엔드로 자유롭게 확장 가능합니다.
