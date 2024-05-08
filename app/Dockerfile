FROM python:alpine

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt && adduser -D -H -u 1000 alham

USER alham

EXPOSE 8000

HEALTHCHECK --interval=60s --timeout=10s --start-period=5s --retries=3 CMD [ "python3", "health.py" ]

CMD ["gunicorn", "-b", "0.0.0.0:8000", "app:app"]
 