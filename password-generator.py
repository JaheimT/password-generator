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
New_length = 0
# if the user says yes numbers are added to the character pool
numbers_choice = input("Include numbers? (y/n): ")
if numbers_choice == "y":
   # removes 1 unit from the required lenght of the password
   New_length = New_length - 1
   CharP = CharP + string.digits 
   for x in range(1):
       random_num = random.choice(string.digits)
       Password += random_num
# if the user says yes Uppercase letters are added to the character pool
uppercase_choice = input("Include uppercase? (y/n): ")
if uppercase_choice == "y":
   New_length = New_length - 1
   CharP = CharP + string.ascii_uppercase
   for x in range(1):
       random_upper = random.choice(string.ascii_uppercase)
       Password += random_upper
# if the user says yes symbols are added to the character pool
punctuation_choice = input("Include symbols? (y/n): ")
if punctuation_choice == "y":
   New_length = New_length - 1
   CharP = CharP + string.punctuation
   for x in range(1):
       random_pun = random.choice(string.punctuation)
       Password += random_pun
# pickes random characters from the pool and creates the password
for x in range(length + New_length):
   random_char = random.choice(CharP)
   Password += random_char
# turn the string into a list to help shuffle the characters for the password around
password_list = list(Password)
random.shuffle(password_list)
Password = "".join(password_list)
print (Password)