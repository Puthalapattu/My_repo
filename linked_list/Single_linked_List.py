"""
# check the Log_files\Linked_List_Log.txt file for a log saving format
"""

# -----imports------
import os

from datetime import datetime, date

####################


class Node:
    # Initializing constructor
    def __init__(self, data: int):
        self.data = data
        self.next = None


class SLL:
    # defining class variables (we can use in entire program)
    __size_of_sll = list()
    __deleted_count = 0
    __deleted_calls = 0
    __original_time = str(datetime.now())[11:19]

    # Initializing constructor
    def __init__(self) -> None:
        self.head = self.tail = Node(None)

    # Method to add an item to Linked List at front everytime when it is called
    def insertAtFront(self, data: int) -> None:
        newnode = Node(data)
        # Check if the linked list is empty or not
        if self.head.data is None:
            self.head = self.tail = newnode
            print("\nAn empty head is created with data: ", data, "\n")

            # UPDATING SIZE OF SLL LIST EVRY TIME A NEW ITEM ADDED

            SLL.__size_of_sll.append(self.length())

            # only if there is some data in linked list----------------
        else:
            current = self.head
            self.head = newnode
            newnode.next = current
            print("\nNewNode", newnode.data, "connected to:", current.data, "\n")

            # UPDATING SIZE OF SLL LIST EVRY TIME A NEW ITEM ADDED

            SLL.__size_of_sll.append(self.length())

            # -----------------------------------------------------

    # Method to check if the linked list is empty or not
    def check_sll(self) -> bool:
        if self.head.data is None:
            return True
        else:
            return False

    # Method to Add item at end of linked list
    def insertAtEnd(self, item: int) -> None:
        newnode = Node(item)
        # Check if the linked list is empty or not
        if self.head.data is None:
            self.head = self.tail = newnode
            print("\nAn empty head is creted with data ", self.head.data, "\n")

            # UPDATING SIZE OF SLL LIST EVRY TIME A NEW ITEM ADDED

            SLL.__size_of_sll.append(self.length())

            # -----------------------------------------------------

        else:
            current = self.tail
            current.next = newnode
            self.tail = newnode
            print("\nNewNode", newnode.data, "connected to: ", current.data, "\n")

            # UPDATING SIZE OF SLL LIST EVRY TIME A NEW ITEM ADDED

            SLL.__size_of_sll.append(self.length())

            # -----------------------------------------------------

    # Method to get the lenght of the linked list ( How many items or elements are present in linked list )
    def length(self) -> int:
        if self.head.data is None:
            return 0
        else:
            count = 1
        current = self.head
        while current.next is not None:
            count += 1
            current = current.next
        return count

    # Method to Add item at spesified position of linked list
    def insertAtPosition(self, item: int, position: int) -> None:
        count = 1
        # Check if the linked list is empty or not
        if self.head.data == 0:
            print("\nSLL is empty\n")
        else:
            # make sure that POSITION attribute is POSITIVE and LESS THAN the length of linked list
            if position > 1 and position > 0 and position < self.length():
                newnode = Node(item)
                current = self.head
                while count != position - 1:
                    count += 1
                    current = current.next
                print("\nconnected to", current.data, "\n")
                newnode.next = current.next
                current.next = newnode

                # UPDATING SIZE OF SLL LIST EVRY TIME A NEW ITEM ADDED

                SLL.__size_of_sll.append(self.length())

                # -----------------------------------------------------
            elif self.length() == position:
                self.insertAtEnd(item)
            elif position == 1:
                self.insertAtFront(item)
            else:
                if position < 0:
                    print("\nYou just entered a negative position\n")
                else:
                    print(
                        "\nposition not found,just know the length of SLL and try again\n"
                    )

    # Method to delete an item at the end of the linked list
    def detletAtEnd(self) -> None:
        print("\nBefore 'Delete at End' operation linked list is :\n")
        # Display the linked list every time brfore deleting data from the linked list
        self.display()
        # Check if the linked list is empty or not
        if self.head.data is None:
            print("\nSLL is empty\n")
        else:
            if self.length() > 1:
                current = self.head
                while current.next.next is not None:
                    current = current.next
                print("\nDeleted node at end having data:", self.tail.data, "\n")
                # getting the list of sll
                linked_list_now = self.slltolist()
                SLL.__deleted_count += 1
                # -------------------------------
                # call the create_log() method with deleted node and linked list
                self.create_log(
                    deleted_data=self.tail.data,
                    linked_list=linked_list_now,
                    delete_type="Delete At End",
                )
                # ---------------------------------------------------------------
                self.tail.data = None
                self.tail = current
                current.next = None
                print("\nAfter 'Delete at End' operation linked list is :\n")
                self.display()

            else:
                print("SLL is not having more than one item to delete!\n")

    # Method to delete an item at the front of the linked list
    def deleteAtFront(self) -> None:
        print("\nBefore 'Delete at Front' operation linked list is :\n")
        # Display the linked list every time brfore deleting data from the linked list
        self.display()
        # Check if the linked list is empty or not
        if self.head.data is None:
            print("\nSLL is empty\n")
        else:
            if self.length() > 1:
                print("\nDeleted node at front having data:", self.head.data, "\n")
                # getting the list of sll
                linked_list_now = self.slltolist()
                # -------------------------------
                SLL.__deleted_count += 1
                # call the create_log() method with deleted node and linked list
                self.create_log(
                    deleted_data=self.head.data,
                    linked_list=linked_list_now,
                    delete_type="Delete At Front",
                )
                # ---------------------------------------------------------------
                current = self.head
                current = current.next
                self.head.data = None
                self.head.next = None
                self.head = current
                print("\nAfter 'Delete at Front' operation linked list is :\n")
                self.display()

            else:
                print("SLL is not having more than one item to delete!\n")

    # Method to delete an item at the position of the linked list
    def deleteAtposition(self, position: int):
        print("\nBefore 'Delete at Position' operation linked list is :\n")
        # Display the linked list every time brfore deleting data from the linked list
        self.display()
        # Check if the linked list is empty or not
        if self.head.data is None:
            print("\nSLL is empty!\n")
        else:
            current = self.head
            if position == self.length():
                self.detletAtEnd()
            elif position < self.length():
                count = 1
                while current.next is not None:
                    if count == position - 1:
                        break
                    else:
                        count += 1
                        current = current.next
                print("\nDeleted node having data:", current.next.data, "\n")

                # getting the list of sll
                linked_list_now = self.slltolist()
                # -------------------------------
                SLL.__deleted_count += 1
                # call the create_log() method with deleted node and linked list
                self.create_log(
                    deleted_data=current.next.data,
                    linked_list=linked_list_now,
                    delete_type="Delete At Position",
                )
                # ---------------------------------------------------------------

                current.next.data = None
                current.next = current.next.next
                print("\nAfter 'delete at Position' operation linked list is :\n")
                self.display()

            elif position == 1:
                self.deleteAtFront()
            else:
                print("\nPosition not found\n")

    # Method to get the item value with the help of position
    def getvalue(self, position: int) -> int:
        if self.check_sll():
            print("\nSLL is empty\n")
        elif position < self.length():
            current = self.head
            count = 1
            while current.next is not None:
                if count == position:
                    return current.data
                else:
                    count += 1
                    current = current.next
        else:
            return self.tail.data

    # Method to display the linked list
    def display(self) -> None:
        current = self.head
        if current.data is None:
            print("\nEmpty linked list!\n")
        else:
            print("\n", current.data, end=" ")
            while current.next is not None:
                current = current.next
                print("-->", current.data, end=" ")
            print("\n")
        return

    # Method to convert the Linked list into a list of items for better manipulation of data
    def slltolist(self) -> list:
        l = list()
        current = self.head
        l.append(current.data)
        while current.next is not None:
            current = current.next
            l.append(current.data)
        return l

    # Method to convert the given list into an linked list ( Every element of list, is added at the end of linked list )
    def listtosll(self, list1: list) -> None:
        if type(list1) == list:
            for i in list1:
                self.insertAtEnd(i)
        else:
            print("\nexpected list but :", type(list1), "given\n")

    # Method to get the head and tail of linked list ( we can use this When linked list is too big )
    def gethead_and_tail(self) -> int:
        return (self.head.data, self.tail.data)

    # Method to get the position of the linked list item or element with the help of item value (data part of a Node in linked list) of linked list
    def getPosition(self, item: int) -> int or bool:
        if self.check_sll() is not True and item in self.slltolist():
            count = 1
            current = self.head
            while current.next is not None:
                if item != current.data:
                    current = current.next
                    count += 1
                else:
                    return count
        return False

    # ----------- creating a log for linked list -------------------------------------------------#

    def create_log(
        self,
        exit_selected: bool = False,
        deleted_data: any = None,
        delete_type: str = None,
        linked_list: list = None,
        user_requested_log=False,
    ) -> None:
        if os.path.exists("Log_files\\linked_list_log.txt"):
            # ------------ TASK1 : (REPEATED TASK for every delete operation) ---------------------------#
            # creating a new file if not exist in present working directory

            # opening the Linked_List_file in append mode as a file_object
            with open("Log_files\\linked_list_log.txt", "a") as file_object:
                today_date = date.today()

                if not SLL.__deleted_calls:
                    # Writing the initial data into the file linked_list_log.txt
                    file_object.write(
                        "DATA ENTERED INTO THIS FILE @ DATE \33 {present_date} @ TIME \33 {time_today}\n\n".format(
                            present_date=today_date, time_today=SLL.__original_time
                        )
                    )

                if deleted_data != None:
                    # incrimenting  "__deleted_calls"  variable of class SLL for every delete operation performed
                    SLL.__deleted_calls += 1

                    # writing the data to the log file for a delete operation into the file linked_list_log.txt
                    file_object.write(
                        "-- DELETE OPERATION {delete_call} --\n\
                TIME WHEN DELETE OPERATION PERFORMED : \33 {time}\n\
                DATA ##-\33 {deleted_data_now} \33-## DELETED FROM SLL WITH DELETE TYPE ##-\33 {deleted_type_now} \33-##\n\
                SLL BEFORE DELETING DATA : \33 {linked_list_now}\n\n".format(
                            delete_call=SLL.__deleted_calls,
                            time=str(datetime.now())[11:19],
                            deleted_data_now=deleted_data,
                            deleted_type_now=delete_type,
                            linked_list_now=linked_list,
                        )
                    )

                if SLL.__deleted_calls == 0:
                    # if __deleted_calls is 0 then that means no delete operation is performed we write data in below formatinto the file linked_list_log.txt
                    file_object.write(
                        "Entry @ \33 {today_date} @ TIME \33 {today_time}\n\
                NO DELETE OPERATIONs IS PERFORMED\n\n".format(
                            today_date=today_date, today_time=str(datetime.now())[11:19]
                        )
                    )

                if user_requested_log:
                    # if user requests any log to save then we write this data into the file linked_list_log.txt
                    file_object.write(
                        "\33-- USER REQUESTED LOG --\33\n\
                LINKED LIST WHEN USER REQUESTED FOR LOG : \33 {linked_list_now}\n\n\
                TIME WHEN USER REQUESTED FOR A LOG TO SAVE : \33 {time} \n\n".format(
                            linked_list_now=linked_list, time=str(datetime.now())[11:19]
                        )
                    )
                # ------------ TASK1 ENDS ----------------------------------------#

                # ------------ TASK2 STARTS ( when user selected exit option this will run ) ----------------------------------------#
                if exit_selected:
                    # whenever user selects the exit option(choice) then we write the finalized below data into the file linked_list_log.txt
                    file_object.write(
                        "- LINKED LIST STATUS WHEN USER SELECTED EXIT OPTION -\n\n\
                TIME : \33 {today_time}\n\
                LINKED LIST BEFORE SELECTING EXIT OPTION : \33 {linked_list_now}\n\n\
                TOTAL DELETE OPERATIONS PERFORMED : \33 {deleted_count}\n\
                MAX LENGTH OF SLL CREATED TODAY : \33 {max_count}\n\n".format(
                            today_time=str(datetime.now())[11:19],
                            linked_list_now=linked_list,
                            deleted_count=SLL.__deleted_count,
                            max_count=(lambda sll: len(sll) > 0 and max(sll) or "0")(
                                SLL.__size_of_sll
                            ),
                        )
                    )
                    # Add a seperator so that we can easily separate logs from each other
                    file_object.write(
                        "##################################################################################################################################################\n\n"
                    )
                return
            # ------------ TASK2 ENDS ----------------------------------------#


