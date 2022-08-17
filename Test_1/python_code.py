from operator import itemgetter
from time import sleep
import re

def test(test):
    a = test.lower()
    b = re.split(r"\W+", a)
    c = dict()
    x = 0
    for i in b:
        c[i] = 0
    for i in b:
        c[i] = c[i] + 1

    spisok = []

    for value in c.items():
        spisok.append(value)
    spisok.sort(reverse=True)
    spisok.sort(key=itemgetter(1), reverse=True)
    return spisok[0:5]


def check_out():
    a = test("Привет а а а а а а а а")
    if (a[0][0] == 'а') and (a[0][1] == 8):
        print('100%')
    else:
        print('0%')


# check_out()

inp = print(test(input("Введите текст:\n")))
sleep(5)