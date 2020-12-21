import numpy as np

def split(word):
    return list(word)

def encrypt_columnar_transposition(text):
    size = 3
    cipherText = ""
    if len(text) > size*size:
        return 'Cannot be encrypted [text size exceed array limits]'
    else:
        text = text.upper()
        text = split(text)
        text = np.array(text)
        text.resize(size, size)
        for i in range(0, size):
            for j in range(0, size):
                if text[i][j] == '':
                    text[i][j] = '@'
        key = input("Enter the permutation key (Eg- [132], [321], [312]):")
        if len(key) != 3:
            print("Invalid Input, using the default value for encryption: [132]")
            key = "132"
        if key == "123":
            pass
        elif key == "132":
            text[:, [2, 1]] = text[:, [1 ,2]]
        elif key == "213":
            text[:, [1, 0]] = text[:, [0 ,1]]
        elif key == "321":
            text[:, [2, 0]] = text[:, [0, 2]]
        elif key == "312":
            text[:, [2, 0]] = text[:, [0, 2]]
            text[:, [2, 1]] = text[:, [1 ,2]]
        elif key == "231":
            text[:, [2, 0]] = text[:, [0, 2]]
            text[:, [1, 0]] = text[:, [0 ,1]]
        else:
            return 'Invalid Input'
        text = text.flatten()
        for letter in text:
            cipherText += letter
        return cipherText

def decrypt_columnar_transposition(text):
    size = 3
    planeText = ""
    text = text.lower()
    text = split(text)
    text = np.array(text)
    text.resize(size, size)
    key = input("Enter the permutation key (Eg- [132], [321], [312]):")
    if len(key) != 3:
        print("Invalid Input, using the default value for encryption: [132]")
        key = "132"
    if key == "123":
        pass
    elif key == "132":
        text[:, [2, 1]] = text[:, [1 ,2]]
    elif key == "213":
        text[:, [1, 0]] = text[:, [0 ,1]]
    elif key == "321":
        text[:, [2, 0]] = text[:, [0, 2]]
    elif key == "312":
        text[:, [2, 1]] = text[:, [1 ,2]]
        text[:, [2, 0]] = text[:, [0, 2]]
    elif key == "231":
        text[:, [1, 0]] = text[:, [0 ,1]]
        text[:, [2, 0]] = text[:, [0, 2]]
    else:
        return 'Invalid Input'
    text = text.flatten()
    for letter in text:
        if letter != '@':
            planeText += letter
    return planeText

if __name__ == "__main__" :
    planeText = "ANSHUMAN"
    cipherText = encrypt_columnar_transposition(planeText)
    print("Ciphertext: ", cipherText)
    print("Original/Decrypted Text :", decrypt_columnar_transposition(cipherText))