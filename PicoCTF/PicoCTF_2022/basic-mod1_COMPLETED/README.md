## <p style="text-align: center;">basic-mod1</p>

<ol>
    <li> 
    We get "message.txt"
    
    $ wget https://artifacts.picoctf.net/c/393/message.txt
    
</li>
<br/>
    <li> The question tells us exactly what we need to do so I just made a Python script doing what they tell us:</li>

```python
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
```
</ol>
<br/>
<details>
    <summary> Flag </summary>
    
    picoCTF{R0UND_N_R0UND_79C18FB3}
</details>