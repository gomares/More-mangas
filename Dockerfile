FROM python:3.10-alpine

LABEL maintainer="gomares"

RUN addgroup -S appgroup && adduser -S appuser -G appgroup

WORKDIR /app/test

COPY pyproject.toml poetry.lock tasks.py /app/

ENV PATH=$PATH:/home/testuser/.local/bin

RUN apk update && apk add python3-dev \
                        gcc \
                        libc-dev \
                        libffi-dev \
                        bash \
                        git

RUN pip install "poetry"


RUN poetry config virtualenvs.create false 
RUN poetry install

USER appuser
ENTRYPOINT ["invoke", "test"]