FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app/
RUN python -m pip install -r requirements.txt

COPY bff /app/bff
COPY bff_config /app/bff_config
COPY gunicorn.conf.py /app/
COPY entrypoint.sh /app/
COPY manage.py /app/

ENTRYPOINT [ "/app/entrypoint.sh", "g", "-Fs" ]
