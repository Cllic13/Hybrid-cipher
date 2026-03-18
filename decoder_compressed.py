from random import choice

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "

def decrypt(cipher, cod_key):
    try:
        shift = int(cod_key[-1])
        pure = cod_key[:-1]
        key = pure[-shift:] + pure[:-shift]
    except: return "KEY INVALID"

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
            if work_word[i:i+2].isdigit():
                diff, i = int(work_word[i:i+2]), i + 2
            elif work_word[i].isdigit():
                diff, i = int(work_word[i]), i + 1
            else:
                diff, i = ALPHABET.index(work_word[i]), i + 1

            res.append(ALPHABET[(k_val - diff) % len(ALPHABET)])

        k_ptr += 1

    return "".join(res)

cipher = input("CRYPTOGRAM): ")
key = input("Key: ")
print(f"RESULT: {decrypt(cipher, key)}")
