import datetime

date = datetime.datetime.now()
print("Bonsoir" if date.hour > 18 or date.hour < 6 else "Bonjour")

user_input = input("quel est votre mot?")
response = user_input[::-1]
print(response)
if response == user_input:
    print("Bien dit!")