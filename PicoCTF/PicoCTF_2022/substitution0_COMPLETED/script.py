def decrypt(ciphertext, alphabet):
    """
    Decrypts a substitution cipher text using the given substitution alphabet.

    Parameters:
    ciphertext (str): The ciphertext to be decrypted.
    alphabet (str): The substitution alphabet to be used for decryption.

    Returns:
    str: The decrypted plaintext.
    """
    # Create a dictionary mapping the original alphabet characters to the substitution alphabet characters
    mapping = {ciphertext[i].upper(): alphabet[i].upper() for i in range(len(alphabet))}

    # Decrypt the ciphertext by replacing each character with its corresponding substitution character
    plaintext = ""
    for c in ciphertext:
        if c.isalpha():
            if c.isupper():
                plaintext += mapping[c]
            else:
                plaintext += mapping[c.upper()].lower()
        else:
            plaintext += c

    return plaintext

# Test the decrypt function
ciphertext = '''Mjbjhfly Ujcbeyz eblgj, rxpm e cbenj eyz gpepjui exb, eyz kblhcmp dj pmj kjjpuj
tbld e cuegg segj xy rmxsm xp reg jysulgjz. Xp reg e kjehpxthu gsebekejhg, eyz, ep
pmep pxdj, hyqylry pl yephbeuxgpg—lt slhbgj e cbjep fbxwj xy e gsxjypxtxs flxyp
lt nxjr. Pmjbj rjbj prl blhyz kuesq gflpg yjeb lyj jvpbjdxpi lt pmj kesq, eyz e
ulyc lyj yjeb pmj lpmjb. Pmj gseujg rjbj jvsjjzxycui mebz eyz culggi, rxpm euu pmj
effjebeysj lt khbyxgmjz cluz. Pmj rjxcmp lt pmj xygjsp reg njbi bjdebqekuj, eyz,
peqxyc euu pmxycg xypl slygxzjbepxly, X slhuz mebzui kuedj Ohfxpjb tlb mxg lfxyxly
bjgfjspxyc xp.

Pmj tuec xg: fxslSPT{5HK5717H710Y_3N0UH710Y_59533E2J}'''
alphabet = "EKSZJTCMXOQUDYLFABGPHNRVIW"

print(decrypt(ciphertext, alphabet))

