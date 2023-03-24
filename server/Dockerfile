FROM python:3.10

ENV PYTHONUNBUFFERED 1

EXPOSE 8000
WORKDIR /app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY server ./ 

CMD uvicorn --host=0.0.0.0 server:app --reload