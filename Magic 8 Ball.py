print("This program is a Virtual Magic 8 Ball")
print("Enter question: ")
question = input()
import random
value = random.randint(0,25)    
if value in range(0,5):
    print("No.")
if value in range(5,10):
    print("Yes.")
if value in range(10,15):
    print("Most likely.")
if value in range(15,20):
    print("Outlook not so good.")
if value in range(20,25):
    print("It is certain.")
