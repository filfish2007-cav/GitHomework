# task 1

# class Cart:
#
#     def __init__(self, client,items):
#         self.client = client.capitalize()
#         self.items = [items]
#
#     def add_item(self,item):
#         self.items.append(item)
#
#     def remove_item(self,item):
#         if item not in self.items:
#             print("There is no such item")
#             return
#         self.items.remove(item)
#
#
#     def display_cart(self):
#         print(self.client,":")
#         print(self.items.join())
#         print()
#
# client1 = Cart("Filip","Water")
# client2 = Cart("Hussein","Banana")
#
# client1.add_item("Milk")
# client1.display_cart()
# client1.remove_item("Milk")
# client1.display_cart()
#
# client2.add_item("Nuts")
# client2.display_cart()

# # task 2

# class Phone:
#     def __init__(self, number):
#         self.number = number
#         self.battery_level = 100
#
#     def lower_charge(self, percent):
#         if self.battery_level < percent:
#             print("Battery level too low cant lower it anymore: ",
#                 self.battery_level,"%")
#             self.battery_level = 0
#             return
#
#         self.battery_level -= percent
#         print(f"The user just consumed {percent}% of phone power")
#
#         if self.battery_level < 20:
#             print("Battery level less that 20% now")
#
#         print("Battery level now is: ", self.battery_level,"%")
#
#     def charge(self, percent):
#         if self.battery_level == 100:
#             print("Battery level is at max: ", self.battery_level,"%")
#             return
#
#         if self.battery_level + percent >= 100:
#             print(f"The user just charged phone by {percent}%")
#             self.battery_level = 100
#             print("Battery level now is at its max : ", self.battery_level,"%")
#             return
#
#         self.battery_level += percent
#         print(f"The user just charged phone by {percent}%")
#
#         print("Battery level now is : ", self.battery_level,"%")
#
#     def display_info(self):
#         print(f"Phone {self.number}: is at {self.battery_level}%")
#
# phone1 = Phone("1")
# phone1.lower_charge(85)
# phone1.charge(100)
# phone1.display_info()
