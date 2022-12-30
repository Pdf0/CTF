
phrase = "cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_Ncualgvd}"
flag = ""
lower_alphabet = "abcdefghijklmnopqrstuvwxyz"
upper_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for letter in phrase:
    if letter not in "{\/}`´^~-_.'\":,;<>|1234567890«»":
        if letter.islower():
            caesar_letter = lower_alphabet[(lower_alphabet.find(letter)+13)%26]
            flag += caesar_letter
        else:
            caesar_letter = upper_alphabet[(upper_alphabet.find(letter)+13)%26]
            flag += caesar_letter
    else:
        flag += letter
print (flag)

 


