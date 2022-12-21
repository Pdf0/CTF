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
        