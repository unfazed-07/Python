import string
import random

def createpassword(password_length, string_character=True, special_character=True):

    number = string.digits
    letter=string.ascii_letters
    special=string.punctuation

    password = ''
    has_number=False
    has_special_character=False
    meets_criteria=False
    while len(password)!=password_length and meets_criteria==False:
        selected_char = random.choice([number, letter, special])
        finally_chosen = random.choice(selected_char)
        password+=finally_chosen

        
        
        if finally_chosen in number:
            has_number=True
        if finally_chosen in special:
            has_special_character = True

        if string_character:
            meets_criteria=has_number
        if special_character:
            meets_criteria=has_special_character and has_special_character
    return password

print(createpassword(10, False, False))
