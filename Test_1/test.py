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
    x = 0
    test1 = 'Привет а а а а а а а а'
    a = test(test1)
    print(a)
    print(f"TEST #1 {test1}\n")
    if (a[0][0] == 'а') and (a[0][1] == 8):
        x = x + 1
    else:
        x = x

    test2 = 'Привет, привет ПРИВЕТ привет!!! пока пока'
    a = test(test2)
    print(a)
    print(f"TEST #2 {test2}\n")

    if (a[0][0] == 'привет') and (a[0][1] == 4):
        x = x + 1
    else:
        x = x

    print(f'Result: {(x*100)/2}')


check_out()

sleep(5.2)

