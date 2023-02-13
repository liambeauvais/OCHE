import datetime
import locale


class Palindrome():

    def __init__(self, time: datetime.datetime = datetime.datetime.now(),
                 locale_time: locale = locale.getdefaultlocale()[0]):
        self.time = time
        self.locale_time = locale_time

    def part_of_the_day(self) -> str:
        if 5 < self.time.hour < 13:
            return "am"
        elif 13 <= self.time.hour < 19:
            return "pm"
        elif 19 <= self.time.hour < 24:
            return "soir"
        else:
            return "nuit"

    def say_hello(self) -> str:
        if self.locale_time == "fr_FR":
            return "Bonjour " + self.part_of_the_day()
        else:
            return "Hello "

    def say_goodbye(self) -> str:
        if self.locale_time == "fr_FR":
            return "Au revoir "
        else:
            return "Goodbye " + self.part_of_the_day()

    def well_said(self) -> str:
        if self.locale_time == "fr_FR":
            return "Bien dit"
        else:
            return "Well said"

    def mirror(self, input: str) -> str:
        response = self.say_hello()
        response += f"\n{input[::-1]}"

        if input == input[::-1]:
            response += f"\n{self.well_said()}"

        response += f"\n{self.say_goodbye()}"
        return response
