# password-generator
A Basic python script that helps a user generate a pasword
## Goals
build a easy to use tool that genereates passwords 


## initial thoughts (what makes a good password Generator)
- True randomness
- limit character repetition
- large character pool
- good length availability
- No predictable patterns

## Code broken down
- ask user for a desired length
- ask if numbers, symbols, or both are required
- build a pool of random characters
- randomly select a character
- combined into a password
- print result

## What I Struggled With
- How to pull a random character from a pool
- adding numbers
- adding upper or lower case characters
- the programe would add only lowercase even if uppercase was selected
- If a user selected an option would only be added to the character pool and not garenteed to be in the password
- forced characters would be at the start making password more predictable


## How I Solved It
- used learned how to use the random import correctly
- used Sting iport then the respective methods such as string.ascii_lowercase , string.digits , string.ascii_uppercase
- i relised that i had repeted logic that would make the character pool be dominated by lowecase characters

## What I Learned 
- how to properly use the string method
- better understading of operators

## Future Improvements
