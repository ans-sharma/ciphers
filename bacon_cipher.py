def encrypt_bacon_cipher(text, space = False, char1 = "A", char2 = "B"):
    text = text.replace(" ", "")
    text = text.upper()
    cipher = ""
    for char in text:
        decimal_value = (ord(char) - 13) % 26
        bin_value = bin(decimal_value).replace("0b","")
        if len(bin_value) < 5:
            zeros = ""
            for i in range(0, 5 - len(bin_value)): # Filling the empty value with 0.
                zeros = zeros + "0"
            zeros = zeros + bin_value
            bin_value = zeros
        for digit in bin_value:
            if digit == "1":
                cipher = cipher + char2
            elif digit == "0":
                cipher = cipher + char1
        if space: #Adding a space iff space = True
            cipher = cipher + " "
    return cipher

def decrypt_bacon_cipher(text, char1 = "A", char2 = "B"):
    planeText = ""
    bin_value = ""
    text = text.replace(" ", "")
    for char in text:
        if char == char1:
            bin_value = bin_value + "0"
        elif char == char2:
            bin_value = bin_value + "1"
    for i in range(0 , len(bin_value), 5):
        temp = bin_value[i : i + 5]
        temp = chr(int(temp, 2) + 65)
        planeText = planeText + temp
    return planeText


if __name__ == "__main__" :
    planeText = "ANSHUMAN"
    cipherText = encrypt_bacon_cipher(planeText)
    print("Ciphertext: ", cipherText)
    print("Original/Decrypted Text :", decrypt_bacon_cipher(cipherText))