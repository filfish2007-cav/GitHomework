import random
import time

from settings import settings

while True:
    time.sleep(3)

    rand_num = random.randint(settings.start_range, settings.end_range)
    print(f"Random number: {rand_num}")
    print(f"password: {settings.password}")
    print(f"login: {settings.login}")
