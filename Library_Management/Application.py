import os
from common import input_int
from common import tryinput_int
from Edit import Edit
class Application:
    def __init__(self):
        self.E = Edit()
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
                        self.E.add_genre()
                    elif key_a == '2':
                        self.E.add_book()
                    elif key_a == '3':
                        self.E.add_user()
                    else:
                        print("Chossed wrong.")
                    input("Press enter.")
            elif key =='2':
                while True:
                    key_s = self.search_menu()
                    if key_s == '0':
                        break
                    elif key_s == '1':
                        self.E.find_book_veiw()
                    elif key_s == '2':
                        self.E.find_user_veiw()
                    elif key_s == '3':
                        self.E.view_all()
                    else:
                        print("Chossed wrong.")
                    input("Press enter.")
            elif key == '3':
                while True:
                    key_d = self.delete_menu()
                    if key_d == '0':
                        break
                    elif key_d == '1':
                        self.E.remove_book()
                    elif key_d == '2':
                        self.E.remove_user()
                    else:
                        print("Chossed wrong.")
                    input("Press enter.")
            elif key == '4':
                while True:
                    key_c = self.checkout_menu()
                    if key_c == '0':
                        break
                    elif key_c == '1':
                        self.E.do_checkout()
                    elif key_c == '2':
                        self.E.return_checkout()
                    elif key_c == '3':
                        self.E.view_checkouts()
                    else:
                        print("Chossed wrong.")
                    input("Press enter.")
            else:
                print("Chossed wrong.")
            input("Press enter.")
        self.E.save()
    
    
        
    def load(self):
        print("===Load===")
        try:
            self.E.load_genres()
            self.E.load_books()
            self.E.load_useres()
            self.E.load_checkouts()
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