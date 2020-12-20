# Ciphers

[![Python](https://img.shields.io/badge/Python-3.7.7-blue)](https://www.python.org/downloads/windows/)

### [Spartans Scytale](https://github.com/ans-sharma/ciphers/blob/master/spartan_scytale.py)

In cryptography, a scytale is a tool used to perform a transposition cipher, consisting of a cylinder with a strip of parchment wound around it on which is written a message. The ancient Greeks, and the Spartans in particular, are said to have used this cipher to communicate during military campaigns. 

##### Encryption
    ```cypher = ''
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


