FROM python:3.9

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt \
    -r requirements-prod.txt

CMD ["gunicorn", "--worker-tmp-dir", "/dev/shm", "-b", "0.0.0.0:3000", "app:app"]
