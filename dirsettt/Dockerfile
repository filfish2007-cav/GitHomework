FROM python:3.11-slim
# базова папка (куди копіювати файли)
WORKDIR /app
# скопіювати

COPY ./requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

COPY ./ ./

ENV LOGIN=student123

CMD ["python3", "-u", "main.py"]
