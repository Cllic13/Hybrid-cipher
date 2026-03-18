import random

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "

def generate_key(length=15):
    key = ""
    for _ in range(length):
        char = random.choice(ALPHABET[:-1])
        if random.choice([True, False]):
            char += str(random.randint(0, 9))
        key += char
    return key

def shift_key(key):
    shift = random.randint(1, 9)
    return key[shift:] + key[:shift] + str(shift)

def encrypt_data(word, key):
    encoded = []
    for i, char in enumerate(word.upper()):
        if char not in ALPHABET: continue # Пропуск символов, которых нет в алфавите

        k_char = key[i % len(key)]

        if k_char.isdigit():
            res = ALPHABET[(ALPHABET.index(char) + int(k_char)) % len(ALPHABET)]
        else:
            diff = (ALPHABET.index(k_char) - ALPHABET.index(char)) % len(ALPHABET)
            res = str(diff) if i % 2 == 0 else ALPHABET[diff]

        encoded.append(res)

    return "".join(encoded)[::-1]

def main():
    raw_key = generate_key()
    transport_key = shift_key(raw_key)

    user_input = input("ENTER DATA: ")
    result = encrypt_data(user_input, raw_key)

    print(f"ENCRYPTED OBJECT: {result}")
    print(f"TRANSPORT KEY: {transport_key}")

if __name__ == "__main__":
    main()
