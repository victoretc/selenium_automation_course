FROM python:3.11-slim-bookworm

WORKDIR /tests

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["pytest -s -v"]