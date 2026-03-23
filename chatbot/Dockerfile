FROM python:3.12-slim

WORKDIR /app

COPY pyproject.toml .
COPY src/ src/
COPY scripts/ scripts/

RUN pip install --no-cache-dir .

# ChromaDB data is mounted as volume
VOLUME /app/chroma_data

EXPOSE 8901

CMD ["uvicorn", "blueprint_chat.api:app", "--host", "0.0.0.0", "--port", "8901"]
