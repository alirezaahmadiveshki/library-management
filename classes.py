import os
from pprint import pprint


class Uni():
    """the university object
    in the first line of the main function we made an object of this class called university
    and with this object we control the library objects
    """

    libraries = {} # a dict that include {"library-name": library-object}
    mother_dir = R"C:\Users\PSK\Documents\GitHub\library-management\library-management\Uni"
    # addres of the Uni directory
    # because we make an Uni object in the first line of the main function
    # so we are sure that we can acsses to this addres throughout our code


    @staticmethod
    def find_lib(name):
        for lib_name, lib in Uni.libraries.items():
            if name.lower() == lib_name.lower():
                return lib


    def add_lib(self, lib: "Library") -> None:
        """this method is doing:
        1 - adding a library to libraries attribute of the university object
        2 - adding a file to the Uni directory with <id-name.txt> format; where name and id are library's

        :param lib: a library object that we're adding
        :type lib: Library
        """
        Uni.libraries[lib.name] = lib
        lib.file.write()



    def remove_lib(self, lib: "Library") -> None:
        """this method is doing:
        1 - removing a function from libraries attribute of the university object
        2 - deleting file with <id-name.text> format; where name and id are library's

        :param lib: a library object
        :type lib: Library
        """
        del self.libraries[lib.name]
        lib.file.remove_file()
        


    def show_lib(self):
        print("*"*40)
        print("\tlibraries: ")
        for lib in self.libraries.keys():
            print(lib)    
        print("*"*40)




class Library():
    def __init__(self, name: str, id: int) -> None:
        self.name = name
        self.id = id
        self.books = []
        self.path = fR"{Uni.mother_dir}/{self.id}-{self.name}.txt"
        self.file = File(f"{self.id}-{self.name}.txt")
        self.file.remove_spaces()
        for line in self.file.lines:
            char_list = line.strip().split(" ")
            b = Book(self.name, char_list[0], char_list[1], char_list[2], char_list[3])
            self.books.append(b)


    def add_book(self, book: "Book") -> None:
        """this method is doing:
        1 - adds the input book to the book sattribute of hte library object
        2 - adds the information of the book to the library file with <id-name.txt> name  

        :param book: an book object that we wawnt to add
        :type book: Book
        """
        self.books.append(book)
        self.lib_info()
        self.file.create_line(book)


    def remove_book(self, book: "Book") -> None:
        """removing a book object:
        from the list: library's books attribute
        from the library's file
        """
        self.books.remove(book) # removes the book from the books attribute of the library objects
        self.lib_info()
        self.file.remove_line(book.name)
        self.file.remove_spaces()

            

    def edit_book(self, book, new_name = "", new_rel_date = "", new_author = "", new_genre = ""):
        if new_name == "":
            new_name = book.name
        if new_rel_date == "":
            new_rel_date = book.rel_date
        if new_author == "":
            new_author = book.author
        if new_genre == "":
            new_genre = book.genre

        self.remove_book(book)
        edited_book = Book(self.name, new_name, new_rel_date, new_author, new_genre)            
        self.add_book(edited_book)


    def find_book(self, book_name):
        for book in self.books:
            if book.name.lower() == book_name.lower():
                return book


    def lib_info(self) -> None:
        """prints out the library information by it's name
        """
        print("-" * 40)
        print(f"name: {self.name}\nid: {self.id}\n\tlist of the books:")
        for book in self.books:
            book.book_info()
        print("-" * 40)




class Book():
    def __init__(self, library, name, rel_date, author, genre) -> None:
        self.name = name.lower()
        self.rel_date = rel_date
        self.author = author.lower()
        self.genre = genre.lower()
        self.library = library.lower()



    def book_info(self):
        """prints out the object book's information
        """
        print("-" * 40)
        print(f"library: {self.library}\nname: {self.name}\nrelease date: {self.rel_date}\nauthor/writer: {self.author}\ngenre: {self.genre}")
        print("-" * 40)




class File():
    mother_dir = R"C:\Users\PSK\Documents\GitHub\library-management\library-management\Uni"
    def __init__(self, name) -> None:
        self.name = name
        self.path = fR"{File.mother_dir}\{self.name}"
        self.amount = 0
        self.lines = []
        f = open(self.path, 'a') #creates the file if it's not created
        f.close()
        with open(self.path, 'r') as file:
            for line in file:
                self.amount += 1
                self.lines.append(line)
        self.remove_spaces()


    def show(self):
        print(f"name: {self.name}\npath: {self.path}\namount: {self.amount}\n lines: {self.lines}")


    def remove_spaces(self):
        with open(self.path, 'r') as file:
            self.lines = []
            for line in file: 
                if line != '\n':
                    self.lines.append(line)
        self.write()      


    def remove_line(self, book_name):
        for line in self.lines:
            name = line.split(" ")[0]
            if name.startswith('\n'):
                name = name.strip()
            if (name.lower() == book_name.lower()):
                self.lines.remove(line)
                self.write()
                break
        self.remove_spaces()


    def write(self):
        with open(self.path, "w") as file:
            file.writelines(self.lines)       


    def create_line(self, book):
        self.lines.append(f"\n{book.name} {book.rel_date} {book.author} {book.genre}")
        self.write()
        self.remove_spaces()



    def remove_file(self):
        os.remove(self.path)
        


class Request():

    def gathering(self):
        """prints out the user interface in the termainal

        :return: inp: input that is gathered    
        :rtype: String
        """
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
    

    def validation(self, inp):
        """controls that if the user input is validated or not

        :param inp: the input of this function is the output of the request_gathering function
        :type inp: String
        :raises ValueError: if the inp wasn't an integer between 0 to 7
        :return: the exact function with diffrent input that we have in the except block
        :rtype: Funcion
        """
        key = False
        try:
            int_inp = int(inp)
            if 0 <= int_inp <= 7:
                key = True
                return (key, int_inp)
            else:
                raise ValueError
        except Exception:
            print("-" * 40)
            print("wrong input\nplease try again")
            print("-" * 40)
            return key, inp