# import only system from os
from os import system, name

# import sleep to show output for some time period
from time import sleep

# define our clear function
class Clear: 

    def clear(self):
        # for windows
        if name == 'nt':
            _ = system('cls')
        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')

    def sleep(self, duration: int=3):
        sleep(duration)