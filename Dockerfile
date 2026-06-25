FROM python:3.12-slim

ARG VERSION=dev
ARG COMMIT=unknown
ARG BUILD_DATE=unknown

ENV APP_VERSION=$VERSION
ENV GIT_COMMIT=$COMMIT
ENV BUILD_DATE=$BUILD_DATE

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
