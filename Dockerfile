FROM python:3.9-slim
LABEL authors="hreyes"

WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY src .

EXPOSE 5000

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "com.grayraccoon.app.app:app"]
