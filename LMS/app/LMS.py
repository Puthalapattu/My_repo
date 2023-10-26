# --------- IMPORTS -------------
import os
from datetime import datetime as dt

# import pickle

##################################


def changeDir() -> None:
    os.chdir("LMS")
    os.chdir("app")
    return


def revertDir() -> None:
    os.chdir("../")
    os.chdir("../")
    return


def addBook(name: str, number: int, author: str) -> None:
    changeDir()
    data = {number: {"name": name, "author": author}}
    with open("BookDetails.txt", "a") as fileObject:
        fileObject.write(str(data)[1 : len(data)] + "\n")

        revertDir()


# addBook("self", 123, "deep")


def gatherBooks() -> list:
    changeDir()
    with open("BookDetails.txt") as fileObject:
        books = {}
        for item in fileObject.read().split("\n"):
            if item != "":
                books[int(item[:3])] = eval(item[5:])

        revertDir()

        return books


# START OF LSM CLASS, MAIN CLASS


class LMS:
    def __init__(self) -> None:
        self.books = gatherBooks()
        print(self.books)
        self.users = None


library = LMS()
