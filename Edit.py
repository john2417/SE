import os
from Book import Book
from common import input_int
from common import tryinput_int
from User import User


class Edit:
    def __init__(self):
        self.genres= list()
        self.books = list()
        self.users = list()
        

    def LoadGenres(self):
        fs = open("genres.csv", "r")
        datas = fs.read()
        # datas:["시\n수필\n소설\n"]
        ds_gs = datas.split("\n")  # 개행 문자를 기준으로 분리
        # dg_gs:["시","수필","소설",""]
        fs.close()
        ds_gs.pop()  # 맨 마지막 원소 삭제
        # ds_gs:["시","수필","소설"]
        self.genres.extend(ds_gs)

    def LoadBooks(self):
        fs = open("books.csv", "r")
        while True:
            book = Book.LoadBook(fs)
            if book == None:
                break
            self.books.append(book)
        fs.close()
        
    def LoadUsers(self):
        fs = open("users.csv", "r")
        while True:
            user = User.LoadUser(fs)
            if user == None:
                break
            self.users.append(user)
        fs.close()

    def Save(self):
        print("===Save===")
        self.SaveGenres(self)
        self.SaveBooks(self)

    def SaveGenres(self):
        fs = open("genres.csv", "w")
        for genre in self.genres:
            fs.write(genre + "\n")
        fs.close()

    def SaveBooks(self):
        fs = open("books.csv", "w")
        for book in self.books:
            book.Write(fs)
        fs.close()
    
    def SaveUsers(self):
        fs = open("users.csv", "w")
        for uesr in self.users:
            uesr.Write(fs)
        fs.close()

    def AddGenre(self):
        print("===Add Genre===")
        self.ViewGenres(self)
        genre = input("Name fo the Genre:")
        self.genres.append(genre)



    def AddBook(self):
        print("===Add Book===")
        gn = self.SelectGenre()  # 장르를 선택한다.
        if gn == 0:  # 잘못 선택하였을 때
            print("You choosed wrong")
            return
        isbn = input("ISBN:")  # ISBN을 입력받는다.
        sbook = self.Findbook(isbn)  # ISBN으로 도서를 검색한다.
        if sbook != None:  # 검색한 도서가 존재하면
            print("The ISBN Already exists.")
            return
        book = self.MakeBook(isbn, gn)  # 도서 개체를 만든다.
        self.books.append(book)  # 도서 컬렉션에 추가한다.

    def AddUser(self):
        print("===Add User===")
        id = input("ID:")  # ISBN을 입력받는다.
        suser = self.Finduser(id)  # ISBN으로 도서를 검색한다.
        if suser != None:  # 검색한 도서가 존재하면
            print("The ID Already exists.")
            return
        User = self.MakeUser(id)  # 도서 개체를 만든다.
        self.users.append(User)  # 도서 컬렉션에 추가한다.

    def SelectGenre(self):
        self.ViewGenres()
        gn = input_int("Number of the genre:")
        if gn > 0 and gn <= len(self.genres):
            return gn
        return 0


    def MakeBook(self, isbn, gn):
        title = input("Tile:")
        author = input("Author:")
        publisher = input("Publisher:")
        price = input_int("Price:")
        return Book(isbn, title, gn, author, publisher, price)
    
    def MakeUser(self, id):
        name = input("Name:")
        birth_d = input("Birth date:")
        phone_n = input("Phone number:")
        email = input_int("Email:")
        ban = False
        return User(id, name, birth_d, phone_n, email, ban)


    def RemoveBook(self):
        print("===Remove Book===")
        isbn = input("isbn:")
        book = self.Findbook(isbn)
        if book == None:
            print("The book doesn't exist")
            return
        self.books.remove(book)
        del book  # 메모리에서 제거
        print("Removed")
        
    def RemoveUser(self):
        print("===Remove User===")
        id = input("id:")
        user = self.Finduser(id)
        if user == None:
            print("The user doesn't exist")
            return
        self.users.remove(user)
        del user  # 메모리에서 제거
        print("Removed")    

    def Findbook(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None
    
    def Finduser(self, id):
        for user in self.users:
            if user.id == id:
                return user
        return None

    def FindBook_veiw(self):
        print("===Book Find===")
        isbn = input("isbn:")
        book = self.Find(isbn)
        if book == None:
            print("The book doesn't exist.")
            return
        self.ViewBook(book)

    def FindUser_veiw(self):
        print("===User Find===")
        isbn = input("id:")
        book = self.Find(isbn)
        if book == None:
            print("The user doesn't exist.")
            return
        self.ViewUser(book)


    def ViewAll(self):
        print("===View all===")
        self.ViewGenres(self)
        self.ViewBooks(self)


    def ViewBooks(self):
        print("===도서 목록:{0}권".format(len(self.books)))
        for book in self.books:
            self.ViewBook(book)
            
    def ViewGenres(self):
        sz = len(self.genres)
        for i in range(0, sz):
            print("{0}:{1}".format(i + 1, self.genres[i]), end="  ")
        print()

    def ViewBook(self, book):
        print("{0}:{1}".format(book.isbn, book.title))
        print("\t장르 번호:", book.gn)
        print("\t저자:", book.author)
        print("\t출판사:", book.publisher)
        print("\t가격:", book.price)
        
    def ViewUser(self, book):
        print("{0}:{1}".format(book.isbn, book.title))
        print("\t장르 번호:", book.gn)
        print("\t저자:", book.author)
        print("\t출판사:", book.publisher)
        print("\t가격:", book.price)
