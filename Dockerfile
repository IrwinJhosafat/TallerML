FROM python:3.9

WORKDIR /app
COPY requirements.txt .

COPY model.h5 .

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python","main.py"]

