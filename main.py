from random import *
import pyttsx3
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
print("\n")
print("""
.d8888. db   db  .d8b.  d8888b.  .d88b.  db   d8b   db
88'  YP 88   88 d8' `8b 88  `8D .8P  Y8. 88   I8I   88
`8bo.   88ooo88 88ooo88 88   88 88    88 88   I8I   88
  `Y8b. 88~~~88 88~~~88 88   88 88    88 Y8   I8I   88
db   8D 88   88 88   88 88  .8D `8b  d8' `8b d8'8b d8'
`8888Y' YP   YP YP   YP Y8888D'  `Y88P'   `8b8' `8d8'
""")
print("\n")
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
print("\t^^^^^^^^^^^^^^^^^^^ SHADOW tools ^^^^^^^^^^^^^^^^^^^^^^^^")
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
print(voices[0].id)
def speak(audio: object) -> object:
    engine.say(audio)
    engine.runAndWait()

speak('enter your password')
user_pass = input("enter your password:\n")

password = ['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ]
password1 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

password2 = ['~', '@', '#', '%', '$', '^', '&', '*', '.', ',', ':', '/', '*', '+', '-', '_', '=', '?', '<', '>', '`']

password3 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
             's', 't', 'u', 'v', 'w', 'x', 'y', 'z','0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
             '~', '@', '#', '%', '$', '^', '&', '*', '.', ',', ':', '/', '*', '+', '-', '_', '=', '?', '<', '>', '`']

speak('enter password type(char,int,special,strong:')
type_input = input('enter password type(char,int,special,strong:\a\n')

guess = ''
while guess != user_pass:
    guess = ''
    if 'char' in type_input:
        for letter in range(len(user_pass)):
            guess_letter = password[randint(0, 25)]
            guess = str(guess_letter) + str(guess)
        print(guess)
        file = open("radhey.txt","a+")
        file.write("\n"+guess)
    elif 'int' in type_input:
        for letter in range(len(user_pass)):
            guess_letter = password1[randint(0, 9)]
            guess = str(guess_letter) + str(guess)
        print(guess)
        file = open("radhey.txt","a+")
        file.write("\n"+guess)
    elif 'special' in type_input:
        for letter in range(len(user_pass)):
            guess_letter = password2[randint(0, 20)]
            guess = str(guess_letter) + str(guess)
        print(guess)
        file = open("radhey.txt","a+")
        file.write("\n"+guess)

    elif 'strong' in type_input:
        for letter in range(len(user_pass)):
            guess_letter = password3[randint(0, 56)]
            guess = str(guess_letter) + str(guess)
        print(guess)
        file = open("radhey.txt","a+")
        file.write("\n"+guess)
file.close()
print("your password is:", guess)
speak('password is successfully creaked. ')
speak('and your password is ')
speak(guess)
speak("Thanks for using Shadow Tools.")