# ----------- creating a logs for linked list ends --------------------------------#

############################# DRIVE CODE STARTS ####################################

c = SLL()

while True:
    print(
        "choices are: \n\n 1--> insert At Front\n 2--> Insert At End\n 3--> Display\n 4--> insert at position\
        \n 5--> Delete node at end\n 6--> Delete node at front\n 7--> Delete with position\n 8--> Convert list to SLL\n 9--> Convert SLL to list\n10--> Get value with popsition\
        \n11--> get Position of element with value\n12--> Length of SLL\n13--> Get The Head and Tail of SLL\n14--> is Empty\n15--> Create A LOG manually (current SLL will be saved)\n16--> Exit\n"
    )
    try:
        ch = int(input("Enter your choice: "))
    except ValueError:
        print("\nAn error occured!\n")
        continue
    except:
        print("\nsomething went wrong!\n")
        break

    if ch == 1:
        try:
            a = int(input("\nEnter the element to insert: "))
        except:
            print("\noops!, Sorry at present only integer's are allowed\n")
            continue
        c.insertAtFront(a)

    elif ch == 2:
        try:
            n = int(input("\nEntre item to insert: "))
        except:
            print("\noops!, Sorry at present only integer's are allowed\n")
            continue
        c.insertAtEnd(n)

    elif ch == 3:
        c.display()

    elif ch == 4:
        try:
            n = int(input("\nEnter data to be inserted: "))
        except:
            print("\noops!, Sorry at present only integer's are allowed\n")
            continue
        try:
            p = int(input("\nEnter the position where to insert: "))
        except:
            print("\nEnter a proper position\n")
            continue
        c.insertAtPosition(n, p)

    elif ch == 5:
        c.detletAtEnd()

    elif ch == 6:
        c.deleteAtFront()

    elif ch == 7:
        try:
            p = int(input("\nEnter the position to delete: "))
        except:
            print("\nEnter a proper position\n")
            continue
        c.deleteAtposition(p)

    elif ch == 8:
        try:
            l = [
                int(x)
                for x in input("\nEnter list elements by comma(','): ").split(",")
            ]
            c.listtosll(l)
        except ValueError:
            print("\noops!, Sorry at present only integer's are allowed\n")

    elif ch == 9:
        if c.check_sll() is not True:
            print("\nConvertion of SLL to list is successfull!", c.slltolist(), "\n")
        else:
            print("\nSLL is empty!\n")

    elif ch == 10:
        try:
            n = int(input("\nEnter position to get data: "))
        except:
            print("\nEnter valid input for the position of sll elements\n")
            continue
        if n <= c.length():
            print("\nThe value at position", n, "is:", c.getvalue(n), "\n")
        else:
            print(
                "\nPosition {} is not found check the length of sll and try again!.".format(
                    n
                ),
                "\n",
            )

    elif ch == 11:
        if c.check_sll() is not True:
            try:
                item = int(input("\nEnter the SLL element to get position: "))
            except:
                print("\nEnter a valind input\n")
                continue
            if c.getPosition(item):
                print("\n", item, "found at position", c.getPosition(item), "\n")
            else:
                print(item, "not found in SLL.\n")
        else:
            print("\nSLL is empty!\n")

    elif ch == 12:
        if c.check_sll():
            print("\nSLL is empty!\n")
        else:
            print("\nlength of SLL is :", c.length(), "\n")

    elif ch == 13:
        if c.check_sll():
            print("\nSLL is empty\n")
        print("\n(Head, Tail) =", c.gethead_and_tail(), "\n")

    elif ch == 14:
        if c.check_sll():
            print("\nLinked list is empty.\n")
        else:
            print("\nLinked list is not empty.\n")

    elif ch == 15:
        if c.check_sll():
            print("Linked list is empty at present!\n")
            continue
        else:
            linked_list_now = c.slltolist()
            c.create_log(
                exit_selected=False,
                linked_list=linked_list_now,
                user_requested_log=True,
            )
            print("User requested log created!\n")

    elif ch == 16:
        linked_list = c.slltolist()
        c.create_log(exit_selected=True, linked_list=linked_list)
        break
    else:
        print("\ninvalid choice!\n")

