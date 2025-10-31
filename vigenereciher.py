def vigenere_encrypt(text, key):
    result = ""
    key = key.upper()
    key_index = 0
    
    for char in text.upper():
        if char.isalpha():
            shift = ord(key[key_index]) - 65
            result += chr(((ord(char) - 65 + shift) % 26) + 65)
            key_index = (key_index + 1) % len(key)
        else:
            result += char
    return result


def vigenere_decrypt(text, key):
    result = ""
    key = key.upper()
    key_index = 0
    
    for char in text.upper():
        if char.isalpha():
            shift = ord(key[key_index]) - 65
            result += chr(((ord(char) - 65 - shift) % 26) + 65)
            key_index = (key_index + 1) % len(key)
        else:
            result += char
    return result


# Contoh penggunaan
plain_text = input("Masukkan teks yang mau dienkripsi: ")
key = input("Masukkan kunci (kata): ")

encrypted = vigenere_encrypt(plain_text, key)
print("Hasil enkripsi:", encrypted)

decrypted = vigenere_decrypt(encrypted, key)
print("Hasil dekripsi:", decrypted)
