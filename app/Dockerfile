FROM cgr.dev/chainguard/python:latest-dev AS builder
WORKDIR /app
COPY requirements.txt .
RUN python -m venv /app/venv && \
    /app/venv/bin/pip install --upgrade pip && \
    /app/venv/bin/pip install -r requirements.txt
COPY . .

FROM cgr.dev/chainguard/python:latest
USER nonroot
WORKDIR /app
COPY --from=builder --chown=nonroot:nonroot /app /app
ENV PATH="/app/venv/bin:${PATH}" DATABASE_URL=""
EXPOSE 8080
ENTRYPOINT ["python", "start.py"]