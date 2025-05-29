# agent/Dockerfile

FROM python:3.10-slim

# Poetry 설치
ENV POETRY_VERSION=1.8.2
RUN pip install --no-cache-dir poetry==${POETRY_VERSION}

# 작업 디렉토리 생성
WORKDIR /app

# pyproject.toml 복사 및 의존성 설치
COPY pyproject.toml poetry.lock* ./
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

# 소스 코드 복사
COPY . .

# FastAPI 앱 실행 (포트 8000)
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
