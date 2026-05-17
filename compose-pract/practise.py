import random
import time

from settings import settings

while True:
    time.sleep(settings.delay)

    rand_len = random.randint(settings.min_len, settings.max_len)

    print(settings.symbol * rand_len)
