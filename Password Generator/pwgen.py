import random

print("Password Generator")

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*?.,()0123456789"

num = input("Amount of your password to generate: ")

num = int(num)

length = input("Input your password length: ")

length = int(length)

print("there are your passwords")

for pwd in range(num):
	passwords = ""
	for c in range(length):
		passwords += random.choice(chars)
	print(passwords)
