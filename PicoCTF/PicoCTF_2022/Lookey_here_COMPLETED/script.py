import re

with open("anthem.flag.txt", 'r') as file:
    text = file.read()
    r = re.search("pico", text)
    print(text[49769:50000]);