from pprint import pprint # better output experience
import os # working with files in Uni directory
# import customtkinter # GUI designing
from classes import *

def fetch():
    """when we run the programm, this is the first funcion ,that will automatically be invwoked in the main() function
    """
    # Uni.mother_dir: Uni -> class ; mother_dir is a class attribute
    # so we can have it throughout of our program
    libaries_List = os.listdir(Uni.mother_dir) # returns a list of csv file pathes(list[str])
    for library_name in libaries_List:
        l = library_name.split("-") # example) '1-zaban.csv' -> ['1', 'zaban.csv']
        id = l[0]
        name = l[1][:-4]
        library = Library(name, id) # with making library object we automatically make book objects
        Uni.libraries[name] = library # adding this objects to class method libraries(dict{'library_name': library_object}) of Uni class 

def make_window():
    win = Window()
    university = Uni()
    win.university = university
    win.mainloop()


def book_add(university):
    """adds the book to our database of the library object in Uni.libraries

    :param university: Uni object
    :type university: Uni
    """
    # gathering data
    lib_name = input("library's name: ")
    book_name = input("book's name: ")
    rel_date = input("book's release date: ")
    author = input("book's author: ")
    genre = input("book's genre: ")
    # searching for the library object
    lib = Uni.find_lib(lib_name)
    # making the the book object
    b = Book(lib_name, book_name, rel_date, author, genre)
    # pass the book object to the Library class method add_book()
    lib.add_book(b)



def book_del(university):
    """deletes the book's with the given name in a library

    :param university: Uni object
    :type university: Uni
    """
    lib_name = input("library's name: ")
    lib = Uni.find_lib(lib_name) # searching for the library object
    book_name = input("book's name: ")
    book = lib.find_book(book_name) # searching for the book object
    # pass the book to the Library's class method remove_book()
    lib.remove_book(book)
    


def book_edit(university):   
    """edits the information of the book in a library
    these information can be one of the below:
    book's name
    release date
    author
    genre

    :param university: Uni object
    :type university: Uni
    """
    lib_name = input("library's name: ")
    lib = Uni.find_lib(lib_name) # searches for library's object
    book_name = input("book's name: ")
    book = lib.find_book(book_name) # searches for book object
    book.book_info() # printing out book's information
    print("fill the detail that you want to change\n"
          "and skip the otherones")
    # the informaion that the user wants to change
    # the empty informations will not be edited
    new_name = input("new name: ")
    new_rel_date = input("new release date: ")
    new_author = input("new author: ")
    new_genre = input("new genre: ")
    lib.edit_book(book, new_name, new_rel_date, new_author, new_genre)



            

def book_info(university):
    """prints out the information of a book with given name

    :param university: Uni object
    :type university: Uni
    """
    book_name = input("book's name: ")
    for lib in Uni.libraries.values(): # for every library in database
        book = lib.find_book(book_name) # return the object of the book with given name [output: NoneType | book object]
        if book: # True if there is a book object and False if it's NoneType
            book.book_info()





def lib_add(university):
    """adds a library to our database(Uni.libraries)

    :param university: Uni object
    :type university: Uni
    """
    name = input("library's name: ")
    id = input("library's id: ")
    university.add_lib(Library(name, id))


def lib_del(university):
    """deletes a library object from databes(Uni.libraries)

    :param university: Uni object
    :type university: Uni
    """
    name = input("library's name: ")
    lib = university.libraries[name]
    university.remove_lib(lib)


def lib_info(university):
    """prints out the information of a library object with its name

    :param university: Uni object
    :type university: Uni
    """
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
    # request = Request()
    # while True:
    #     university.show_lib()
    #     inp = request.gathering()
    #     key, valid_inp = request.validation(inp)
    #     if valid_inp == 0:
    #         break
    #     if key:
    #         function_pending(university, valid_inp)
               

if __name__ == "__main__":
    main()