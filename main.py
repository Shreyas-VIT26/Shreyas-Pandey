#V2

import random

# --- Math Functions ---

def find_gcd(a, b):
    # keep dividing until remainder is 0
    while b != 0:
        a, b = b, a % b
    return a

def check_if_prime(n):
    if n < 2:
        return False
    # looping only to the square root saves a lot of processing time
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_random_prime(min_val=50, max_val=500):
    # min value is 50 so n stays above 255 (avoids ascii errors)
    p = random.randint(min_val, max_val)
    while not check_if_prime(p):
        p = random.randint(min_val, max_val)
    return p

# --- Crypto Functions ---

def generate_user_keys():
    p1 = get_random_prime(50, 200)
    p2 = get_random_prime(50, 200)
    while p1 == p2:
        p2 = get_random_prime(50, 200)
        
    n_val = p1 * p2
    phi_val = (p1 - 1) * (p2 - 1)
    
    e_val = random.randrange(2, phi_val)
    while find_gcd(e_val, phi_val) != 1:
        e_val = random.randrange(2, phi_val)
        
    d_val = 1
    while (d_val * e_val) % phi_val != 1:
        d_val += 1
        
    return (e_val, n_val), (d_val, n_val)

def text_to_cipher(pub_key, text):
    if len(text) == 0:
        return []
        
    e, n = pub_key
    encrypted_list = []
    
    for letter in text:
        num = ord(letter)
        # using pow() for instant modular math instead of ** %
        cipher_num = pow(num, e, n)
        encrypted_list.append(cipher_num)
        
    return encrypted_list

def cipher_to_text(priv_key, num_list):
    if len(num_list) == 0:
        return ""
        
    d, n = priv_key
    final_text = ""
    
    for c in num_list:
        # using pow() for decryption efficiency 
        original_num = pow(c, d, n)
        final_text += chr(original_num)
        
    return final_text

# --- Main Program Loop ---

def main_menu():
    print("Initializing crypto tools...")
    # using a dictionary to store keys
    user_keys = {}
    
    pub, priv = generate_user_keys()
    user_keys['admin'] = {'public': pub, 'private': priv}
    
    while True:
        print("\n--- SECURE CHAT MENU ---")
        print("1 - Show my keys")
        print("2 - Encrypt a message")
        print("3 - Decrypt a message")
        print("4 - Quit")
        
        user_choice = input("Enter choice: ")
        
        try:
            if user_choice == '1':
                print("Public key:", user_keys['admin']['public'])
                print("Private key:", user_keys['admin']['private'])
                
            elif user_choice == '2':
                msg = input("Enter message to hide: ")
                hidden = text_to_cipher(user_keys['admin']['public'], msg)
                print("Hidden data array:", hidden)
                
            elif user_choice == '3':
                raw_data = input("Enter numbers with commas: ")
                # list comprehension strips spaces and ignores trailing commas
                num_array = [int(x.strip()) for x in raw_data.split(',') if x.strip()]
                decoded = cipher_to_text(user_keys['admin']['private'], num_array)
                print("Decoded message:", decoded)
                
            elif user_choice == '4':
                print("Exiting...")
                break
            else:
                print("Wrong input. Try 1 to 4.")
                
        except Exception as e:
            print("Uh oh, something went wrong:", e)

if __name__ == '__main__':
    main_menu()