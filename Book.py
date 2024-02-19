class Book:
    def __init__(self,isbn,title,gn,author,publisher,price):
        self.isbn = isbn
        self.title = title
        self.gn = gn
        self.author = author
        self.publisher = publisher
        self.price = price
        
    def write(self,fs):
        fs.write(str(self.isbn)+",")
        fs.write(self.title+",")
        fs.write(str(self.gn)+",")
        fs.write(self.author+",")
        fs.write(self.publisher+",")
        fs.write(str(self.price)+"\n")
        
    @staticmethod
    def load_book(fs):
        data = fs.readline()
        elems = data.split(",")
        if len(elems)<6:
            return None
        isbn = int(elems[0])
        title = elems[1]
        gn = int(elems[2])
        author = elems[3]
        publisher = elems[4]
        price = int(elems[5][:-1])
        return Book(isbn,title,gn,author,publisher,price)