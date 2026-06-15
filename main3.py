# Створіть додаток «Соціальна мережа», який зберігає
# інформацію про користувача, його друзів, публікації корис-
# тувача. Можливості додатку:
# ■ додати користувача;
# ■ видалити користувача;
# ■ редагувати інформацію про користувача;
# ■ пошук користувача за ПІБ;
# ■ перегляд інформації про користувача;
# ■ перегляд усіх друзів користувача;
# ■ перегляд усіх публікацій користувача.
# Зберігайте дані у базі даних NoSQL. Можете використо-
# вувати Redis в якості платформи.
from redis import Redis

# class SocialApp():
#     def __init__(self):
#         self.server = Redis(host='localhost', port=6379, db=0)
#
#         self.current_user = None
#
# # get keys for database
#     def _get_cred_key(self,user_name):
#         return f"credential:{user_name}}"
# # get info
#     def _get_info_key(self,user_name):
#         return f"personal info:{user_name}"
# # get friends_info
#     def _get_friends_key(self,user_name):
#         return f"personal info:{user_name}"
# # get story_info
#     def _get_story_key(self,user_name,story_name):
#         return f"story info:{user_name},{story_name}"
#
# # ■ вхід за логіном і паролем;
# # ■ додати користувача;
#
#     def login(self,user_name,password):
#         key = self._get_cred_key(user_name)
#
#         if not self.server.exists(key):
#             print("User does not exist")
#             return
#
#         true_password = self.server.get(key)
#
#         if true_password != password:
#             print("Wrong Password")
#             return
#
#         self.current_user = user_name
#         print("Login Successful")
#
#     def sign_up(self,user_name,password):
#         key = self._get_info_key(user_name)
#
#         if self.server.exists(key):
#             print("User Exists")
#             return
#
#         self.server.set(key,password)
#         print("Sign up Successful")
#
#
#
#     def add_info(self,user_name,age,city):
#         # get key for user who logged in before
#         key = self._get_info_key(self.current_user)
#
#         data = {
#             "name": user_name,
#             "age": age,
#             "city": city
#         }
#
#         self.server.hmset(key,data)
#
#         print("info updated")
#
# # ■ перегляд інформації про користувача;
#     def get_info(self):
#         if self.current_user is None:
#             print("User did not log in")
#             return
#
#         key = self._get_info_key(self.current_user)
#         data = self.server.hgetall(key)
#
#         print("info loaded: ",data)
#
#         friend_key = self._get_friends_key(self.current_user)
#         self.
#
#
#     def add_friend(self,friend):
#
#         if self.current_user is None:
#             print("User did not log in")
#             return
#         # if friend registered if his password exists
#         friend_key = self._get_cred_key(friend)
#         if not self.server.exists(friend_key):
#             print("not registered")
#             return
#
#         #add friend
#         key = self._get_info_key(self.current_user)
#         self.server.sadd(key,friend)
#
#         friend_key = self._get_friends_key(friend_key)
#         self.server.sadd(friend_key,self.current_user)
#
#         print("Friend added")
#
#     def get_friends(self):
#         if self.current_user is None:
#             print("User did not log in")
#             return
#         key = self._get_info_key(self.current_user)
#         friends = self.server.smembers(key)
#
#         print(f"friends loaded: {friends}")
#
#     def add_story(self,story_name,content):
#         if self.current_user is None:
#             print("User did not log in")
#             return
#
#         key = self._get_story_key(self.current_user,story_name)
#
#         if self.server.exists(key):
#             print("u have this story with that name")
#             return
#
#         self.server.set(key,content)
#         print("Story added")


# app = SocialApp()
#
#
# app.login("filip","abao")
# app.add_info(user_name="filip_rybkin",age=39,city="Dnipro")
# app.get_info()


# Завдання 2
# Створіть додаток «Музей літератури». Додаток має зберігати
# інформацію про експонати та людей, які мають відношення
# до експонатів. Можливості додатку:
# ■ вхід за логіном і паролем;
# ■ додати експонат;
# 1
# Практичнє завдання
# ■ видалити експонат;
# ■ редагування інформації про експонат;
# ■ перегляд повної інформації про експонат;
# ■ виведення інформації про всі експонати;
# ■ перегляд інформації про людей, які мають відношення
# до певного експонату;
# ■ перегляд інформації про експонати, що мають відношення
# до певної людини;
# ■ перегляд набору експонатів на основі певного критерію.
# Наприклад, показати всі книжкові експонати.
# Зберігайте дані у базі даних NoSQL. Можете використо-
# вувати Redis в якості платформи.


# ■ вхід за логіном і паролем;
class LiteratureMuseum:
    def __init__(self):
        self.server = Redis(host="localhost", port=6379, db=0, decode_responses=True)

        self.current_user = None

        self.isloggedin = False

    def _get_cred_key(self, user_name):
        return f"password:{user_name}"

    def _get_exponat_key(self, exp_name):
        return f"exponat:{exp_name}"

    def _get_people_key(self, person_name):
        return f"people:{person_name}"

    def _get_exp_related_name_key(self, exp_name):
        return f"exponat:{exp_name}:people"

    def login(self, user_name, password):
        key = self._get_cred_key(user_name)

        if not self.server.exists(key):
            print("user does not exist")
            return

        true_password = self.server.get(key)

        if true_password != password:
            print("wrong password")
            return

        print("you are logged in")
        self.isloggedin = True

    def signup(self, user_name, password):
        key = self._get_cred_key(user_name)

        if self.server.exists(key):
            print("user exists")
            return

        self.server.set(key, password)

        print("you are registered now")

    def add_exp_info(self, exp_name, desc):
        key = self._get_exponat_key(exp_name)

        if not self.isloggedin:
            print("not logged in")
            return

        self.server.set(key, desc)
        print("exp added")


# save password:filip 12344
# save exponat:name description
# save people:name description
# save exponat:name:people name

app = LiteratureMuseum()

app.login("filip_rybkin", "abao")


app.add_exp_info("triangle", "figure")
app.add_exp_info("rectangle", "figure2")


# ■ додати експонат;
