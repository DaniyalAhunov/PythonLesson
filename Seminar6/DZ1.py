# Задача 1 Семинар 5.Напишите программу, удаляющую из текста все слова, содержащие ""абв"".


# Было!!!!
# my_string = 'Мы неабв очень любим Питон иабв Джавабв'.split()
# print(my_string)
# result_list = []
# for i in range(len(my_string)):
#     if 'абв' not in my_string[i]:
#         result_list.append(my_string[i])
# print(result_list)

# Стало !!!
my_string = 'Мы неабв очень любим Питон иабв Джавабв'.split()
result_list = list(filter(lambda x: 'абв' not in x , my_string))
print(result_list)