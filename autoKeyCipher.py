# making autokey cipher cipher encryption and decryption using python

import sys
import os


design = """
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
+     _         _                              ___ _       _                +
+    /_\  _   _| |_ ___     /\ /\___ _   _    / __(_)_ __ | |__   ___ _ __  +
+   //_\\| | | | __/ _ \   / //_/ _ \ | | |  / /  | | '_ \| '_ \ / _ \ '__| +
+  /  _  \ |_| | || (_) | / __ \  __/ |_| | / /___| | |_) | | | |  __/ |    + 
+  \_/ \_/\__,_|\__\___/  \/  \/\___|\__, | \____/|_| .__/|_| |_|\___|_|    +
+                                  |___/          |_|                       +
+                                                           -By 7omahawk    +
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""


domain = 26
string = "abcdefghijklmnopqrstuvwxyz"

# this is the encryption part
def encryption(userInput, key, domain, string):
    
    # making the value of key 
    for i in range(len(key)):
        for j in range(len(string)):
            if string[j] == key[i]:
                k = j   # the value of the key

    # using the value of key making the cipher
    cipher = ""
    for i in range(len(userInput)):
        for j in range(len(string)):
            if string[j] == userInput[i]:
                text = (string[(j+k)%domain])
                cipher = cipher + text
                k = j    # store next letters key
                
    print(f"The encrypted message is: {cipher}")
    print('\n')

# the decryption part will be added here
def decryption(userInput, key, domain, string):
    
    cipher = ""
    # making the value of key 
    for i in range(len(key)):
        for j in range(len(string)):
            if string[j] == key[i]:
                k = j      # the value of the key

    # using the value of key making the cipher
    for i in range(len(userInput)):
        for j in range(len(string)):
            if string[j] == userInput[i]:
                text = (string[(j-k)%domain])
                cipher = cipher + text
                k = (j-k)%domain   # store next letters key
                
    print(f"The encrypted message is: {cipher}")
    print('\n')


# choice the what you need to do (encrypt/decrypt)
while(True):
    print(design)
    print("Enter your choice(Number): ")
    print("1. Encryption: ")
    print("2. Decryption: ")
    print("3. Exit: ")

    number = int(input("Enter the number: "))

    def choice(number):
        if number == 1:
            userInput = input("Enter your text to encrypt (A-Z): ")
            key = input("Enter the key (any alphabet, ex: m): ")
            userInput = userInput.lower()
            encryption(userInput, key, domain, string)
        elif number == 2:
            userInput = input("Enter your text to decrypt (A-Z): ")
            key = input("Enter the key (any alphabet, ex: m): ")
            userInput = userInput.lower()
            decryption(userInput, key, domain, string)
        elif number == 3:
            sys.exit()
        else:
            print("Input should be a number from 1 to 3")

    choice(number) 

    input()             # press enter to clear screen
    os.system('clear')  # clear screen
