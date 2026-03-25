from random import choice, randint

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "

def generate_key(length=15):
    key = ""
    for _ in range(length):
        char = choice(ALPHABET[:-1])
        if choice([True, False]):
            char += str(randint(0, 9))
        key += char
    return key

def shift_key(key):
    shift = randint(1, 9)
    return key[shift:] + key[:shift] + str(shift)

def encrypt_data(word, key):
    encoded = []
    for i, char in enumerate(word.upper()):
        if char not in ALPHABET: continue
        k_char = key[i % len(key)]
        if k_char.isdigit():
            res = ALPHABET[(ALPHABET.index(char) + int(k_char)) % len(ALPHABET)]
        else:
            diff = (ALPHABET.index(k_char) - ALPHABET.index(char)) % len(ALPHABET)
            res = str(diff) if i % 2 == 0 else ALPHABET[diff]
        encoded.append(res)
    return "".join(encoded)[::-1]

def decrypt_data(cipher, cod_key):
    try:
        shift = int(cod_key[-1])
        pure = cod_key[:-1]
        key = pure[-shift:] + pure[:-shift]
    except: return "ERROR: INVALID KEY"

    work_word = cipher[::-1]
    res = []
    i = k_ptr = 0
    while i < len(work_word):
        k_char = key[k_ptr % len(key)]
        if k_char.isdigit():
            idx = ALPHABET.index(work_word[i])
            res.append(ALPHABET[(idx - int(k_char)) % len(ALPHABET)])
            i += 1
        else:
            k_val = ALPHABET.index(k_char)
            if i + 1 < len(work_word) and work_word[i:i+2].isdigit():
                diff, i = int(work_word[i:i+2]), i + 2
            elif work_word[i].isdigit():
                diff, i = int(work_word[i]), i + 1
            else:
                diff, i = ALPHABET.index(work_word[i]), i + 1
            res.append(ALPHABET[(k_val - diff) % len(ALPHABET)])
        k_ptr += 1
    return "".join(res)

def main():
    while True:
        print("=== CRYPT-OS ===\n")
        print("1 - Encoder")
        print("2 - Decoder")
        print("3 - Description")
        print("4 - GitHub")
        print("0 - Exit")

        choice = input(f"\nSelect an option: ")

        if choice == "1":
            raw_key = generate_key()
            transport_key = shift_key(raw_key)
            user_input = input("ENTER DATA TO ENCRYPT: ")
            result = encrypt_data(user_input, raw_key)
            print(f"ENCRYPTED OBJECT: {result}")
            print(f"KEY: {transport_key}")
            input("Enter to return...")

        elif choice == "2":
            cipher = input("ENTER CRYPTOGRAM: ")
            key = input("ENTER KEY: ")
            print(f"RESULT: {decrypt_data(cipher, key)}")
            input("Enter to return...")

        elif choice == "3":
            print("This is a compressed and combined version of the encoder and decoder.\nMade by Cllic13 from the OOM team\nver 1.03")
            input("Enter to return...")

        elif choice == "4":
            print("GitHub: https://github.com/Cllic13/Hybrid-cipher")
            input("Enter to return...")

        elif choice == "0":
            print("Goodbye World")
            break
        else:
            print("Invalid choice.")


try:
     main()
     input("Enter to exit...")
except:
     print("\nAborted")