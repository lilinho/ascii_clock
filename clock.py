import datetime
import time
import os

"""
Definition of function, which will format time -
if hour/minute/second is one-digit - it will add "0" before
and conver rest of it to string.

It returns time in HH:MM:SS format as string
"""


def f_time(t_raw):
    if t_raw.hour < 10:
        formated = '0' + str(t_raw.hour)
    else:
        formated = str(t_raw.hour)
    formated += ':'

    if t_raw.minute < 10:
        formated += '0' + str(t_raw.minute)
    else:
        formated += str(t_raw.minute)
    formated += ':'

    if t_raw.second < 10:
        formated += '0' + str(t_raw.second)
    else:
        formated += str(t_raw.second)

    return formated

"""
Definition of buffer. It containts dictionary in which there are 9
(numerate form 0) fields.

It has also:
clean_buffer method, which cleans dictionary after every second
print_lines method, wich prints large digits made from ASCII (from file)
add_to_buffer method, which adds to dictionary one digit at a time 
"""
class Buffer:
    def __init__(self):
        self.lines = {0: "", 1: "", 2: "", 3: "", 4: "", 5: "", 6: "", 7: "", 8: ""}

    def clean_buffer(self):
        for i in range(0, 9):
            self.lines[i] = ""

    def print_lines(self):
        for i in range(0, 9):
            print(self.lines[i])

    def add_to_buffer(self, c, i):
        self.lines[i] += c + " "

#declaration of buffer, openning file and read line by line from it to list
buf = Buffer()
file = open('digits.txt', 'r')
digit = file.read().split("\n")
file.close()

"""
Infinite loop:
1. Cleans screen
2. Take actual time and format if
3. Search in list of ASCII digits if number in time equals index
4. If it's it split digit list to one specific number and save it to buffer
5. Prints on screen
6. Sleeps for 1 sec
7. Cleans buffer
"""

while True:
    os.system('cls')
    t = f_time(datetime.datetime.now().time())
    for dg in t:
        for i in range(0, len(digit), 10):
            if dg == digit[i]:
                tmp = digit[i+1:]
                for k in range(0, 9):
                    buf.add_to_buffer(tmp[k], k)
    buf.print_lines()
    time.sleep(1)
    buf.clean_buffer()
    

