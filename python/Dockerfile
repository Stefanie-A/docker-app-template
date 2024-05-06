FROM python:3.12-slim

WORKDIR /app

EXPOSE 8000
# Install pip requirements

COPY requirements.txt .

RUN pip install -r requirements.txt 

COPY . .

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:app"]
