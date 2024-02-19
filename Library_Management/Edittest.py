from unittest.mock import patch
import unittest
from Edit import Edit
from Book import Book
from User import User
from Checkout import Checkout

class CustomTests(unittest.TestCase):
    
    def setUp(self) -> None:
        book = Book(1,'title1',1,'auto','puby',1100) ##basic book
        user = User(1, 'Kim', 19970909, '0103444234', 'john5454@naver.com')
        checkout = Checkout(1, 'Kim', 1, 'title1')
        self.edit = Edit()
        self.edit.genres = ['poem']
        self.edit.books.append(book)
        self.edit.users.append(user)
        self.edit.checkouts.append(checkout)
    
    def test_addgenre(self):
        user_input = [
            'novel'
        ]
        with patch('builtins.input', side_effect = user_input):
            self.edit.add_genre()
        assert self.edit.genres == ['poem','novel']
    
    
    def test_addbook(self):
        user_input = [
            '1','2417','title1','auto','puby','1100'
        ]
        book = Book(2417,'title1',1,'auto','puby',1100)
        with patch('builtins.input', side_effect = user_input):
            self.edit.add_book()
        assert (self.edit.books[1].isbn == book.isbn and self.edit.books[1].price == book.price)
    
    def test_addbook_error(self): ## checking error for misstyping ispn,price
        user_input1 = [
            '1','misstype','2417','title1','auto','puby','1100'
        ] ## for not inputting numbers in ispn made an exception so 'misstype'will not be saved.
        user_input2 = [
            '1','2417','title1','auto','puby','misstype','1100'
        ]## for not inputting numbers in price made an exception so 'misstype'will not be saved.
        
        book = Book(2417,'title1',1,'auto','puby',1100)
        with patch('builtins.input', side_effect = user_input1):
            self.edit.add_book()
        assert (self.edit.books[1].isbn == book.isbn and self.edit.books[1].price == book.price)
        
        with patch('builtins.input', side_effect = user_input2):
            self.edit.add_book()
        assert (self.edit.books[1].isbn == book.isbn and self.edit.books[1].price == book.price)
    
    def test_addbook_overlap(self):
        user_input1 = [
            '1','1','ttitle1','aauto','ppuby','11300'
        ]
        user_input2 = [
            '1','2417','title1','auto','puby','misstype','1100'
        ]
        book = Book(2417,'title1',1,'auto','puby',1100)
        with patch('builtins.input', side_effect = user_input1):
            self.edit.add_book()
        with patch('builtins.input', side_effect = user_input2):
            self.edit.add_book()
        assert (self.edit.books[1].isbn == book.isbn and self.edit.books[1].price == book.price) ## because ispn in input1 already exist so input 1 will not be saved. 
        
    def test_adduser(self):
        user_input = [
            '1234', 'Toby', '20000216', '01023442234', 'toby44@naver.com'
        ]
        user = User(1234, 'Toby', 20000216, '01023442234', 'toby44@naver.com')
        with patch('builtins.input', side_effect = user_input):
            self.edit.add_user()
        assert (self.edit.users[1].id == user.id and self.edit.users[1].email == user.email)
        
    def test_adduser_error(self):## checking error for misstyping id
        user_input = [
           'misstype', '1234', 'Toby', '20000216', '01023442234', 'toby44@naver.com'
        ] ## misstype will not be saved.
        user = User(1234, 'Toby', 20000216, '01023442234', 'toby44@naver.com')
        with patch('builtins.input', side_effect = user_input):
            self.edit.add_user()
        assert (self.edit.users[1].id == user.id and self.edit.users[1].email == user.email)
    
    def test_adduser_overlap(self):
        user_input1 = [
            '1', 'Tooby', '20000216', '01023442234', 'tooby44@naver.com'
        ]
        user_input2 = [
            '1234', 'Toby', '20000216', '01023442234', 'toby44@naver.com'
        ]
        user = User(1234, 'Toby', 20000216, '01023442234', 'toby44@naver.com')
        with patch('builtins.input', side_effect = user_input1):
            self.edit.add_user()
        with patch('builtins.input', side_effect = user_input2):
            self.edit.add_user()
        assert (self.edit.users[1].id == user.id and self.edit.users[1].email == user.email)## because id in input1 already exist so input 1 will not be saved. 
        
    def test_addcheckout(self):
        user_input = [
            '1', '1'
        ]
        checkout = Checkout(1, 'Kim', 1, 'title1')
        with patch('builtins.input', side_effect = user_input):
            self.edit.do_checkout()
        assert(self.edit.checkouts[1].id == checkout.id and self.edit.checkouts[1].title == checkout.title)
    
    def test_addcheckout_error(self): ##check for the misstype error int id and isbn
        user_input1 = [
            'misstype','1', 'misstype','1'
        ]
        checkout = Checkout(1, 'Kim', 1, 'title1')
        
        user_input2 = [
            '123','1'
        ]
        
        user_input3 = [
            '1','1234'
        ]
        with patch('builtins.input', side_effect = user_input1):
            self.edit.do_checkout()
        assert(self.edit.checkouts[1].id == checkout.id and self.edit.checkouts[1].title == checkout.title)
        
        with patch('builtins.input', side_effect = user_input2):
            self.edit.do_checkout()
        assert len(self.edit.checkouts) == 2 ## user id 123 dose not exist so checkout dose not been made.
        
        with patch('builtins.input', side_effect = user_input3):
            self.edit.do_checkout()
        assert len(self.edit.checkouts) == 2 ## isbn 1234 dose not exist so checkout dose not been made.
        
if __name__ == '__main__':
    unittest.main