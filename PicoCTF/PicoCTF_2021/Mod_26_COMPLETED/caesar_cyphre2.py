phrase = "cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_Ncualgvd}"
flag = ""

alpha = "abcdefghijklmnopqrstuvwxyz"
ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for c in phrase:
    if c in alpha or c in ALPHA:
        if c.islower():
            c = alpha[(alpha.find(c) + 13) % 26] 
        else:
            c = ALPHA[(ALPHA.find(c) + 13) % 26]
    flag += c        

print(flag)