alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.
def encrypt(original_text, shift_amount):

# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
#  by the shift amount and print the encrypted text.
    encoded_message= ""
    decoded_message = ""
    if direction == 'encode':
        print("Encrypting...")
    elif direction == 'decode':
        print("Decrypting...")
    else:
        print("Invalid input")

    for t in original_text:
        for a in alphabet:
            if t == a:
                if direction == 'encode':
                    shifting_position = alphabet.index(t) + shift_amount
                    shifting_position %= len(alphabet)
                    shifting = alphabet[shifting_position]
                    encoded_message += shifting
                else:
                    unshifting_position = alphabet.index(t) - shift_amount
                    unshifting_position %= len(alphabet)
                    unshifting = alphabet[unshifting_position]
                    decoded_message += unshifting
            else:
                continue
            #shifting = alphabet[len(alphabet) - shift_amount:]
            #print("Decoded message :")
    print("Encoded message : " + encoded_message)
    print("Decoded message : " + decoded_message)
# TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?

# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.
#H E L L O
encrypt(text, shift)