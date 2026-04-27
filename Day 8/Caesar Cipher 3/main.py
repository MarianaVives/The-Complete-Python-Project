alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(original_text, shift_amount, direction):

    final_message= ""
    if direction == 'encode':
        print("Encrypting...")
    elif direction == 'decode':
        print("Decrypting...")
        shift_amount *= -1
    else:
        print("Invalid input")

    for t in original_text:
        if t == " ":
            final_message += t
        for a in alphabet:
            if t == a:
                shifting_position = alphabet.index(t) + shift_amount
                shifting_position %= len(alphabet)
                shifting = alphabet[shifting_position]
                final_message += shifting
    print("Encoded message : " + final_message) if direction=="encode" else print("Decoded message : " + final_message)

try_again = True

while try_again:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    encrypt(text, shift, direction)
    continue_yn = input("Want to continue y/n : ").lower()
    if continue_yn == "n":
        try_again = False