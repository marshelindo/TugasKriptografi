# Program Caesar Cipher

def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

# Input dari user
plain_text = input("Masukkan teks: ")
shift = int(input("Masukkan nilai kunci (shift): "))

# Enkripsi
cipher_text = encrypt(plain_text, shift)
print("Hasil enkripsi:", cipher_text)

# Dekripsi
print("Hasil dekripsi:", decrypt(cipher_text, shift))
