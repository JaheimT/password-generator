# import string → gives access to character sets (letters, digits, symbols)
import string
# import random → used to generate random choices
import random
# Empty string that will store all allowed characters
Password = ""
# Character pool passowrd is being chosen from
CharP = "qwertyuiopasdfghjklzxcvbnm"
# user picks desired lenght of password
length = int(input("what length do u require -   " ))
# if the user says yes numbers are added to the character pool
numbers_choice = input("Include numbers? (y/n): ")
if numbers_choice == "y":
    CharP = CharP + string.digits + "A"
# if the user says yes Uppercase letters are added to the character pool
uppercase_choice = input("Include uppercase? (y/n): ")
if uppercase_choice == "y":
   CharP = CharP + string.ascii_uppercase
# if the user says yes symbols are added to the character pool
punctuation_choice = input("Include symbols? (y/n)?")
if punctuation_choice == "y":
   CharP = CharP + string.punctuation
# pickes random characters from the pool and creates the password
for x in range(length):
   random_char = random.choice(CharP)
   Password += random_char
print (Password)