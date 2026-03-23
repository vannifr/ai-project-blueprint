FROM python:3.12-slim

WORKDIR /app

COPY pyproject.toml .
COPY src/ src/

RUN pip install --no-cache-dir .

# Docs are mounted as volume
VOLUME /app/docs

ENV BLUEPRINT_TRANSPORT=streamable-http
ENV BLUEPRINT_HOST=0.0.0.0
ENV BLUEPRINT_PORT=8902
ENV BLUEPRINT_DOCS_PATH=/app/docs
ENV BLUEPRINT_LANGUAGE=en

EXPOSE 8902

CMD ["blueprint-mcp"]
