import string

lowercase_letters = string.ascii_lowercase
uppercase_letters = string.ascii_uppercase

# TASK 1

def caesar_encoder(text, shift_value):
    ### This function encodes a given plain text using the caesar cipher encoding. The words are pushed by the shift_value times to the left. For example, letter A + 4 is going to be letter E. E.g. casear_encoder("Python", 5) -> "Udymts"... Approach -> Use loop and ascii letters, for some reason, I'm having an hard time getting chr and ord to work.###
    encoded_string = ""
    for letter in text:
        if letter in lowercase_letters:
            letter_position = lowercase_letters.find(letter) + 1
            #print(letter_position)
            new_position = (letter_position + shift_value) % 26
            #print(new_position)
            encoded_string += lowercase_letters[new_position - 1] 
        elif letter in uppercase_letters:
            letter_position = uppercase_letters.find(letter) + 1
            new_position = (letter_position + shift_value) % 26
            encoded_string += uppercase_letters[new_position - 1]
        else:
            print("OOPS! What you've inputted is not a valid letter of the english Alphabet and that is my only use case.")
    return encoded_string
print(caesar_encoder("Python", 5))
print(caesar_encoder("ADEWALE", 1))
print(caesar_encoder("Zyxy", 5))


# TASK 2

def caesar_decoder(encoded_string, shift_value):
    ### This function decodes already encoded strings back to the plain text form. E.g. caesar_decoder("Udymts") -> 'Python'###
    decoded_string = ""
    for letter in encoded_string:
        if letter in lowercase_letters:
            letter_position = lowercase_letters.find(letter) + 1
            #print(letter_position)
            new_position = (letter_position - shift_value) % 26
            #print(new_position)
            decoded_string += lowercase_letters[new_position - 1]
        elif letter in uppercase_letters:
            letter_position = uppercase_letters.find(letter) + 1
            new_position = (letter_position - shift_value) % 26
            decoded_string += uppercase_letters[new_position - 1]
        else:
            print("OOPS! What you've inputted is not a valid letter of the english Alphabet and that is my only use case.")
    return decoded_string
print(caesar_decoder("Udymts", 5))
print(caesar_decoder("Edcd", 5))

# TASK 3

def caesar_cipher(input_text, shift_value, decision):
    ### This function performs the caesar cipher operations on an input_text. If user says encode or True, then the text is encoded, but if decode or false is said then the input_text is decode. E.G. casear_cipher("Python", 5, True) -> "Udymts"###
    if decision == True or decision.lower() == "encode":
        return caesar_encoder(input_text, shift_value)
    elif decision == False or decision.lower() == "decode":
        return caesar_decoder(input_text, shift_value)

print(caesar_cipher("Python", 5, True))
print(caesar_cipher("Edcd", 5, "decode"))