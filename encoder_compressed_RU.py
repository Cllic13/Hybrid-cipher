from random import choice, random, randint

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "

def encrypt(word, key):
    res = []
    for i, char in enumerate(word.upper()):
        k = key[i % len(key)]
        idx = ALPHABET.index(char)

        if k.isdigit():
            new_char = ALPHABET[(idx + int(k)) % len(ALPHABET)]
        else:
            diff = (ALPHABET.index(k) - idx) % len(ALPHABET)
            new_char = str(diff) if i % 2 == 0 else ALPHABET[diff]
        res.append(new_char)

    return "".join(res)[::-1]

raw_key = "".join(choice(ALPHABET[:-1]) + str(randint(0,9)) for _ in range(15))
shift = randint(1, 9)
transport_key = raw_key[shift:] + raw_key[:shift] + str(shift)

word = input("Введите текст: ")
result = encrypt(word, raw_key)

print(f"Зашифровано: {result}")
print(f"Ключ: {transport_key}")
