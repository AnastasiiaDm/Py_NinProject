'''8. Написать функцию `XOR_cipher`, принимающая 2 аргумента: строку, которую нужно зашифровать, и ключ шифрования, которая
возвращает строку, зашифрованную путем применения операции XOR (битовое исключающее ИЛИ) над символами строки с ключом.
Написать также функцию `XOR_uncipher`, которая по зашифрованной строке и ключу восстанавливает исходную строку.'''

string = 'XOR_cipher'
key = 'keykeykeykeykeykeykeykeykeykeykey'


def XOR_cipher(m, n):

    return "".join([chr(ord(c1) ^ ord(c2)) for (c1, c2) in zip(m, n)])


encoded = XOR_cipher(key, string)
print(encoded)
decoded = XOR_cipher(encoded, key)
print(decoded)
