FROM python:3.10-slim

RUN apt-get update && \
    apt-get install -y build-essential cmake python3-dev && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . .

RUN pip install --upgrade pip
RUN pip install flask transformers llama-cpp-python

EXPOSE 5000

CMD ["python", "app.py"]