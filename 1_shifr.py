'''8. Написать функцию `XOR_cipher`, принимающая 2 аргумента: строку, которую нужно зашифровать, и ключ шифрования, которая
возвращает строку, зашифрованную путем применения операции XOR (битовое исключающее ИЛИ) над символами строки с ключом.
Написать также функцию `XOR_uncipher`, которая по зашифрованной строке и ключу восстанавливает исходную строку.'''

data = 'XOR_cipher'
key = 'key'
cipher = []


def XOR_cipher(data, key = 'awesomepassword', encode = False, decode = False):

    from itertools import izip, cycle
    import base64

    if decode:
        data = base64.decodestring(data)
    xored = ''.join(chr(ord(x) ^ ord(y)) for (x, y) in izip(data, cycle(key)))

    if encode:
        return base64.encodestring(xored).strip()
    return xored
secret_data = "XOR procedure"

print("The cipher text is")
print(XOR_cipher(secret_data, encode=True))
print("The plain text fetched")
print(XOR_cipher(XOR_cipher(secret_data, encode=True), decode=True))










