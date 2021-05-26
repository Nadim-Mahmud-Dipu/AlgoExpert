# Caesar Cipher Encryptor
def ceasarCipher(string, key):
    key = key % 26
    result = []
    for letter in string:
        nlc = ord(letter) + key
        if nlc <= 122:
            result.append(chr(nlc))
        else:
            result.append(chr(96 + (nlc % 122)))
    return "".join(result)

print(ceasarCipher("abcdef", 55))
