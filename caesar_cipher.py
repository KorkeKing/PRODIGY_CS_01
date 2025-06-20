def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

# --- User Input ---
message = input("Enter a message: ")
shift = int(input("Enter the shift value (e.g., 3): "))

encrypted = caesar_encrypt(message, shift)
print("\nEncrypted:", encrypted)

decrypted = caesar_decrypt(encrypted, shift)
print("Decrypted:", decrypted)
