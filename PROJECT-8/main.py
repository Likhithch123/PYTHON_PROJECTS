## Title of the project: CAESAR CIPHER


import art

print(art.logo)
alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]


def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for char in plain_text:
        if char in alphabet:
            new_index = alphabet.index(char) + shift_amount
            if new_index > 25:
                new_index = new_index - 25 - 1
            cipher_text += alphabet[new_index]
        else:
            cipher_text += char
    print(f"The encoded text is {cipher_text}")


def decrypt(encoded_text, shift_amount):
    original_text = ""
    for char in encoded_text:
        if char in alphabet:
            new_index = alphabet.index(char) - shift_amount
            original_text += alphabet[new_index]
        else:
            original_text += char
    print(f"The decoded text is {original_text}")


should_continue = True
while should_continue:
    direction = input(
        "Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if shift > 26:
        shift = shift % 26
    if direction == "encode":
        encrypt(plain_text=text, shift_amount=shift)
    elif direction == "decode":
        decrypt(encoded_text=text, shift_amount=shift)
    else:
        print("Invalid direction.")
    user_choice = input(
        "Type 'yes' if you want to go again. Otherwise 'no'.\n").lower()
    if user_choice == 'yes':
        should_continue = True
    else:
        print("Goodbye.")
        should_continue = False