############################# DRIVE CODE ENDS ####################################

# --------------- NEW VERSION WITH LOGS OF DATA WE STORE---------------------#

"""
~~~~~~~~~~~ WHICH MODULES WE NEED TO IMPORT ~~~~~~~~~~~~~~~~

import os
from datetime import datetime, date

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

###### 

       now we need to create a log file:
       firstly we need to create a file named --'Linked_List_log'--
       check file --"linkedlistlogformat.png" FOR FORMAT

######

for the FOLLOWING content we are going to create a fun :- def create_log() WITH ONE PERAMETER - 'exit_selected = None' which is defaulty set to none


#### To do all these we have to maintain some values of sll
     we are going to introduce some new variables in sll class
  --
    __size_of_sll : list to keep track of size of sll
    __delete_count : to count how many delete operations perfoemed 
    __deleted_calls : to know how many time create_log() method called
    __original_time : to know when the program is started
  --
  Note : we are going to write when the delete operation performed and which data is deleted and sll befor deleting that data

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 ~$~ keep in checks :
        -- every time adding new data to sll update the 'size_of_sll' list with size of sll
        -- evry time any delete operation performed call 'create_log()' method

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ------------- WE NEED TO CREATE LOG : IN THE BELOW FORMAT ----------------------------#
     ---task1 (repeated task)
           -- created DATE and TIME
           -- if we are deleting data:
             --- (for every delete operation) DELETE OPERATION PERFORMED :
               -- time when delete operation performed --
               -- DATA DELETED with type of operation --
               -- LINKED LIST BEFORE DELETE OPERATION PERFORMED --
             ---
           -- if no delettions then:
              say : NO DELETIONS
           --
           -- if user requested any log to save :
              -- LINKED LIST when user requested to save log
              -- TIME when user requested for log
           --
    ---task1 ends

    ---task2 (runs only once when user selected exit option):
           --- LINKED LIST STATUS WHEN USER SELECTED EXIT OPTION ---
              -- LINKED LIST BEFORE SELECTING EXIT OPTION --
              -- Total deletete operations performed -- 
              -- MAX SIZE OF LINKED LIST CREATED --
    ---task2 ends

# ---

 THE create_log() FUNCTION IS CALLED WHEN USER DELETES THE DATA FROM THE LINKED LIST: 

#-------------------------------------------
"""

# --------------- NEW VERSION WITH LOGS OF DATA WE STORE---------------------#
