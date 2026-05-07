import time
import pydantic
import sys
import datetime

start_time = datetime.datetime.now()

while True:
    time.sleep(2)
    print(f"python version: {sys.version}")
    print(f"python version: {pydantic.__version__}")
    print(f"program started: {start_time}")
    print("Hello")