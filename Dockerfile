FROM python:3.10

WORKDIR /myapp

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
RUN pip install -e .

CMD ["sh", "-c", "uvicorn main:app --host=$HOST --port=$PORT"]