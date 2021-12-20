

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encrypt(message, shift):  
    tab = []
    for char in message:
        position = alphabet.index(char)
        new_position = position + shift
        while new_position > alphabet.__len__() - 1:
            new_position -= alphabet.__len__()
        tab.append(alphabet[new_position])
    
    print("".join(tab))

def decrypt(message, shift):
    tab = []
    for char in message:
        position = alphabet.index(char)
        new_position = position - shift
        while new_position < 0:
            new_position += alphabet.__len__()
        tab.append(alphabet[new_position])

    print("".join(tab))

        
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))  