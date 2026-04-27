alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(original_text, shift_amount):

    final_message= ""
    if direction == 'encode':
        print("Encrypting...")
    elif direction == 'decode':
        print("Decrypting...")
    else:
        print("Invalid input")

    for t in original_text:
        if t == " ":
            final_message += t
        for a in alphabet:
            if t == a:
                if direction == 'encode':
                    shifting_position = alphabet.index(t) + shift_amount
                    shifting_position %= len(alphabet)
                    shifting = alphabet[shifting_position]
                    final_message += shifting
                else:
                    unshifting_position = alphabet.index(t) - shift_amount
                    unshifting_position %= len(alphabet)
                    unshifting = alphabet[unshifting_position]
                    final_message += unshifting
            else:
                continue
            #shifting = alphabet[len(alphabet) - shift_amount:]
            #print("Decoded message :")
    print("Encoded message : " + final_message) if direction=="encode" else print("Decoded message : " + final_message)
    #print("Decoded message : " + decoded_message)

encrypt(text, shift)