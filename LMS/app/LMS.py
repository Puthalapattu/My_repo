# --------- IMPORTS -------------
import os
from datetime import datetime as dt
from pickle import dump, load

##################################

# START OF LSM CLASS, MAIN CLASS

data = 9


class LMS:
    def __init__(self) -> None:
        self.books = data
        print(self.books)


library = LMS()
