import unittest
from vigenere import encrypt_vigenere, decrypt_vigenere

class TestVigenereCipher(unittest.TestCase):
    def test_encrypt_vigenere(self):
        # Проверка шифрования
        self.assertEqual(encrypt_vigenere("ATTACKATDAWN", "LEMON"), "LXFOPVEFRNHR")
        self.assertEqual(encrypt_vigenere("PYTHON", "A"), "PYTHON")
        self.assertEqual(encrypt_vigenere("python", "a"), "python")
        self.assertEqual(encrypt_vigenere("", "KEY"), "")

    def test_decrypt_vigenere(self):
        # Проверка дешифрования
        self.assertEqual(decrypt_vigenere("LXFOPVEFRNHR", "LEMON"), "ATTACKATDAWN")
        self.assertEqual(decrypt_vigenere("PYTHON", "A"), "PYTHON")
        self.assertEqual(decrypt_vigenere("python", "a"), "python")
        self.assertEqual(decrypt_vigenere("", "KEY"), "")

if __name__ == "__main__":
    unittest.main()