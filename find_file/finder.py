import os
import time
import re
import argparse
import subprocess
from threading import Thread
from colorama import init, Fore, Style
init(autoreset=True)

t1 = time.time()
global t2
t2 = 0
dict1, d = {}, {}


def find(dir):
    for r, folder, file in os.walk(dir):
        for f in file:
            path1 = r+"\\"+f
            dict1[path1] = ""


def finder(args):
    try:
        c = 0
        file, dir = " ".join(args[:-1]), args[-1].upper()
        find(dir)
        global t2
        t2 = time.time()
        for i in dict1:
            if re.search(file, i, re.I):
                c += 1
                d[c] = i
                print(c, ":", Fore.CYAN + Style.BRIGHT + i+"\n")
        open()
    except:
        print("Not found")


def findall(file):
    f = " ".join(file)
    c = 0
    try:
        for i in dict1:
            if re.search(f, i, re.I):
                c += 1
                d[c] = i
                print(c, ":", Fore.CYAN + Style.BRIGHT + i+"\n")
        open()
    except:
        print("Not found")


def open():
    if d != {}:
        a = int(input("Enter the no. of the file you want to open or 0 to exit:"))
        file = d[a]
        subprocess.Popen(f'explorer /select,{file}')
    else:
        print("Not found")


if __name__ == "__main__":

    parse = argparse.ArgumentParser()
    parse.add_argument("-s", nargs="+", help="Takes two argument first the file to search and second the disk name ")
    parse.add_argument("-all", nargs="+", help="Takes one argument ie. filename")

    args = parse.parse_args()

    if args.s:
        finder(args.s)

    if args.all:
        d1 = ["C:\\", "D:\\", "E:\\"]
        l1 = []
        c = 0
        for i in d1:
            process1 = Thread(target=find, args=(i,))
            process1.start()
            l1.append(process1)
        for t in l1:
            t.join()
        findall(args.all)
    print(Fore.MAGENTA + Style.BRIGHT + "Total Files", len(dict1))
    print(Fore.MAGENTA + Style.BRIGHT + "Relevant Files", len(d))

    t2 = time.time()
    print("Total time taken:", t2-t1)
