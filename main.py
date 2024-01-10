from Book import book
from Bookmanager import bookmanager

manager = bookmanager()
running = True

while running:

    print('''

    1. 
    2. 
    3. 
    4. 
    5. 
    ''')

    menu = input()

    if menu == "1":
        manager.showbooks()
    elif menu == "2":
        title = input("Input book name : ")
        author = input("Input Author : ")
        manager.append(book(title, author))
    elif menu == "3":
        title = input("Title : ")
        manager.removebook(title)
    elif menu == "4":
        title = input("Title : ")
        title2 = input("Title to chage : ")
        manager.modifybook(title, title2)
    elif menu == "5":
        running = False
    else:
        print("Please input the right number !!!")