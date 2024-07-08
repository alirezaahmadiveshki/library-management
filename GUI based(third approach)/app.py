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


def main():
    """the main function: controlls program flow
    """
    fetch()
    make_window()

if __name__ == "__main__":
    main()