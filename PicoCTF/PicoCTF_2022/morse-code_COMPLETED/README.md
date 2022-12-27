## <p style="text-align: center;">morse-code</p>

<ol>
    <li>
    We get the audio file

    $ wget https://artifacts.picoctf.net/c/235/morse_chal.wav
</li>
<br/>
    <li>
    We know that it's morse code and since it's easier to work with text, we can convert this to text. In my case I used Audacity to see the dots and traces more clearly (I used ";" as spaces)

<br/>

![Imgur](https://imgur.com/MQSA23V)

<br/>

``.-- .... ....- --... ; .... ....- --... .... ; ----. ----- -.. ; .-- ..--- ----- ..- ----. .... --...``
</li>
<br/>
    <li>
    Once we have the morse code written down, we can translate it to regular text. I used this python script

```python
MORSE_CODE_DICT = { '.-':    'a', '-...':  'b',
                    '-.-.':  'c', '-..':   'd', '.':     'e',
                    '..-.':  'f', '--.':   'g', '....':  'h',
                    '..':    'i', '.---':  'j', '-.-':   'k',
                    '.-..':  'l', '--':    'm', '-.':    'n',
                    '---':   'o', '.--.':  'p', '--.-':  'q',
                    '.-.':   'r', '...':   's', '-':     't',
                    '..-':   'u', '...-':  'v', '.--':   'w',
                    '-..-':  'x', '-.--':  'y', '--..':  'z',
                    '.----': '1', '..---': '2', '...--': '3',
                    '....-': '4', '.....': '5', '-....': '6',
                    '--...': '7', '---..': '8', '----.': '9',
                    '-----': '0', '--..--':',', '.-.-.-':'.',
                    '..--..':'?', '-..-.': '/', '-....-':'-',
                    '-.--.': '(', '-.--.-':')', ';':     ' '
                  }

with open("morse_code.txt",'r') as file:
    morse_code = file.read().split(' ')
    print("picoCTF{", end= "")
    for letter in morse_code:
        print(MORSE_CODE_DICT.get(letter), end="")
    print("}")
```
</li>
</ol>
<br/>
<details>
    <summary> Flag </summary>
    
    picoCTF{wh47_h47h_90d_w20u9h7}
</details>