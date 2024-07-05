FROM tiangolo/uvicorn-gunicorn:python3.11

WORKDIR /test

COPY requirements.txt .
COPY . /test

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "main.py"]