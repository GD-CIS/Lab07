
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alpha_list = list(alpha)
secret = "COOL"
def header(alpha_list):
    print("| ", end="")
    for i, _ in enumerate(alpha_list):
            print(f"|{alpha_list[i]}", end="")
    print("|")
    for i, _ in enumerate(alpha_list):
        if i == 0:
            print(f"|-", end="")
            print(f"|-", end="")
        else:
            print(f"|-", end="")
    print("|")

def vigenere_sq(alpha_list):
    for move in range(26):
        for i, letter in enumerate(alpha_list):
            if i == 0:
                print(f"|{alpha_list[(i + move) % 26]}", end="")
                print(f"|{alpha_list[(i + move) % 26]}", end="")
            else:
                print(f"|{alpha_list[(i + move) % 26]}", end="")
        print("|")

def letter_to_index(letter, alpha_list):
    return alpha_list.index(letter)

def index_to_letter(n, alpha_list):
    return alpha_list[n]

def mainword(word):
    for i in word:
        return (letter_to_index(i, alpha_list))

def key(secret):
    for j in secret:
        return letter_to_index(j, alpha_list)

def vigenere_index(key_letter, plaintext_letter, alpha_list):
    return (letter_to_index(key_letter, alpha_list) + letter_to_index(plaintext_letter, alpha_list)) % len(alpha_list)

def anti_index(key_letter, cipher_letter, alpha_list):
    return (letter_to_index(cipher_letter, alpha_list) - letter_to_index(key_letter, alpha_list)) % len(alpha_list)

def encrypt_vigenere(key, plaintext, alpha_list):
    cipher = []
    cipher_text = ""
    for i, c in enumerate(plaintext):
        if c == " ":
            pass
        elif(c.upper() in alpha_list):
            cipher.append(index_to_letter(vigenere_index(key[i % len(key)], c, alpha_list), alpha_list))
    print(cipher)
    cipher_text = cipher_text.join(cipher)
    return global_list.append(cipher_text)

def decrypt(key, cipher_text, alpha_list):
    uncipher = []
    uncipher_text = ""
    for i, f in enumerate(cipher_text):
        if f in cipher_text:
            uncipher.append(index_to_letter(anti_index(key[i % len(key)], f, alpha_list), alpha_list))
    print(uncipher)
    return print(uncipher_text.join(uncipher))

def menu():
   while True:
        choice = ["1.Encrypt", "2.Decrypt", "3.Dump Encrypted", "4.Quit"]
        print(choice)
        n = input("")
        better_n = int(n) - 1
        if better_n == 0:
            plaintext = input("Put text here: ").upper()
            encrypt_vigenere(secret, plaintext, alpha_list)
        elif better_n == 1:
            special = input("put text you want to decrypt here: ").upper()
            decrypt(secret, special, alpha_list)
        elif better_n == 2:
            print(global_list)
        elif better_n == 3:
            break


global_list = []

header(alpha_list)
vigenere_sq(alpha_list)
menu()



