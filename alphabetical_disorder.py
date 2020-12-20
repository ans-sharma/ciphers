def encrypt_alphabetical_disorder_cipher(text):
    import random
    text = text.upper()
    tempValue = ""
    cipherText = ""
    for i in range(0, len(text)):
        tempValue = tempValue + text[i]
        if i in [2, 4, 12, 14]:
            tempValue = tempValue[::-1]
            tempValue = tempValue + " "
            cipherText = cipherText + tempValue
            tempValue = ""
        elif i == len(text)-1:
            tempValue = tempValue[::-1]
            tempValue = tempValue + " "
            cipherText = cipherText + tempValue
            # tempValue = ""
    return cipherText

def decrypt_alphabetical_disorder_cipher(cipher):
    cipher = cipher.lower()
    cipher = cipher.replace(" ", "")
    tempValue = ""
    planeText = ""
    for i in range(0, len(cipher)):
        tempValue = tempValue + cipher[i]
        if i in [2, 4, 12, 14]:
            tempValue = tempValue[::-1]
            planeText = planeText + tempValue
            tempValue = ""
        elif i == len(cipher)-1:
            tempValue = tempValue[::-1]
            planeText = planeText + tempValue
    return planeText

if __name__ == "__main__":
    planeText = "Anshuman"
    cipherText = encrypt_alphabetical_disorder_cipher(planeText)
    print("Ciphertext: ", cipherText)
    print("Original/Decrypted Text :", decrypt_alphabetical_disorder_cipher(cipherText))
    