from random import choice

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "

def decrypt(cipher, cod_key):
    # 1. Восстановление ключа
    try:
        shift = int(cod_key[-1])
        pure = cod_key[:-1]
        key = pure[-shift:] + pure[:-shift]
    except: return "ОШИБКА КЛЮЧА"

    # 2. Подготовка текста
    work_word = cipher[::-1]
    res = []
    i = k_ptr = 0

    # 3. Цикл дешифровки
    while i < len(work_word):
        k_char = key[k_ptr % len(key)]

        if k_char.isdigit():
            # Цезарь назад
            idx = ALPHABET.index(work_word[i])
            res.append(ALPHABET[(idx - int(k_char)) % len(ALPHABET)])
            i += 1
        else:
            # Разница индексов
            k_val = ALPHABET.index(k_char)
            # Проверяем, число ли перед нами (2 знака или 1)
            if work_word[i:i+2].isdigit():
                diff, i = int(work_word[i:i+2]), i + 2
            elif work_word[i].isdigit():
                diff, i = int(work_word[i]), i + 1
            else:
                diff, i = ALPHABET.index(work_word[i]), i + 1

            res.append(ALPHABET[(k_val - diff) % len(ALPHABET)])

        k_ptr += 1

    return "".join(res)

# Тест
cipher = input("Шифрограмма: ")
key = input("Ключ: ")
print(f"Результат: {decrypt(cipher, key)}")
