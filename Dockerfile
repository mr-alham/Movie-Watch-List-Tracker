FROM python:3.11-alpine

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r app/requirements.txt && \
    adduser -D -H -u 1000 alham && \
    chown alham app/data/movies.json && \
    chmod 770 app/data/movies.json

USER alham

EXPOSE 80

HEALTHCHECK --interval=60s --timeout=10s --start-period=5s --retries=3 CMD [ "python3", "health.py" ]

CMD ["gunicorn", "-b", "0.0.0.0:80", "app:app"]
