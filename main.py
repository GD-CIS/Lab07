alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
secret = "COOL"
message = "awesome"
def header(alpha):
    print("| ", end="")
    for i, _ in enumerate(alpha):
            print(f"|{alpha[i]}", end="")
    print("|")
    for i, _ in enumerate(alpha):
        if i == 0:
            print(f"|-", end="")
            print(f"|-", end="")
        else:
            print(f"|-", end="")
    print("|")

def vigenere_sq(alpha):
    for move in range(26):
        for i, letter in enumerate(alpha):
            if i == 0:
                print(f"|{alpha[(i + move) % 26]}", end="")
                print(f"|{alpha[(i + move) % 26]}", end="")
            else:
                print(f"|{alpha[(i + move) % 26]}", end="")

        print("|")

def letter_to_index(letter, alpha):
    return alpha.lower().index(letter.lower())
def index_to_letter(n, alpha):
    return alpha[n]
def mainword(word):
    for i in word:
        return (letter_to_index(i, alpha))
def key(secret):
    for j in secret:
        return letter_to_index(j, alpha)
def vigenere_index(key_letter, plaintext_letter, alphabet):
    return (letter_to_index(key_letter, alpha) + letter_to_index(plaintext_letter, alpha)) % len(alpha)

def encrypt_vigenere(key, plaintext, alpha):
    cipher = ""
    for i, c in enumerate(plaintext):
        if c == " ":
            pass
        elif(c.upper() in alpha):
            cipher += index_to_letter(vigenere_index(key[i%len(key)], c, alpha), alpha)
    return cipher
header(alpha)
vigenere_sq(alpha)
print(f"{encrypt_vigenere(secret, message, alpha)}")