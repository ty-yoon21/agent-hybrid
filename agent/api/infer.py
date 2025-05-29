# from fastapi import APIRouter
# from agent.models.schema import InferRequest, InferResponse
# from agent.services.reasoner import run_reasoning_pipeline

# router = APIRouter()


# @router.post("/agent/infer", response_model=InferResponse)
# def infer(request: InferRequest):
#     """
#     사용자의 자연어 요청을 받아 Reasoning → Tool 실행 → 결과 반환
#     """
#     return run_reasoning_pipeline(request)

from fastapi import APIRouter
from agent.models.schema import InferRequest, InferResponse
from agent.services.tool_executor import run_pipeline

router = APIRouter()


@router.post("/agent/infer", response_model=InferResponse)
def infer(request: InferRequest):
    """
    사용자의 자연어 요청을 받아 고정된 MCP 파이프라인 실행 후 결과 반환
    """
    result = run_pipeline(request.query)
    return InferResponse(**result)
