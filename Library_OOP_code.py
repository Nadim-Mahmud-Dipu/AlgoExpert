
# Abstraction and Encapsulation
class Library:
    def __init__(self, listOfBooks):
        self.availableBooks = listOfBooks

    def displayAvailablebooks(self):
        for book in self.availableBooks:
            print(book)

    def lendBook(self, requestedBook):
        if requestedBook in self.availableBooks:
            print("You've now borrowed the book.")
            self.availableBooks.remove(requestedBook)
        else:
            print("Sorry, the book is not available in our list.")

    def addBook(self, returnedBook):
        self.availableBooks.append(returnedBook)
        print("You've returned the book. Thank you!")


class Customer:
    def requestBook(self):
        print("Enter the name of the book that you would like to borrow: ")
        self.book = input()
        return self.book

    def returnBook(self):
        print("Please enter the name of the book you're returning: ")
        self.book = input()
        return self.book


library = Library(["Think and Grow Rich", "Who Will Cry When You Die", "For One More Day"])
customer = Customer()
print("Enter 1 to display the available books")
print("Enter 2 to request for a book")
print("Enter 3 to return a book")
print("Enter 4 to exit")

while True:

    userChoice = int(input())

    if userChoice == 1:
        library.displayAvailablebooks()
    elif userChoice == 2:
        requestedBook = customer.requestBook()
        library.lendBook(requestedBook)
    elif userChoice == 3:
        returnBook = customer.returnBook()
        library.addBook(returnBook)
    elif userChoice == 4:
        quit()
