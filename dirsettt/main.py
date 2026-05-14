import time

from settings import settings

while True:
    time.sleep(1)

    print(settings.filename)
    print(settings.app_name)
    print(settings.password)
    print(settings.login)
    print()
