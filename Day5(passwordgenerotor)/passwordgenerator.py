import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
password=""
for char in range(1, nr_letters + 1):
  password += random.choice(letters)
for char in range(1, nr_symbols + 1):
   password += random.choice(symbols)
for char in range(1, nr_numbers + 1):
   password += random.choice(numbers)
print(password)
# now the passowrd has some pattern lets makes the pattern random
list1=[]
def Convert(string):
   
    list1[:0]=string
    return list1

print(Convert(password))
random.shuffle(list1)
print(list1)
password_random = ""
for char in list1:
  password_random += char

print(f"Your password is: {password_random}")
