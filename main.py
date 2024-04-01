'01.04.24=========================DJANGO========================='
# name_of_list = ['Helloworld!'] 
# new_list = name_of_list[0]
# for i in new_list:
#     if len(new_list) / 2 == 0:

name_of_list = ['Helloworld!']
input_string = name_of_list[0]
length = len(input_string)
if length % 2 == 0:
    first_half = input_string[:length // 2]
    print(first_half)
    second_half = input_string[length // 2:]
else:
    first_half = input_string[:length // 2 + 1]
    second_half = input_string[length // 2 + 1:]
    new_list = [char for char in second_half + first_half]
print(new_list) 