import customtkinter
from pprint import pprint

class Uni():
    Libraries = []


    def add_lib():
        ...


    def remove_lib():
        ...




class Library():
    def __init__(self, name, id, books) -> None:
        self.name = name
        self.id = id
        self.books = books


    def add_book():
        ...


    def remove_book():
        ...


    def edit_book():
        ...


    def lib_info(self):
        print("-" * 40)
        print(f"name: {self.name}\nid: {self.id}\nlist of the books: {self.books}")
        print("-" * 40)



class Book():
    def __init__(self, name, rel_date, author, genre) -> None:
        self.name = name
        self.rel_date = rel_date
        self.author = author
        self.genre = genre


    def book_info(self):
        print("-" * 40)
        print(f"name: {self.name}\nrelease date: {self.rel_date}\nauthor/writer: {self.author}\ngenre: {self.genre}")
        print("-" * 40)




def make_window():
    print("-" * 40)
    print("GUI is In the progress")
    print("-" * 40)


def requset_gathering():
        print("-" * 40)
        print("choose on of the below options :")
        print("BOOKS:")
        print("\t1 for ADD a book")
        print("\t2 for DELETING a book")
        print("\t3 for EDITING A BOOK")
        print("\t4 for book info")
        print("LIBRARIES:")
        print("\t5 for ADD a library")
        print("\t6 for DELETING a library")
        print("\t7 for library info")
        print("\t0 for the QUITING")
        inp = input("choose your request: ")
        return inp


def request_validation(inp):
    try:
        int_inp = int(inp)
        if 0 <= int_inp <= 7:
            return int_inp
        else:
            raise ValueError
    except:
        print("-" * 40)
        print("wrong input\nplease try again")
        print("-" * 40)
        inp = requset_gathering()
        return request_validation(inp)



def book_add():
   # library, name, rel_date, author, genre
    library = input("Library: ")
    name = input("Book's Name:")
    rel_date = input("Book's Release date: ")
    author = input("Book's Author/writer: ")
    genre = input("Books's genre:")
    b = Book(name, rel_date, author, genre)



def book_del():
    print("book_del")


def book_edit():
    print("book_edit")


def book_info():
    print("book_info")


def lib_add():
    print("lib_add")


def lib_del():
    print("lib_del")


def lib_info():
    print("lib_info")


def request_pending(inp):
    functions = [book_add, book_del, book_edit, book_info, lib_add, lib_del, lib_info]
    return functions[inp-1]()


def main():
    make_window()
    print("hello dear user :)")
    while True:
        inp = requset_gathering()
        int_inp = request_validation(inp)
        if int_inp == 0:
            break
        request_pending(int_inp)
        


if __name__ == "__main__":
    main()