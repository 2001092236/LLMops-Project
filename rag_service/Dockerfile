FROM python:3.11-slim

RUN pip install poetry==1.8.3
COPY pyproject.toml poetry.lock ./
RUN poetry install --no-root


COPY src/ ./rag_service
RUN poetry install --no-dev
WORKDIR /rag_service

# RUN pip install -qU langchain-text-splitters

CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
