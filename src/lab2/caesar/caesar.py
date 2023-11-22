def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    encrypted = []
    for letter in plaintext:
        if ord(letter) in range(ord('a'), ord('z') + 1):
            if ord(letter) + shift > 122:
                encrypted.append(chr(ord(letter) + shift - 26))
            else:
                encrypted.append(chr(ord(letter) + shift))
        if ord(letter) in range(ord('A'), ord('Z') + 1):
            if ord(letter) + shift > 90:
                encrypted.append(chr(ord(letter) + shift - 26))
            else:
                encrypted.append(chr(ord(letter) + shift))
        if (ord(letter) < 65) or ((ord(letter) > 90) and (ord(letter) < 97)) or (ord(letter) > 122):
            encrypted.append(letter)
    ciphertext = ''.join(encrypted)
    return ciphertext
def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    decrypted = []
    for letter in ciphertext:
        if ord(letter) in range(ord('a'),ord('z')+1):
            if ord(letter) - shift < 97:
                decrypted.append(chr(ord(letter) - shift + 26))
            else:
                decrypted.append(chr(ord(letter) - shift))
        if ord(letter) in range(ord('A'),ord('Z')+1):
            if ord(letter) - shift < 65:
                decrypted.append(chr(ord(letter) - shift + 26))
            else:
                decrypted.append(chr(ord(letter) - shift))
        if (ord(letter)<65)or((ord(letter)>90)and(ord(letter)<97))or(ord(letter)>122):
            decrypted.append(letter)
    plaintext = ''.join(decrypted)
    return plaintext