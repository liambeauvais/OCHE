import datetime
import locale


class Palindrome():

    def __init__(self, time: datetime.datetime = datetime.datetime.now(),
                 locale: locale = locale.getdefaultlocale()[0]):
        self.time = time
        self.locale = locale

    def say_hello(self):
        if self.locale == "fr_FR":
            return "Bonjour"
        else:
            return "Hello"

    def say_goodbye(self):
        if self.locale == "fr_FR":
            return "Au revoir"
        else:
            return "Goodbye"

    def well_said(self):
        if self.locale == "fr_FR":
            return "Bien dit"
        else:
            return "Well said"

    def mirror(self, input: str):
        response = self.say_hello()
        response += f"\n{input[::-1]}"

        if input == input[::-1]:
            response += f"\n{self.well_said()}"

        response += f"\n{self.say_goodbye()}"
        return response


