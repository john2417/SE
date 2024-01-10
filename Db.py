import io
from Book import book

class db:
    def __init__(self, fileName):
        self.fileName = fileName

    def read(self):
        file = io.open(self.fileName, 'r', encoding='utf8')
        lines = file.readlines()

        booklist = []
        for line in lines:
            tokens = line.split(',')
            title = tokens[0].strip()
            author = tokens[1].strip()

            if title != '' and author != '':
                booklist.append(book(title, author))

        return booklist

    def save(self, booklist):
        strArr = []
        for book in booklist:
            strArr.append(book.toString())

        file = io.open(self.fileName, 'W+', encoding='utf8')
        file.writelines(strArr)
