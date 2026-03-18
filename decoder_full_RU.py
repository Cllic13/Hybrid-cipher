import time
import sys
import random

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
GREEN = "\033[92m"
YELLOW = "\033[93m"
BOLD = "\033[1m"
END = "\033[0m"

def matrix_print(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def hack_effect(text, duration=15):
    chars = "ABCDEF0123456789%&^*@#$"
    for _ in range(duration):
        fake = "".join(random.choice(chars) for _ in range(len(text)))
        sys.stdout.write(f"\r{GREEN}[АНАЛИЗ ДАННЫХ]: {fake}{END}")
        sys.stdout.flush()
        time.sleep(0.08)
    print("\r" + " " * (len(text) + 20), end="\r")

def recover_key(cod_key):
    try:
        shift = int(cod_key[-1])
        pure = cod_key[:-1]
        return pure[-shift:] + pure[:-shift]
    except (ValueError, IndexError):
        return None

def decoder_pro():
    print(GREEN)
    matrix_print(">>> ИНИЦИАЛИЗАЦИЯ ДЕШИФРАТОРА v4.2...")

    cipher_text = input("[ВВОД ШИФРОГРАММЫ]: ").strip()
    cod_key = input("[ВВОД КЛЮЧА ДОСТУПА]: ").strip()

    key = recover_key(cod_key)
    if not key:
        print(f"{BOLD}ОШИБКА: КЛЮЧ ПОВРЕЖДЕН{END}")
        return

    hack_effect(cod_key)
    matrix_print("[OK] КЛЮЧ ВОССТАНОВЛЕН. ДЕКОДИРОВАНИЕ...")

    work_word = cipher_text[::-1]
    decoded = []

    i = 0
    k_idx = 0

    while i < len(work_word):
        k_char = key[k_idx % len(key)]
        sys.stdout.write(f"  Байт {i:02} (Key:{k_char}): ")

        for _ in range(3):
            sys.stdout.write(random.choice(ALPHABET[:-1]))
            sys.stdout.flush()
            time.sleep(0.05)
            sys.stdout.write("\b")

        if k_char.isdigit():
            idx = ALPHABET.index(work_word[i])
            res = ALPHABET[(idx - int(k_char)) % len(ALPHABET)]
            i += 1
        else:
            k_val = ALPHABET.index(k_char)

            if work_word[i:i+2].isdigit():
                diff = int(work_word[i:i+2])
                res = ALPHABET[(k_val - diff) % len(ALPHABET)]
                i += 2
            elif work_word[i].isdigit():
                diff = int(work_word[i])
                res = ALPHABET[(k_val - diff) % len(ALPHABET)]
                i += 1
            else:
                diff = ALPHABET.index(work_word[i])
                res = ALPHABET[(k_val - diff) % len(ALPHABET)]
                i += 1

        decoded.append(res)
        print(f"-> {'[SPACE]' if res == ' ' else res} [OK]")
        k_idx += 1

    print(f"\n{GREEN}{'='*45}")
    matrix_print(">>> ДОСТУП РАЗРЕШЕН. РЕЗУЛЬТАТ:")
    print(f"{BOLD}{YELLOW} {''.join(decoded)} {END}")
    print(f"{GREEN}{'='*45}{END}")

if __name__ == "__main__":
    try:
        decoder_pro()
        input("Нажмите Enter для выхода...")
    except KeyboardInterrupt:
        pass
