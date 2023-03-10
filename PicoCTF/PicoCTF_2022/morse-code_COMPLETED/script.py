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
                    '-.--.': '(', '-.--.-':')', ';':     '_'
                  }

with open("morse_code.txt",'r') as file:
    morse_code = file.read().split(' ')
    print("picoCTF{", end= "")
    for letter in morse_code:
        print(MORSE_CODE_DICT.get(letter), end="")
    print("}")