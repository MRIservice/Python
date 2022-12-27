#!/usr/bin/python3

with open("file1.txt") as file1:
    file1_data = file1.readlines()

with open("file2.txt") as file2:
    file2_data = file2.readlines()

######### List Comprehention EXERCISES Python ###################

# names = ["Alex", "Beth", "Caroline", "Dave", "Herbert", "Freddie"]
# numbers = [1, 2, 3]

# # new_list = []
# # for num in numbers:
# #     add_1 = num+1
# #     new_list.append(add_1)

#####################################################
# # Example list comprehention
# #new_list = [new_item for item in list if test]
#####################################################

# new_list = [item + 1 for item in numbers]
# print(new_list)

# name = "Super Dave"
# letters_list = [letter for letter in name]
# print(letters_list)

# new_list2 = [test*2 for test in range(1, 5)]
# print(new_list2)

# new_list3 = [name for name in names if len(name) < 5]
# print(new_list3)

# new_list4 = [name.upper() for name in names if len(name) > 5]
# print(new_list4)

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# squared_num = [item*item for item in numbers]
# print(squared_num)

# even_num = [number for number in numbers if number % 2 == 0]
# print(even_num)

result = [int(item) for item in file1_data if item in file2_data]

print(result)
