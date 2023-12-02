class book (object):
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def greeting(self):
        print("Book name : " + self.title)
        print("Author : " + self.author)