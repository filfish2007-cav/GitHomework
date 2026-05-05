# import threading
#
# def get_sum(nums: list[int]):
#     result = sum(nums)
#     print(f"Сума чисел: {result}")
#
# def get_average(nums: list[int]):
#     if not nums:
#         print("Середнє арифметичне: 0")
#         return
#     result = sum(nums) / len(nums)
#     print(f"Середнє арифметичне: {result}")
#
# numbers = []
#
# print("Вводьте числа (порожній рядок для завершення):")
# while True:
#     user_input = input()
#     if user_input == "":
#         break
#     numbers.append(int(user_input))
#
# print(f"\nСписок чисел: {numbers}")
#
# thread_sum = threading.Thread(target=get_sum, args=(numbers,))
# thread_avg = threading.Thread(target=get_average, args=(numbers,))
#
# thread_sum.start()
# thread_avg.start()
#
# thread_sum.join()
# thread_avg.join()


def delete_nth(order, max_e):
    new = []
    for i in order:
        if order.count(i) != max_e:
            new.append(i)

    return new

print(delete_nth([3,3,3,5,5,5,5,7,8,9], 2))





# sum_array([4,9,9,9,10,10,1,5])

