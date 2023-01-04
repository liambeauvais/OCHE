import datetime
import locale

date = datetime.datetime.now()
if locale.getdefaultlocale()[0] == "fr_FR":
    print("Bonsoir" if date.hour > 18 or date.hour < 6 else "Bonjour")
else:
    print("Good evening" if date.hour > 18 or date.hour < 6 else "Good morning")

user_input = input("quel est votre mot?")
response = user_input[::-1]
print(response)
if response == user_input:
    print("Bien dit!")
