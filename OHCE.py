import datetime
import locale


class Palindrome():

    def __init__(self, time: datetime.datetime = datetime.datetime.now(),
                 locale: locale = locale.getdefaultlocale()[0]):
        self.time = time
        self.locale = locale

    def say_hello(self):
        return "Bonjour"

    def say_goodbye(self):
        return "Au revoir"

    def mirror(self, input: str):
        response = self.say_hello()
        response += f"\n{input[::-1]}"

        if input == input[::-1]:
            response += f"\n{self.well_said()}"

        response += f"\n{self.say_goodbye()}"
        return response

    def well_said(self):
        return "Bien dit"
