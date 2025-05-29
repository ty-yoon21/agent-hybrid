from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from agent.api.infer import router as infer_router

app = FastAPI(
    title="AI Agent API", description="ReAct 기반 MCP Tool Agent", version="0.1.0"
)

# CORS 설정 (필요 시 조정)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 라우터 등록
app.include_router(infer_router)
