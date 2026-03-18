import random
import time
import sys

COLORS = {
    "GREEN": "\033[92m",
    "YELLOW": "\033[93m",
    "CYAN": "\033[96m",
    "BOLD": "\033[1m",
    "END": "\033[0m"
}
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "

def typing_effect(text, delay=0.03, color=""):
    sys.stdout.write(color)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print(COLORS["END"])

def loading_bar(task, length=20):
    sys.stdout.write(f"{COLORS['CYAN']}{task} [")
    for _ in range(length):
        time.sleep(random.uniform(0.01, 0.08))
        sys.stdout.write("#")
        sys.stdout.flush()
    print(f"] DONE{COLORS['END']}")

def generate_key(length=15):
    typing_effect(">>> ЗАПУСК ГЕНЕРАТОРА ЭНТРОПИИ...", color=COLORS["CYAN"])
    key = ""
    for _ in range(length):
        char = random.choice(ALPHABET[:-1])
        if random.choice([True, False]):
            char += str(random.randint(0, 9))
        key += char
        sys.stdout.write(f"\r{COLORS['YELLOW']}ПОТОК ДАННЫХ: {key}{COLORS['END']}")
        sys.stdout.flush()
        time.sleep(0.03)
    print("\n[OK] ПЕРВИЧНЫЙ КЛЮЧ СФОРМИРОВАН.")
    return key

def shift_key(key):
    shift = random.randint(1, 9)
    shifted = key[shift:] + key[:shift] + str(shift)
    loading_bar("ЦИКЛИЧЕСКОЕ СМЕЩЕНИЕ")
    return shifted

def encrypt_data(word, key):
    encoded = []
    typing_effect(f"ПРИМЕНЕНИЕ АЛГОРИТМА СЛОЖЕНИЯ ПО МОДУЛЮ {len(ALPHABET)}...", color=COLORS["CYAN"])

    for i, char in enumerate(word.upper()):
        k_char = key[i % len(key)]
        display_char = "[SPACE]" if char == " " else char
        sys.stdout.write(f"Защита байта {i:02}: {display_char} + {k_char} -> ")

        if k_char.isdigit():
            res = ALPHABET[(ALPHABET.index(char) + int(k_char)) % len(ALPHABET)]
        else:
            diff = (ALPHABET.index(k_char) - ALPHABET.index(char)) % len(ALPHABET)
            res = str(diff) if i % 2 == 0 else ALPHABET[diff]

        print(f"{'[SPACE]' if res == ' ' else res}")
        encoded.append(res)
        time.sleep(random.uniform(0.05, 0.08))

    return "".join(encoded)[::-1]

def main():
    raw_key = generate_key()
    transport_key = shift_key(raw_key)

    print(f"\n{COLORS['BOLD']}ВВЕДИТЕ ДАННЫЕ ДЛЯ ШИФРОВАНИЯ:{COLORS['END']}")
    user_input = input(">>> ")

    loading_bar("МАЙНИНГ ДАННЫХ")

    result = encrypt_data(user_input, raw_key)

    loading_bar("ЗЕРКАЛИРОВАНИЕ И ФИНАЛИЗАЦИЯ")

    border = "=" * 45
    print(f"\n{COLORS['GREEN']}{border}")
    typing_effect("ОПЕРАЦИЯ ЗАВЕРШЕНА УСПЕШНО", color=COLORS["BOLD"])
    print(f"ЗАШИФРОВАННЫЙ ОБЪЕКТ: {COLORS['YELLOW']}{result}{COLORS['END']}")
    print(f"КЛЮЧ ТРАНСПОРТИРОВКИ: {COLORS['YELLOW']}{transport_key}{COLORS['END']}")
    print(f"{COLORS['GREEN']}{border}{COLORS['END']}")

if __name__ == "__main__":
    try:
        main()
        input("\nНажмите Enter для выхода...")
    except KeyboardInterrupt:
        print("\nПрервано пользователем.")
