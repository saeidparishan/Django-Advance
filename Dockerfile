FROM python:3.13 
 
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1 

WORKDIR /app

COPY requirements.txt  /app/
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt


RUN pip install --upgrade pip 
RUN pip install -r requirements.txt


COPY ./core /app
 