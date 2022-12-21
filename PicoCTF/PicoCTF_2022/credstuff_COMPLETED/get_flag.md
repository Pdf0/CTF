1. $ wget https://artifacts.picoctf.net/c/534/leak.tar
2. Extract the files from leak.tar
3. Check script.py to see how I got the encrypted password
4. Since it's a Caesar Cyphre, we can go online and decrypt it using a shift of 13

<ol>
    <li>
    We get the tar and extract them

    $ wget https://artifacts.picoctf.net/c/534/leak.tar; tar -xf leak.tar; rm leak.tar
</li>
<br/>
    <li>
    Since the passwords are equivalents to the username with the same index, we just need to get the password with the same index as the username named "cultiris". I used this python script:

```python 
with open("usernames.txt", 'r') as usernames:
    with open("passwords.txt", 'r') as passwords:
        usernames_list = usernames.read().split()
        passwords_list = passwords.read().split()
        
        position = usernames_list.index("cultiris")

        print(passwords_list[position])
```
</li>
<br/>
    <li>
    However, the password comes encypted. Fortunately, it's fairly easy to see that it's a Caesar Cyphre with a rotation of 13, so we can modify the script to give us the decrypted flag:

```python
import string

with open("usernames.txt", 'r') as usernames:
    with open("passwords.txt", 'r') as passwords:
        usernames_list = usernames.read().split()
        passwords_list = passwords.read().split()
        
        position = usernames_list.index("cultiris")

        # Decypting the password using Caesar cyphre with a rotation by 13

        encrypted_password = passwords_list[position]
        decrypted_password = ""

        for letter in encrypted_password:
            if letter.isupper():
                decrypted_password += string.ascii_uppercase[(string.ascii_uppercase.find(letter ) + 13) % 26]
            elif letter.islower():
                decrypted_password += string.ascii_lowercase[(string.ascii_lowercase.find(letter ) + 13) % 26]
            else:
                decrypted_password += letter

        print(decrypted_password)
```
</li>
</ol>
<br/>
<details>
    <summary> Flag </summary>
    
    picoCTF{C7r1F_54V35_71M3}
</details>