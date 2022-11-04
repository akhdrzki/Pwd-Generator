import random

print("Password Generator")

#variable include the characters that will be random generate
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*?.,()0123456789"

#to input how much u gonna get passwords
num = input("Amount of your password to generate: ")

num = int(num)

#length of your passwords that u wanna get
length = input("Input your password length: ")

length = int(length)

print("there are your passwords")

#generate the passwords
for pwd in range(num):
	passwords = ""
	for c in range(length):
		passwords += random.choice(chars)
	print(passwords)
