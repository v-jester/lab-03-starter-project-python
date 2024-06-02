FROM python:3.10

WORKDIR /app


RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=bind,source=./requirements/backend.in,target=./requirements/backend.in \
    python -m pip install --no-cache-dir -r ./requirements/backend.in


    COPY . .
    EXPOSE 8080

    CMD ["uvicorn", "spaceship.main:app", "--host=0.0.0.0", "--port=8080"]