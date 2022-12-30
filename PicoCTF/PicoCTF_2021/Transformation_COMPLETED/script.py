crypted_phrase = '灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸弰摤捤㤷慽'
flag = ''

for char in crypted_phrase:
    hex_letter = hex(ord(char)).lstrip("0x")
    bytes_object = bytes.fromhex(hex_letter)
    ascii_string = bytes_object.decode("ASCII")
    flag += ascii_string
print(flag)

