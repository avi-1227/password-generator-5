import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'A', 'B', 'C', 'D', 'E', 'F']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '@', '$', '*','&']

print("Welcome to the PyPassword Generator!")
pw_letters = int(input("How many letters would you like in your password?\n"))
pw_symbols = int(input('How many symbols would you like?\n'))
pw_numbers = int(input("How many numbers would you like?"))

# Easy Level Example
# password_generator = ""
# for ltr in range(1, pw_letters+1):
#     password_generator+= random.choice(letters)
    
# print(password_generator)


# Hard level
password_list = []
for ltr in range(1, pw_letters+1):
    password_list.append(random.choice(letters))

for ltr in range(1, pw_symbols+1):
    password_list.append(random.choice(symbols))

for ltr in range(1, pw_numbers+1):
    password_list.append(random.choice(numbers))
    
random.shuffle(password_list)

password = ""
for char in password_list:
    password+=char

print(f'Your password is {password}')