# Prime-Based Cryptographic Engine

## Overview
This project is a terminal-based text encryption tool built as part of my flipped course evaluation. It applies fundamental programming algorithms to secure communication. Instead of relying on complex built-in security libraries, it uses mathematical concepts like prime number generation, the Greatest Common Divisor (GCD), and modular exponentiation to generate custom keys, encrypt text into numerical arrays, and decrypt them back to readable messages.

## Features
* **Keypair Generation:** Automatically calculates unique public and private keys using randomly generated prime numbers.
* **Message Encryption:** Converts readable text strings into hidden numerical arrays.
* **Message Decryption:** Reverses the modular arithmetic using the private key to perfectly restore the original text.
* **Interactive Menu:** A user-friendly terminal interface built with loops and conditional logic to easily navigate the tool.

## Technologies & Tools Used
* **Language:** Python 3
* **Libraries:** `random` (Python built-in library)
* **Version Control:** Git & GitHub

## Steps to Install & Run
1. Clone this repository to your local machine.
2. Open your terminal or command prompt.
3. Navigate to the main project folder.
4. Run the main application file by typing the following command:
   ```bash
   python main.py


Follow the on-screen menu to view your keys and start encrypting messages!

Instructions for Testing
To verify that the underlying mathematical logic and encryption loops work correctly without any data loss, a validation test script is included[cite: 1].

In your terminal, ensure you are in the main project directory.

Run the test file by typing:

Bash
python tests/test_crypto.py
The console will output a success message confirming that the prime logic, GCD math, and data loops passed validation.