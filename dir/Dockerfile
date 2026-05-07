FROM python:3.11-slim

#create directory
WORKDIR app

#copy everything
COPY ./ ./

RUN pip install -r requirements.txt

EXPOSE 8080

#run this file
CMD ["python3","server_hw.py"]