# numpy should be install in you python environment
import numpy as np

def split(word):
    return list(word)

def decrypt_spartan_scytale(text, size):
    ptext = ''
    text = split(text)
    output = np.array(text)
    output.resize(size, size)
    output = output.transpose()
    output = output.flatten()
    for letter in output:
        if letter != '@':
            ptext += letter
    return ptext


def encrypt_spartan_scytale(text, size):
    if len(text) > size * size:
        return 'Cannot be encrypted [text size exceed array limits]'
    else:
        cypher = ''
        text = split(text)
        output = np.array(text)
        output.resize(size, size)
        for i in range(0, size):
            for j in range(0, size):
                if output[i][j] == '':
                    output[i][j] = '@'
        output = output.transpose()
        output = output.flatten()
        for letter in output:
            cypher += letter
        return cypher


if __name__ == "__main__" :
    planeText = "ANSHUMAN"
    cipherText = encrypt_spartan_scytale(planeText, 4)
    print("Ciphertext: ", cipherText)
    print("Original/Decrypted Text :", decrypt_spartan_scytale(cipherText, 4))