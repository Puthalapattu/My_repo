# --------- IMPORTS -------------
import os
from datetime import datetime as dt
from pickle import dump, load

##################################


def addBook(name: str, number: int, author: str) -> str:
    with open("BookDetails.txt") as fileObject:
        pass


def gatherBooks() -> list:
    os.chdir("LMS")
    os.chdir("app")

    with open("BookDetails.txt") as fileObject:
        books = {item for item in fileObject.read().split("\n")}
        while "" in books:
            books.remove("")

        os.chdir("../")
        os.chdir("../")

        return books


print(gatherBooks())

# START OF LSM CLASS, MAIN CLASS


# class LMS:
#     def __init__(self) -> None:
#         self.books = gatherBooks()
#         print(self.books)
#         self.users = None


# library = LMS()
