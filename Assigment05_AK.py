# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# <Andrew Kehl>,<11/13/2021>,Added code to complete assignment 5/Fixed punctuation and grammatical errors.
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
strFile = "ToDoList.txt"   # An object that represents a file
objFile = None  # file handle
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection
Task = "" #
Priority = ""
# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
strFile = 'ToDoList.txt'
objFile = open(strFile, "r")
for row in objFile:
    strTask, strPriority = row.split(',')
    dicRow = {'Task':strTask, 'Priority':strPriority.strip()}
    lstTable.append(dicRow)

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data.
    2) Add a new item.
    3) Remove an existing item.
    4) Save data to file.
    5) Exit program.
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        print('Current Data:')
        for row in lstTable:
            print(row['Task'] + ' | ' + row['Priority'])
        # TODOONE: Add Code Here
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        print("ToDo List Data Entry")
        Task = input(" Enter a Task: ")  #defined
        Priority = input(" Enter a Priority: ")
        dicRow = {"Task":Task,"Priority":Priority}
        lstTable.append(dicRow)
        for row in lstTable:
            print(row['Task'] + ' | ' + row['Priority'])
        continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        for row in lstTable:
            print(row['Task'] + ' | ' + row['Priority'])
        strItem = input("Task to Remove: ")
        for row in lstTable:
            if row["Task"].lower() == strItem.lower():
                lstTable.remove(row)
                print("Task Removed")
        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        objFile = open("ToDoList.txt", "w")
        for row in lstTable:
            objFile.write(str(row["Task"]) + ',' + str(row["Priority"] + '\n'))
        print(" Data was saved to file: ToDoList.txt. ")
        objFile.close()
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        print('Goodbye!')
        break  # and Exit the program
