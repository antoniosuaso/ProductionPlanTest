FROM python:3.9

WORKDIR /code

COPY requirements.txt .

RUN pip install "uvicorn[standard]" && pip install fastapi

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8888"]