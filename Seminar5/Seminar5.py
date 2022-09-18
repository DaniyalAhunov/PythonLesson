
def file_reading(x):
    with open(x, 'r') as file:
        y = file.readline()
    return y
def search_propysk(x):
    for i in range(len(x) - 1):
        if x[i] + 1 != x[i+1]:
            return x[i] + 1

list_numbers = file_reading('PythonGB/FileSeminar/s5s1.txt').split()
list_numbers = list(map(int, list_numbers))
num = search_propysk(list_numbers)
print(list_numbers)
print(num)

# my_string = 'Мы неабв очень любим Питон иабв Джавабв'.split()
# print(my_string)
# result_list = []
# for i in range(len(my_string)):
#     if 'абв' not in my_string[i]:
#         result_list.append(my_string[i])
# print(result_list)