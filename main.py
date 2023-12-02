from book import book
from bookmanager import bookmanager

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
        
        manager.appendbook(book(title, author))
    elif menu == "3":
        pass
    elif menu == "4":
        pass
    elif menu == "5":
        running = False
    else:
        print("Put right input")