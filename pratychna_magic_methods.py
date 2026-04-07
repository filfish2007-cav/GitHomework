# # task 1
# import datetime
#
# class Message:
#     def __init__(self, message: str,user: str,time: str):
#         self._message = message
#         self._user = user
#         self._time = datetime.datetime.strptime(time,'%H:%M')
#     def __str__(self):
#         return f"Message: {self._message} \n was sent by {self._user} at {self._time}"
#
#     def __len__(self):
#         return len(self._message)
#
#     def __gt__(self, other):
#         return self._time > other._time
#
#
# mes1 = Message("Hello man","Gringo","10:13")
# mes2 = Message("How are you","John","10:43")
# mes3 = Message("Im fine","Amigo","10:03")
#
# messages = [mes1, mes2, mes3]
#
# for message in messages:
#     print(message)
#
# messages.sort()
# for msg in messages:
#     print(msg)

# # task 2
# class Song:
#     def __init__(self, name: str, artist: str):
#         self.name = name
#         self.artist = artist
#
#     def __eq__(self, other):
#         return self.name == other.name and self.artist == other.artist
#
#     def __str__(self):
#         return f"Artist: {self.artist}. Song: {self.name} "
#
# class Playlist:
#     def __init__(self, songs:List[Song]):
#         self.songs = songs
#
#     def __len__(self):
#         return len(self.songs)
#
#     def __contains__(self, song):
#         return song in self.songs
#
#     def __iter__(self):
#         return iter(self.songs)
#
#     def add_song(self, song):
#         self.songs.append(song)
#
#     def remove_song(self, song):
#         self.songs.remove(song)
#
#
# sg1 = Song("Imagine", "John Lennon")
# sg2 = Song("Bohemian Rhapsody", "Queen")
# sg3 = Song("Shape of You", "Ed Sheeran")
# sg4 = Song("Walk", "Pantera")
#
#
# pisni = Playlist([sg1, sg2, sg3])
# pisni.add_song(sg4)
# for pisn in pisni:
#     print(pisn)


# # task 3


class Cart:
    def __init__(self, items: list[str], total: int):
        self.items = items
        self.total = total

    def __str__(self):
        return f"Items: {self.items} \n Total: {self.total}"

    def __len__(self):
        return len(self.items)

    def __add__(self, other):
        return Cart(self.items + other.items, self.total + other.total)

    def __iter__(self):
        return iter(self.items)


cart1 = Cart(["Milk", "Butter", "Bread"], 600)
cart2 = Cart(["Oil", "Carrots", "Potato", "Matches"], 400)

print(cart1)
print(cart2)

print(len(cart1))
print(len(cart2))

cart3 = cart1 + cart2

print(cart3)

print(len(cart3))
