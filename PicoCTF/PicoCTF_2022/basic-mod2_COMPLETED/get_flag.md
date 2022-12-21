<ol>
    <li> 
    We get "message.txt"

    $ wget https://artifacts.picoctf.net/c/499/message.txt
    
</li>
<br/>
    <li> Just like "basic-mod1", the question tells us exactly what we need to do, so I just made a Python script with what they tell us:</li>

```python
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
```
</ol>
<br/>
<details>
    <summary> Flag </summary>
    
    picoCTF{1nv3r53ly_h4rd_c680bdc1}
</details>
