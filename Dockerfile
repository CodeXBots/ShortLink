FROM python:3.11.2-slim-buster

WORKDIR /Shortlink-Convertor

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python3", "bot.py"]
