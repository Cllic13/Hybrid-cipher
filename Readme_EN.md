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
