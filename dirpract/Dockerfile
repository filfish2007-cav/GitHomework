FROM python:3.11-slim

#create directory
WORKDIR /app

#copy everything
COPY ./requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

COPY ./ ./

#run this file
CMD ["python3","-u","server_hw.py"]