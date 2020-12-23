def coprime(x ,y):
    if x > y:
       smaller = y
    else:  
       smaller = x
    for i in range(1,smaller + 1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i
    if hcf == 1:
        return True
    else:
        return False

def encrypt_skip_code(text, step, start = 0):
    cipher = ""
    if coprime(len(text), step):
        text = text.upper()
        cipher = cipher + text[start]
        for i in range(1, len(text)):
            start = (start + step) % len(text)
            cipher = cipher + text[start]
        return cipher
    else:
        print("Invalid Step!")
        return ""

def decrypt_skip_code(text, step, start = 0):
    planeText = ""
    text = text.lower()
    planeText = planeText + text[start]
    for i in range(1, len(text)):
        start = (start + step) % len(text)
        planeText = planeText + text[start]
    return planeText

if __name__ == "__main__":
    planeText = "Anshuman"
    cipherText = encrypt_skip_code(planeText, 3)
    print("Ciphertext: ", cipherText)
    print("Original/Decrypted Text :", decrypt_skip_code(cipherText, 3))