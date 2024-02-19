from Book import Book
from common import input_int
from common import tryinput_int
from User import User
from Checkout import Checkout


class Edit:
    def __init__(self):
        self.genres= list()
        self.users = list()
        self.books = list()
        self.users = list()
        self.checkouts= list()
        

    def load_genres(self):
        fs = open("genres.csv", "r")
        datas = fs.read()
        # datas:["peom\non-novel\nnovel\n"]
        ds_gs = datas.split("\n")  # divid them by \n
        # dg_gs:["peom","non-novel","novel",""]
        fs.close()
        ds_gs.pop()  # Delete the last argument
        # ds_gs:["peom","non-novel","novel"]
        self.genres.extend(ds_gs)

    def load_books(self):
        fs = open("Library_Management/books.csv", "r")
        while True:
            book = Book.load_book(fs)
            if book == None:
                break
            self.books.append(book)
        fs.close()
        
    def load_useres(self):
        fs = open("Library_Management/users.csv", "r")
        while True:
            user = User.load_user(fs)
            if user == None:
                break
            self.users.append(user)
        fs.close()

    def load_checkouts(self):
        fs = open("Library_Management/checkouts.csv", "r")
        while True:
            checkout = Checkout.load_checkout(fs)
            if checkout == None:
                break
            self.checkouts.append(checkout)
        fs.close()
    
    def save(self):
        print("===Save===")
        self.save_genres()
        self.save_books()
        self.save_users()
        self.save_checkouts()

    def save_genres(self):
        fs = open("Library_Management/genres.csv", "w")
        for genre in self.genres:
            fs.write(genre + "\n")
        fs.close()

    def save_books(self):
        fs = open("Library_Management/books.csv", "w")
        for book in self.books:
            book.write(fs)
        fs.close()
    
    def save_users(self):
        fs = open("Library_Management/users.csv", "w")
        for uesr in self.users:
            uesr.write(fs)
        fs.close()
        
    def save_checkouts(self):
        fs = open("Library_Management/checkouts.csv", "w")
        for checkout in self.checkouts:
            if checkout == None:
                continue
            checkout.write(fs)
        fs.close()

    def add_genre(self):
        print("===Add Genre===")
        self.view_genres()
        genre = input("Name fo the Genre:")
        self.genres.append(genre)

    def add_book(self):
        print("===Add Book===")
        gn = self.select_genre()  # choose genre
        if gn == 0:  # when choosed wrong
            print("You choosed wrong")
            return
        while True:
            try :
                isbn = int(input("ISBN:"))  # input ISBN
                break
            except ValueError:
                print("please input number")
        sbook = self.find_book(isbn)  # search with ISBN
        if sbook != None:  # If it exists
            print("The ISBN Already exists.")
            return
        book = self.make_book(isbn, gn)  # Create a book object.
        self.books.append(book)  # add to books

    def add_user(self): #almost same as add_book
        print("===Add User===")
        while True:
            try :
                id = int(input("ID:"))   
                break
            except ValueError:
                print("please input number")

        suser = self.find_user(id)  
        if suser != None:  
            print("The ID Already exists.")
            return
        user = self.make_user(id)  
        self.users.append(user)  
        
    def do_checkout(self):
        print("===Checkout===")
        while True:
            try :
                id = int(input("ID:"))   
                break
            except ValueError:
                print("please input number")
                
        while True:
            try :
                isbn = int(input("ISBN:"))  
                break
            except ValueError:
                print("please input number")
        checkout = self.make_checkout(id, isbn)
        if checkout == None:
            return
        self.checkouts.append(checkout)

    def select_genre(self):
        self.view_genres()
        gn = input_int("Number of the genre:")
        if gn > 0 and gn <= len(self.genres):
            return gn
        return 0


    def make_book(self, isbn, gn):
        title = input("Tile:")
        author = input("Author:")
        publisher = input("Publisher:")
        while True:
            try :
                price = int(input("Price:"))
                break
            except ValueError:
                print("input number")
        return Book(isbn, title, gn, author, publisher, price)
    
    def make_user(self, id):
        name = input("Name:")
        birth_d = input("Birth date:")
        phone_n = input("Phone number:")
        email = input("Email:")
        ban = False
        return User(id, name, birth_d, phone_n, email, ban)

    def make_checkout(self, id, isbn):
        user = self.find_user(id)
        if user == None:
            print("The user doesn't exist")
            return
        name = user.name
        book = self.find_book(isbn)
        if book == None:
            print("The book doesn't exist")
            return
        title = book.title
        return Checkout(id, name, isbn, title)
        

    def remove_book(self):
        print("===Remove Book===")
        isbn = input("isbn:")
        book = self.find_book(isbn)
        if book == None:
            print("The book doesn't exist")
            return
        self.books.remove(book)
        del book  #remove from the memory
        print("Removed")
        
    def remove_user(self):
        print("===Remove User===")
        id = input("id:")
        user = self.find_user(id)
        if user == None:
            print("The user doesn't exist")
            return
        self.users.remove(user)
        del user  
        print("Removed")    
        
        
    def return_checkout(self):
        print("===Retrun Book===")
        id = int(input("id:"))
        isbn = int(input("isbn :"))
        checkout = self.find_checkout(id, isbn)
        if checkout == None:
            print("The user or the isbn doesn't exist")
            return
        
        self.checkouts.remove(checkout)
        del checkout  
        print("Removed") 

    def find_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None
    
    def find_user(self, id):
        for user in self.users:
            if user.id == id:
                return user
        return None
    
    
    def find_checkout(self, id, isbn):
        for checkout in self.checkouts:
            if checkout.id == id:
                if checkout.isbn == isbn:
                    return checkout
        return None

    def find_book_veiw(self):
        print("===Book Find===")
        isbn = input("isbn:")
        book = self.find_book(isbn)
        if book == None:
            print("The book doesn't exist.")
            return
        self.view_book(book)

    def find_user_veiw(self):
        print("===User Find===")
        id = input("id:")
        user = self.find_user(id)
        if user == None:
            print("The user doesn't exist.")
            return
        self.view_user(user)


    def view_all(self):
        print("===View all===")
        self.view_genres()
        self.view_books()
        self.view_users()


    def view_books(self):
        print("=== {0} Books".format(len(self.books)))
        for book in self.books:
            self.view_book(book)
            
    def view_users(self):
        print("=== {0} Users ".format(len(self.users)))
        for user in self.users:
            self.view_user(user)

    def view_genres(self):
        sz = len(self.genres)
        for i in range(0, sz):
            print("{0}:{1}".format(i + 1, self.genres[i]), end="  ")
        print()
        
    def view_checkouts(self):
        print("=== {0} Checkouts ".format(len(self.checkouts)))
        for checkout in self.checkouts:
            self.view_checkout(checkout)

    def view_book(self, book):
        print("{0}:{1}".format(book.isbn, book.title))
        print("\tGenre: ", book.gn)
        print("\tAutor:", book.author)
        print("\tPublisher:", book.publisher)
        print("\tPrice:", book.price)
        
    def view_user(self, user):
        print("{0}:{1}".format(user.id, user.name))
        print("\tBirth date:", user.birth_d)
        print("\tPhone number:", user.phone_n)
        print("\tEmail:", user.email)
        print("\tRentable:", user.ban)
        
    def view_checkout(self, checkout):
        print("{0}:{1}".format(checkout.id, checkout.isbn))
        print("\tName: ", checkout.name)
        print("\tTitle:", checkout.title)
       
