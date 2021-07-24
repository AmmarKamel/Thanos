import random
import os

path = os.getcwd()
os.chdir(path + "\\Universe")

lst = os.listdir()

while len(lst) > 25:
    n = random.randint(0 , len(lst))
    os.remove(lst[n])
    lst.pop(n)