import datetime
class Message:
    def __init__(self, message: str,user: str,time: str):
        self._message = message
        self._user = user
        self._time = datetime.datetime.strptime(time,'%H:%M')
    def __str__(self):
        return f"Message: {self._message} \n was sent by {self._user} at {self._time}"

    def __len__(self):
        return len(self._message)

    def __gt__(self, other):
        return self._time > other._time


mes1 = Message("Hello man","Gringo","10:13")
mes2 = Message("How are you","John","10:43")
mes3 = Message("Im fine","Amigo","10:03")
messages = [mes1, mes2, mes3]
for message in messages:
    print(message)

messages.sort()
for msg in messages:
    print(msg)

