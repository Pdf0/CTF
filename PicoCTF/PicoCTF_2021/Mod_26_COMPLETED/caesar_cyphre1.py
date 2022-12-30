phrase = "cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_Ncualgvd}"
flag = ""

lower_alphabet = "abcdefghijklmnopqrstuvwxyz"
upper_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for letter in phrase:
    if letter in lower_alphabet or letter in upper_alphabet:
        if letter.islower():
            letter = lower_alphabet[(lower_alphabet.find(letter) + 13) % 26]
        else:
            letter = upper_alphabet[(upper_alphabet.find(letter) + 13) % 26]
    
    flag += letter

print(flag)



