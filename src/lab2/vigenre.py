def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    cipher = []
    while True:
        if len(keyword)>=len(plaintext):
            break
        else: keyword+=keyword
    count = 0
    shift = 0
    for letter in plaintext:
        if (ord(keyword[count])>=65) and (ord(keyword[count])<=90):
            shift = ord(keyword[count])-65
        else: shift = ord(keyword[count])-97
        if ord(letter) in range(ord('a'), ord('z') + 1):
            if ord(letter) + shift > 122:
                cipher.append(chr(ord(letter) + shift - 26))
            else:
                cipher.append(chr(ord(letter) + shift))
        if ord(letter) in range(ord('A'), ord('Z') + 1):
            if ord(letter) + shift > 90:
                cipher.append(chr(ord(letter) + shift - 26))
            else:
                cipher.append(chr(ord(letter) + shift))
        if (ord(letter) < 65) or ((ord(letter) > 90) and (ord(letter) < 97)) or (ord(letter) > 122):
            cipher.append(letter)
        count+=1
    ciphertext = ''.join(cipher)
    return ciphertext

def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    plain = []
    while True:
        if len(keyword) >= len(ciphertext):
            break
        else:
            keyword += keyword
    count = 0
    shift = 0
    for letter in ciphertext:
        if (ord(keyword[count]) >= 65) and (ord(keyword[count]) <= 90):
            shift = ord(keyword[count]) - 65
        else:
            shift = ord(keyword[count]) - 97
        if ord(letter) in range(ord('a'), ord('z') + 1):
            if ord(letter) - shift < 97:
                plain.append(chr(ord(letter) - shift + 26))
            else:
                plain.append(chr(ord(letter) - shift))
        if ord(letter) in range(ord('A'), ord('Z') + 1):
            if ord(letter) - shift < 65:
                plain.append(chr(ord(letter) - shift + 26))
            else:
                plain.append(chr(ord(letter) - shift))
        if (ord(letter) < 65) or ((ord(letter) > 90) and (ord(letter) < 97)) or (ord(letter) > 122):
            plain.append(letter)
        count += 1
    plaintext = ''.join(plain)
    return plaintext