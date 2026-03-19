# CRYPT-OS: Hybrid Vigenere-Based Cipher
> **Symmetric stream encryption tool with a bespoke visual terminal**

**English version 🇬🇧** | [Русская версия 🇷🇺](README.md)

## Project Overview
**CRYPT-OS** is an original implementation of a symmetric encryption algorithm that combines classic character substitution with dynamic index offset calculation. The full version of the programme recreates the atmosphere of a cinematic "hacker terminal", accompanying every stage of the process (key generation, data analysis, encryption) with real-time animations and system logs.

## Key Features
*   **Hybrid Logic:** The algorithm doesn’t just use a Vigenere or Caesar cipher; it merges them into a single workflow (albeit a straightforward one).
*   **Simplicity at Heart:** The core algorithm is designed to be accessible and uncomplicated—it simply gets the job done.
*   **Randomised Key:** Keys do not have a fixed length, and the distribution of numerical digits within them is entirely random.
*   **Key Obfuscation:** The transport key is protected by a lightweight internal cipher, making it difficult to utilise without the proper algorithm.
*   **Cine-Visual Interface:** The full "Hollywood Edition" features a bespoke "hacker-style" terminal visualiser.
*   **Character Support:** Full support for Latin script and spaces. Support for Cyrillic, special characters, and additional symbols is currently in the roadmap.

## Technical Stack
*   **Language:** Python 3.XX
*   **Standard Libraries:** `random`, `time`, `sys`

## The essence of the algorithm
If, of course, anyone is actually reading this
  Look, the logic behind this encoder is dead simple. Here’s how it works, for what it’s worth:
  
  First, a key is generated. Minimum length is 15 letters plus one shift digit at the end. It can go up to 30 characters plus that final digit. It’s built by picking random letters from the alphabet (including spaces), with a 50% chance of a digit spawning between the letters. That’s it for now; I’ll probably make the generation more convoluted later, if I don't bin the whole thing.
  
  Then, your word gets encrypted using that key. It takes the first letter of your text and the first character of the key and checks them: if it’s a letter or a space, it’s interpreted as a number based on the internal alphabet. If it’s a digit, the value stays as is. Then, the letter of your text shifts along the alphabet by that value (wrapping back to the start if it hits the end). Then it moves to the second letter of your text and the second character of the key, and so on.
  
  Once the text is scrambled, your personal key gets encrypted by a random shift digit, and then that digit is tacked onto the very end.
There is nothing complicated about it. Deepseek or Gemini couldn't decipher it without an algorithm.
Any ideas or suggestions can be added to the GitHub Discussions. Do not criticize the code. It is still being developed, and I am in degradation.
