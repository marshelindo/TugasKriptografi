def affine_encrypt(text, a, b):
    result = ""
    for char in text.upper():
        if char.isalpha():
            result += chr(((a * (ord(char) - 65) + b) % 26) + 65)
        else:
            result += char
    return result

def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

def affine_decrypt(cipher, a, b):
    result = ""
    a_inv = mod_inverse(a, 26)
    for char in cipher.upper():
        if char.isalpha():
            result += chr(((a_inv * ((ord(char) - 65 - b)) % 26) + 65))
        else:
            result += char
    return result


# Contoh pemakaian
plain_text = input("Masukkan teks: ")
a = int(input("Masukkan kunci a (coprime dengan 26): "))
b = int(input("Masukkan kunci b: "))

encrypted = affine_encrypt(plain_text, a, b)
print("Hasil enkripsi:", encrypted)

decrypted = affine_decrypt(encrypted, a, b)
print("Hasil dekripsi:", decrypted)
