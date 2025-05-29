from pydantic import BaseModel, Field
from typing import List, Optional


class InferRequest(BaseModel):
    query: str = Field(..., description="사용자의 자연어 요청")
    session_id: Optional[str] = Field(None, description="세션 추적용 ID")


class StepResult(BaseModel):
    step: str = Field(..., description="작업 단계 이름 (예: 기사 검색, 요약 등)")
    status: str = Field(..., description="진행 상태 (예: 진행중, 완료, 실패)")
    result: Optional[str] = Field(
        None, description="해당 단계의 결과 요약 또는 핵심 출력"
    )


class InferResponse(BaseModel):
    steps: List[StepResult] = Field(
        ..., description="Agent가 수행한 각 단계별 상태 및 결과"
    )
    final_output: Optional[str] = Field(
        None, description="최종 응답 (예: 번역된 요약문)"
    )
    tool_used: Optional[List[str]] = Field(None, description="사용된 Tool 이름 목록")
