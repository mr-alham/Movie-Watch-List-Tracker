FROM python:alpine

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80

RUN adduser -D -H -u 1000 alham

RUN chown alham data/movies.json

RUN chmod 770 data/movies.json && cd data && chmod gu+rw movies.json 

HEALTHCHECK --interval=60s --timeout=10s --start-period=5s --retries=3 CMD [ "python3", "health.py" ]

USER alham

CMD ["gunicorn", "-b", "0.0.0.0:80", "app:app"]
