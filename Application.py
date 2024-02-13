import os
from Book import Book
from common import input_int
from common import tryinput_int
from Edit import Edit
class Application:
    def __init__(self):
        self.E = Edit
        self.E.genres= list()
        self.E.books = list()
        self.E.users = list()
        self.E.checkouts = list()
        
    def run(self):
        self.load()
        while True:
            key = self.select_menu()
            if key == '0':
                break
            elif key ==  '1':
                while True:
                    key_a = self.add_menu()
                    if key_a == '0':
                        break
                    elif key_a == '1':
                        Edit.add_genre(self.E)
                    elif key_a == '2':
                        Edit.add_book(self.E)
                    elif key_a == '3':
                        Edit.add_user(self.E)
                    else:
                        print("Chossed wrong.")
                    input("Press enter.")
            elif key =='2':
                while True:
                    key_s = self.search_menu()
                    if key_s == '0':
                        break
                    elif key_s == '1':
                        Edit.find_book_veiw(self.E)
                    elif key_s == '2':
                        Edit.find_user_veiw(self.E)
                    elif key_s == '3':
                        Edit.view_all(self.E)
                    else:
                        print("Chossed wrong.")
                    input("Press enter.")
            elif key == '3':
                while True:
                    key_d = self.delete_menu()
                    if key_d == '0':
                        break
                    elif key_d == '1':
                        Edit.remove_book(self.E)
                    elif key_d == '2':
                        Edit.remove_user(self.E)
                    else:
                        print("Chossed wrong.")
                    input("Press enter.")
            elif key == '4':
                while True:
                    key_c = self.checkout_menu()
                    if key_c == '0':
                        break
                    elif key_c == '1':
                        Edit.do_checkout(self.E)
                    elif key_c == '2':
                        Edit.return_checkout(self.E)
                    elif key_c == '3':
                        Edit.view_checkouts(self.E)
                    else:
                        print("Chossed wrong.")
                    input("Press enter.")
            else:
                print("Chossed wrong.")
            input("Press enter.")
        Edit.save(self.E)
    
    
        
    def load(self):
        print("===Load===")
        try:
            Edit.load_genres(self.E)
            Edit.load_books(self.E)
            Edit.load_useres(self.E)
            Edit.load_checkouts(self.E)
        except:
            print("Welcome")
        input("Press Enter.")
    
    def select_menu(self):
        os.system("cls")
        print("==  Library management programm ==")
        print("1:Registration ")
        print("2:Search")
        print("3:Delete ")
        print("4:Checkout & Return")
        print("0:Exit program")
        return input("\nInput menu ◀:")
    
    def add_menu(self):
        os.system("cls")
        print("1:Add Genre")
        print("2:Add Book")
        print("3:Add User ")
        print("0:Return to Main")
        return input("\nInput menu ◀:")
    
    def search_menu(self):
        os.system("cls")
        print("1:Search Book")
        print("2:Find User")
        print("3:View Everything")
        print("0:Return to Main")
        return input("\nInput menu ◀:")
    
    def delete_menu(self):
        os.system("cls")
        print("1:Delete Book")
        print("2:Remove User")
        print("0:Return to Main")
        return input("\nInput menu ◀:")
    
    def checkout_menu(self):
        os.system("cls")
        print("1:Checkout")
        print("2:Return book")
        print("3:View all chekcouts")
        print("0:Return to Main")
        return input("\nInput menu ◀:")