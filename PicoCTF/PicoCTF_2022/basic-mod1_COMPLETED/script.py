import string

file = open("message.txt", "r").read().split()

number_list = [int(x) % 37 for x in file]

for index, number in enumerate(number_list):
    if number in range(0,26):
        number_list[index] = string.ascii_uppercase[number]
    elif number in range(26,36):
        number_list[index] = str(number -26)
    else:
        number_list[index] = '_'

print("picoCTF{" + "".join(number_list) + "}")