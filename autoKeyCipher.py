# making shift cipher encryption and decryption using python

import sys
domain = 26
string = "abcdefghijklmnopqrstuvwxyz"

def encryption(userInput, key, domain, string):
    
    cipher = ""
    for i in range(len(key)):
        for j in range(len(string)):
            if string[j] == key[i]:
                k = j

    for i in range(len(userInput)):
        for j in range(len(string)):
            if string[j] == userInput[i]:
                text = (string[(j+k)%domain])
                cipher = cipher + text
                k = j
                
    print(f"The encrypted message is: {cipher}")
    print('\n')

while(True):
    print("Enter your choice(Number): ")
    print("1. Encryption: ")
    print("2. Decryption: ")
    print("3. Exit: ")

    number = int(input("Enter the number: "))

    def choice(number):
        if number == 1:
            userInput = input("Enter your text to encrypt: ")
            key = input("Enter the key: ")
            userInput = userInput.lower()
            encryption(userInput, key, domain, string)
        elif number == 2:
            userInput = input("Enter your text to decrypt: ")
            key = input("Enter the key: ")
            userInput = userInput.lower()
            decryption(userInput, key, domain, string)
        elif number == 3:
            sys.exit()
        else:
            print("Input should be a number from 1 to 3")

    choice(number) 
