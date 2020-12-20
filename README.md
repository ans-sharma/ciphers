# Ciphers

[![Python](https://img.shields.io/badge/Python-3.7.7-blue)](https://www.python.org/downloads/windows/)

### [Spartans Scytale](https://github.com/ans-sharma/ciphers/blob/master/spartan_scytale.py)

In cryptography, a scytale is a tool used to perform a transposition cipher, consisting of a cylinder with a strip of parchment wound around it on which is written a message. The ancient Greeks, and the Spartans in particular, are said to have used this cipher to communicate during military campaigns. 

##### Encryption
    ```python 
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
    ```
Implementing a Scytale using a 2 dimensional array.

### [Rail Fence](https://github.com/ans-sharma/ciphers/blob/master/rail_fence.py)

Rail Fence Encryption uses an integer for the number of levels of the zigzag.The encoded message is written in zig-zag (like a rail fence/sawtooth) along a path with N levels/floors.

##### Encryption
    ``` python
    if len(text) % 2 != 0:
        text += '@'
    for letter in range(0, len(text)):
        if letter % 2 == 0:
            part1 += text[letter]
        else:
            part2 += text[letter]
    text = part1 + part2
    ```
"@" is used a filled value in the method.

### [Vigenere Cipher](https://github.com/ans-sharma/ciphers/blob/master/vigen%C3%A8re_cipher.py)

The Vigenère cipher is a method of encrypting alphabetic text by using a series of interwoven Caesar.ciphers, based on the letters of a keyword. It employs a form of polyalphabetic substitution. A polyalphabetic cipher is any cipher based on substitution, using multiple substitution alphabets . The encryption of the original text is done using the Vigenère square or Vigenère table.

##### Encryption
    ```python
    for i in range(len(string)):
        x = (ord(string[i]) +
             ord(key[i])) % 26
        x += ord('A')
        cipher_text.append(chr(x))
    ```

### [Caesar Cipher](https://github.com/ans-sharma/ciphers/blob/master/caesar_cipher.py)

Caesar cipher, also known as Caesar's cipher, the shift cipher, Caesar's code or Caesar shift, is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet.

#### Encryption
    ```python
    keys = [x.upper() for x in keys]
    for l in text:
        for i in range(0, 26):
            if l == letters[i]:
                cipher += keys[i]
        if l == ' ':
            cipher += ' '
    ```

