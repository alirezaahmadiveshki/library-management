from pprint import pprint # better output experience
import os # working with files in Uni directory
# import customtkinter # GUI designing
from classes import *

def fetch_add_book(lib_name, book_list):
    """this function turn book-list to book objects and add them to the library with <lib-name>

    :param lib_name: the library file path that the book-list is from   
    :type lib_name: String
    :param book_list: list of the lines of the library files in uni directory
    :type book_list: List[str]
    """
    book_objects = []
    for book in book_list:
        if book.strip():
            book = book.split()
            b = Book(book[0], book[1], book[2], book[3])
            book_objects.append(b)
    
    lib_name_list = lib_name.split("-")
    id = lib_name_list[0]
    name = lib_name_list[1][:-4]
    lib = Library(name, id, book_objects)
    Uni.libraries[lib.name] = lib
    

def fetch():
    """fetching and reading data from librariy files located in the Uni directory
    """
    def library_file_path():
        """opens library files then make a book-list of them and pass them to fetch_add_book function
        """
        mother_dir = R"C:\Users\PSK\Documents\GitHub\library-management\library-management\Uni"
        libaries_List = os.listdir(mother_dir)
        for library_name in libaries_List:
            library_path = f"{mother_dir}/{library_name}"
            with open(library_path, "r") as library_file:
                book_list = library_file.readlines()
                fetch_add_book(library_name, book_list)
    library_file_path()


def make_window():
    print("-" * 40)
    print("GUI is In the progress")
    print("-" * 40)


def requset_gathering(university):
    """prints out the user interface in the termainal

    :return: inp: input that is gathered    
    :rtype: String
    """
    university.show_lib()
    print("-" * 40)
    print("choose on of the below options :")
    print("BOOKS:")
    print("\t1 for ADD a book")
    print("\t2 for DELETING a book")
    print("\t3 for EDITING A BOOK")
    print("\t4 for book info")
    print("libraries:")
    print("\t5 for ADD a library")
    print("\t6 for DELETING a library")
    print("\t7 for library info")
    print("\t0 for the QUITING")
    inp = input("choose your request: ")
    return inp


def request_validation(inp):
    """controls that if the user input is validated or not

    :param inp: the input of this function is the output of the request_gathering function
    :type inp: String
    :raises ValueError: if the inp wasn't an integer between 0 to 7
    :return: the exact function with diffrent input that we have in the except block
    :rtype: Funcion
    """
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
        inp = requset_gathering(university)
        return request_validation(inp)


def book_add(university):
    # library, name, rel_date, author, genre
    while True:
        library = input("Library: ")
        name = input("Book's Name: ")
        rel_date = input("Book's Release date: ")
        author = input("Book's Author/writer: ")
        genre = input("Books's genre: ")
        b = Book(name, rel_date, author, genre)
        if library in university.libraries.keys():
            lib = university.libraries[library]
            lib.add_book(b)
            break
        else:
            print("wrong library name, try again")


def book_del(university):
    while True:
        library = input("Library: ")
        name = input("Book's Name: ")
        if library in university.libraries.keys():
            lib = university.libraries[library]
            for b in lib.books:
                if b.name == name:
                    lib.remove_book(b)
                    break
            break
        else:
            print("wrong library name, try again")    


# def changing_book_info(lib, book):
#     print("which title do you want to edit?")
#     print("1 for name\n2 for release data\n3 for author\n4 for genre")
#     opt = input("option: ").lower()
#     if opt == "1":
#         new_name = input("enter the new name: ")
#         lib.edit_book(book, new_name , book.rel_date, book.author, book.genre)
#     elif opt == "2":
#         new_release_date = input("enter the new release date: ")
#         lib.edit_book(book, book.name , new_release_date, book.author, book.genre)
#     elif opt == "3":
#         new_author = input("enter the new author: ")
#         lib.edit_book(book, book.name , book.rel_date, new_author, book.genre)
#     elif opt == "4":
#         new_genre = input("enter the new genre: ")
#         lib.edit_book(book, book.name , book.rel_date, book.author, new_genre)
#     else:
#         print("wrong option please try again")


def book_edit(university):   
    print("*"*40) 
    print("this command is under process")
    print("*"*40) 
    # libs = university.libraries.values()
    # book_name = input("Book's name: ")
    # for lib in libs:
    #     lib_books = lib.books
    #     for book in lib_books:
    #         if book.name == book_name:
    #             changing_book_info(lib, book)
    #             break
    #         print("*" * 40)
    #         print("there's not a book with this name")
    #         opt = input("enter r for resuming and q for quiting: ").lower()
    #         if opt == "r":
    #             book_edit(university)
    #         elif opt == "q":
    #             return
    #         else:
    #             print("wrong input, try again")    
    #         print("*" * 40)
    #     break

            

def book_info(university):
    """print out the book's information with the name of the book

    :param university: the university object
    :type university: Uni
    """
    inp_name = input("book's name: ")
    a = False
    for lib in university.libraries.values():
        for book in lib.books:
            if book.name == inp_name.lower():
                print("*"* 40)
                print(lib.name)
                print("*"* 40)
                book.book_info()
                a = True
    if a == False:
        print("-" * 40)
        print("this book doesn't exist")
        print("-" * 40)


def lib_add(university):
    print("*" * 40)
    print("*" * 40)
    print("fill the follow informations")
    name = input("library's name: ")
    id = input("library's id: ")
    lib = Library(name, id)
    university.add_lib(lib)


def lib_del(university):
    try:
        lib_name = input("library name: ")
        lib = university.libraries[lib_name]
        university.remove_lib(lib)
    except KeyError:
        print("wrong library name, try again")


def lib_info(university):
    """prints out the library information

    :param university: university object
    :type university: Uni
    """
    lib_name = input("Library's name: ")
    lib_object = university.libraries[lib_name]
    lib_object.lib_info()


def request_pending(inp, university):
    """the function links the user input to a function

    :param inp: the user input
    :type inp: Integer(from 1 - 7)
    :param university: the university object 
    :type university: Uni
    :return: the function that the user has requested
    :rtype: Function
    """
    functions = [book_add, book_del, book_edit, book_info, lib_add, lib_del, lib_info]
    return functions[inp-1](university)


def main():
    """the main function: controlls program flow
    """
    university = Uni()
    fetch()
    make_window()
    print("hello dear user :)")
    while True:
        inp = requset_gathering(university)
        int_inp = request_validation(inp)
        if int_inp == 0:
            break
        request_pending(int_inp, university)
        

if __name__ == "__main__":
    main()