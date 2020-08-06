class Library:
    def __init__(self, list, name):
        self.bookList = list
        self.name = name
        self.landingDict = {}

    def display_book(self):
        print( f"we have following books{self.name}" )
        for book in self.bookList:
            print( book )

    def lendBook(self, user, book):
        if book not in self.landingDict.keys():
            self.landingDict.update( {book: user} )
            print( "book is Updated" )
        else:
            print( {self.landingDict[book]} )

    def addBook(self, book):
        self.bookList.append( book )
        print( "book added" )

    def returnBook(self, book):
        self.landingDict.pop( book )
        print( "book removed" )


if __name__ == '__main__':
    l1 = Library( ["python", "java", ".net", "c++", "c"], "codeWithBook" )
    while (True):
        print( f"welcome to {l1.name} world" )
        print( "1.DisplayBook" )
        print( "2.LendBook" )
        print( "3.AddBook" )
        print( "4.ReutrnBook" )
        user_choice = input()
        if user_choice not in ['1', '2', '3', '4']:
            print( "Enter a valid option:" )
            continue
        else:
            user_choice = int( user_choice )
        if user_choice == 1:
            l1.display_book()
        elif user_choice == 2:
            book = input( "which book you ewant to lend:" )
            user = input( "Enter your Name:" )
            l1.lendBook( book, user )
        elif user_choice == 3:
            book1 = input( "Enter the book name Which you want to add:" )
            l1.addBook( book1 )
        elif user_choice == 4:
            book2 = input( "Enter the book name which you want to return:" )
            l1.returnBook( book2 )
        else:
            print( "not a valid option" )
        print( "press q or c" )
        user_choice1 = ""
        while (user_choice1 != "q" and user_choice1 != "c"):
            user_choice1 = input()
            if user_choice1 == "q":
                exit()
            elif user_choice1 == "c":
                continue
