import string

file = open("message.txt", 'r').read().split()

number_list = [pow((int(x) % 41), -1, 41) for x in file]

for index, number in enumerate(number_list):
    if number in range(1,27):
        number_list[index] = string.ascii_lowercase[number - 1]
    elif number in range(27,37):
        number_list[index] = str(number - 27)
    else:
        number_list[index] = '_'

print("picoCTF{" + "".join(number_list) + "}")


