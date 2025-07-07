FROM python:3.13 AS build

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /factory
COPY requirements.txt /factory/

RUN python -m pip install build
RUN python -m pip install -r requirements.txt

COPY pyproject.toml /factory/
COPY temperature_api /factory/temperature_api

RUN python -m build

FROM python:3.13 AS deploy

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app/
RUN python -m pip install -r requirements.txt

COPY --from=build /factory/dist /dist/
RUN python -m pip install temperature_api -f /dist

COPY entrypoint.sh /app/

ENTRYPOINT [ "/app/entrypoint.sh", "uv" ]
