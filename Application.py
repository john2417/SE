import os
from Book import Book
from common import input_int
from common import tryinput_int
class Application:
    def __init__(self):
        self.genres= list()
        self.books = list()
    def Run(self):
        self.Load()
        while True:
            key = self.SelectMenu()
            if key == '0':
                break
            elif key ==  '1':
                self.AddGenre()
            elif key =='2':
                self.AddBook()
            elif key == '3':
                self.RemoveBook()
            elif key == '4':
                self.FindBook()
            elif key =='5':
                self.ViewAll()
            else:
                print("잘못 선택하였습니다.")
            input("엔터 키를 누르세요.")
        self.Save()
    def Load(self):
        print("===Load===")
        try:
            self.LoadGenres()
            self.LoadBooks()
        except:
            print("환영합니다. 즐~")
        input("엔터 키를 누르세요.")
    def LoadGenres(self):
        fs = open("genres.csv","r")
        datas = fs.read()
        #datas:["시\n수필\n소설\n"]
        ds_gs = datas.split("\n")#개행 문자를 기준으로 분리
        #dg_gs:["시","수필","소설",""]
        fs.close()
        ds_gs.pop()#맨 마지막 원소 삭제
        #ds_gs:["시","수필","소설"]
        self.genres.extend(ds_gs)
    def LoadBooks(self):
        fs = open("books.csv","r")
        while True:
            book = Book.LoadBook(fs)
            if book == None:
                break
            self.books.append(book)
        fs.close()
    def Save(self):
        print("===Save===")
        self.SaveGenres()
        self.SaveBooks()
    def SaveGenres(self):
        fs = open("genres.csv","w")
        for genre in self.genres:
            fs.write(genre+"\n")
        fs.close()
    def SaveBooks(self):
        fs = open("books.csv","w")
        for book in self.books:
            book.Write(fs)
        fs.close()
    def SelectMenu(self):
        os.system("cls")
        print("==  도서 관리 프로그램 ==")
        print("1:Add Genre")
        print("2:Add Book")
        print("3:Delete Book")
        print("4:Search Book")
        print("5:View Everything")
        print("0: Exit program")
        return input("\n메뉴 입력 ◀:")
    def AddGenre(self):
        print("===장르 추가===")
        self.ViewGenres()
        genre = input("추가할 장르 명:")
        self.genres.append(genre)
    def ViewGenres(self):
        sz = len(self.genres)
        for i in range(0,sz):
            print("{0}:{1}".format(i+1, self.genres[i]),end='  ')
        print()
    def AddBook(self):
        print("===도서 추가===")
        gn = self.SelectGenre()#장르를 선택한다.
        if gn == 0:#잘못 선택하였을 때
            print("잘못 선택하였습니다.")
            return
        isbn = input("ISBN:")#ISBN을 입력받는다.
        sbook = self.Find(isbn)#ISBN으로 도서를 검색한다.
        if sbook != None:#검색한 도서가 존재하면
            print("이미 존재하는 ISBN입니다.")
            return
        book = self.MakeBook(isbn,gn)#도서 개체를 만든다.
        self.books.append(book)#도서 컬렉션에 추가한다.
    def SelectGenre(self):
        self.ViewGenres()
        gn = input_int("선택할 장르 번호:")
        if gn>0 and gn<=len(self.genres):
            return gn
        return 0
    def Find(self,isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None
    def MakeBook(self,isbn,gn):
        title = input("제목:")
        author = input("저자:")
        publisher = input("출판사:")
        price = input_int("가격:")
        return Book(isbn,title,gn,author,publisher,price)
    def RemoveBook(self):
        print("===도서 삭제===")
        isbn = input("isbn:")
        book =self.Find(isbn)
        if book == None:
            print("존재하지 않는 도서입니다.")
            return
        self.books.remove(book)
        del book #메모리에서 제거
        print("삭제하였습니다.")
    def FindBook(self):
        print("===도서 검색===")
        isbn = input("isbn:")
        book =self.Find(isbn)
        if book == None:
            print("존재하지 않는 도서입니다.")
            return
        self.ViewBook(book)
    def ViewAll(self):
        print("===전체 보기===")
        self.ViewGenres()
        self.ViewBooks()
    def ViewBooks(self):
        print("===도서 목록:{0}권".format(len(self.books)))
        for book in self.books:
            self.ViewBook(book)
    def ViewBook(self,book):
        print("{0}:{1}".format(book.isbn,book.title))
        print("\t장르 번호:",book.gn)
        print("\t저자:",book.author)
        print("\t출판사:",book.publisher)
        print("\t가격:",book.price)