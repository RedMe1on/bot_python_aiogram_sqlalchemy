# Separate build image
FROM python:3.9-slim-buster as compile-image
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \
 && pip install --no-cache-dir -r requirements.txt


FROM python:3.9-slim-buster

COPY --from=compile-image /opt/venv /opt/venv

# set environment variables
ENV PATH="/opt/venv/bin:$PATH"

# compile code once
ENV PYTHONDONTWRITEBYTECODE 1
# log to terminal
ENV PYTHONUNBUFFERED 1

WORKDIR /app

ENV TZ=Europe/Moscow
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

COPY bot ./bot

ENTRYPOINT ["python", "main.py"]

