import os
import sys


def readFile():
    with open("README.txt","r") as f:
        print(f.readline().strip())
        print("hello")

readFile()
