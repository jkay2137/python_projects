import art

print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caeser(message, shift, choose):
    new_text = ""
    if choose == "encode" or choose == "decode":
        for char in message:
            position = alphabet.index(char)
            if choose == "encode":
                new_position = position + shift
                while new_position > alphabet.__len__() - 1:
                    new_position -= alphabet
                new_text += alphabet[new_position]
            else:
                new_position = position - shift
                while new_position < 0:
                    new_position += alphabet.__len__()
                new_text += alphabet[new_position]
    if choose == "decode":
        print(f"The decoded message is:\t {new_text}")
    elif choose == "encode":
        print(f"The encoded message is:\t {new_text}")
    else:
        print("Wrong option. Try again.")

        
while True:        
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caeser(text, shift, direction)

    decision = input("Do you want again? [Y/n]: ").lower()

    if decision == "" or decision == "y":
        continue
    else:
        break 
