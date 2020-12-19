def encrypt_caesar_cipher(text, increment=3):
    letters = []
    keys = []
    cipher = ''
    letter = 'a'
    for i in range(0, 26):
        letters.append(letter)
        letter = chr(ord(letter) + 1)
    for i in range(increment, 26):
        keys.append(letters[i])
    for i in range(0, increment):
        keys.append(letters[i])
    keys = [x.upper() for x in keys]
    for l in text:
        for i in range(0, 26):
            if l == letters[i]:
                cipher += keys[i]
        if l == ' ':
            cipher += ' '
    return cipher


def decrypt_caesar_cipher(text, decrement=3):
    letters = []
    keys = []
    cipher = ''
    letter = 'a'
    for i in range(0, 26):
        letters.append(letter)
        letter = chr(ord(letter) + 1)
    for i in range(decrement, 26):
        keys.append(letters[i])
    for i in range(0, decrement):
        keys.append(letters[i])
    keys = [x.upper() for x in keys]
    for l in text:
        for i in range(0, 26):
            if l == keys[i]:
                cipher += letters[i]
        if l == ' ':
            cipher += ' '
    return cipher

if __name__ == "__main__" :
    planeText = "anshuman"
    cipherText = encrypt_caesar_cipher(planeText, increment=5)
    print("Ciphertext: ", cipherText)
    print("Original/Decrypted Text :", decrypt_caesar_cipher(cipherText, decrement=5))
