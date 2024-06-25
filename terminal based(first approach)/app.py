from pprint import pprint # better output experience
import os # working with files in Uni directory
# import customtkinter # GUI designing
from classes import *


def fetch():
    libaries_List = os.listdir(Uni.mother_dir)
    for library_name in libaries_List:
        l = library_name.split("-")
        id = l[0]
        name = l[1][:-4]
        library = Library(name, id)
        Uni.libraries[name] = library


def make_window():
    print("-" * 40)
    print("GUI is In the progress")
    print("-" * 40)


def book_add(university):
    lib_name = input("library's name: ")
    book_name = input("book's name: ")
    rel_date = input("book's release date: ")
    author = input("book's author: ")
    genre = input("book's genre: ")
    lib = Uni.find_lib(lib_name)
    b = Book(lib_name, book_name, rel_date, author, genre)
    lib.add_book(b)


def book_del(university):
    lib_name = input("library's name: ")
    lib = Uni.find_lib(lib_name)
    book_name = input("book's name: ")
    book = lib.find_book(book_name)
    lib.remove_book(book)
    


def book_edit(university):   
    lib_name = input("library's name: ")
    lib = Uni.find_lib(lib_name)
    lib.lib_info() 
    book_name = input("book's name: ")
    book = lib.find_book(book_name)
    book.book_info()
    print("fill the detail that you want to change\n"
          "and skip the otherones")
    new_name = input("new name: ")
    new_rel_date = input("new release date: ")
    new_author = input("new author: ")
    new_genre = input("new genre: ")
    lib.edit_book(book, new_name, new_rel_date, new_author, new_genre)



            

def book_info(university):
    book_name = input("book's name: ")
    for lib in Uni.libraries.values():
        book = lib.find_book(book_name)
        if book:
            book.book_info()





def lib_add(university):
    name = input("library's name: ")
    id = input("library's id: ")
    university.add_lib(Library(name, id))


def lib_del(university):
    name = input("library's name: ")
    lib = university.libraries[name]
    university.remove_lib(lib)


def lib_info(university):
    lib_name = input("library's name: ")
    lib_name = lib_name.lower()
    lib = Uni.find_lib(lib_name)
    lib.lib_info()


def function_pending(university, inp):
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
    request = Request()
    while True:
        university.show_lib()
        inp = request.gathering()
        key, valid_inp = request.validation(inp)
        if valid_inp == 0:
            break
        if key:
            function_pending(university, valid_inp)
               

if __name__ == "__main__":
    main()