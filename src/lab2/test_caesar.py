import unittest
from caesar import encrypt_caesar, decrypt_caesar
class TestCaesarCipher(unittest.TestCase):
    def test_encrypt_caesar(self):
        # Проверяем зашифрованный текст с сдвигом 3
        self.assertEqual(encrypt_caesar("PYTHON"), "SBWKRQ")
        self.assertEqual(encrypt_caesar("python"), "sbwkrq")
        self.assertEqual(encrypt_caesar("Python3.6"), "Sbwkrq3.6")
        self.assertEqual(encrypt_caesar(""), "")  # Пустая строка должна оставаться пустой

    def test_decrypt_caesar(self):
        # Проверяем расшифрованный текст с сдвигом 3
        self.assertEqual(decrypt_caesar("SBWKRQ"), "PYTHON")
        self.assertEqual(decrypt_caesar("sbwkrq"), "python")
        self.assertEqual(decrypt_caesar("Sbwkrq3.6"), "Python3.6")
        self.assertEqual(decrypt_caesar(""), "")  # Пустая строка должна оставаться пустой


if __name__ == '__main__':
    unittest.main()