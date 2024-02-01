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
        
    def Run(self):
        self.Load()
        while True:
            key = self.SelectMenu()
            if key == '0':
                break
            elif key ==  '1':
                Edit.AddGenre(self.E)
            elif key =='2':
                Edit.AddBook(self.E)
            elif key == '3':
                Edit.RemoveBook(self.E)
            elif key == '4':
                Edit.FindBook_veiw(self.E)
            elif key =='5':
                Edit.ViewAll(self.E)
            else:
                print("잘못 선택하였습니다.")
            input("엔터 키를 누르세요.")
        Edit.Save(self.E)
        
    def Load(self):
        print("===Load===")
    try:
        Edit.LoadGenres()
        Edit.LoadBooks()
    except:
        print("환영합니다. 즐~")
    input("엔터 키를 누르세요.")
    
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