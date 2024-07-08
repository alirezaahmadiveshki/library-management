import pandas as pd
import os

class Uni():
    """the university object
    in the first line of the main function we made an object of this class called university
    and with this object we control the library objects
    """

    libraries = {} # a dict that include {"library-name": library-object}
    mother_dir = R"Uni\csv files"
    # addres of the Uni directory
    # because we make an Uni object in the first line of the main function
    # so we are sure that we can acsses to this addres throughout our code


    @staticmethod
    def find_lib(name):
        for lib_name, lib in Uni.libraries.items():
            if name.lower() == lib_name.lower():
                return lib
        else:
            print("library's name is wrong!")



    def add_lib(self, lib: "Library") -> None:
        """this method is doing:
        1 - adding a library to libraries attribute of the university object
        2 - adding a file to the Uni directory with <id-name.txt> format; where name and id are library's

        :param lib: a library object that we're adding
        :type lib: Library
        """
        Uni.libraries[lib.name] = lib
        self.show_lib()
        lib.file.file_open()



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
        self.path = fR"{Uni.mother_dir}/{self.id}-{self.name}.csv"
        self.file = File(f"{self.id}-{self.name}.csv")
        self.books = self.file.book_initializer(self.name)



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

            

    def edit_book(self, book, new_name = "", new_rel_date = "", new_author = "", new_genre = ""):
        if new_name == "":
            new_name = book.name
        if new_rel_date == "":
            new_rel_date = book.rel_date
        if new_author == "":
            new_author = book.author
        if new_genre == "":
            new_genre = book.genre


        new_book = Book(self.name, new_name, new_rel_date, new_author, new_genre)
        self.file.remove_line(book.name)
        self.file.create_line(new_book)



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
    mother_dir = R"Uni\csv files"
    def __init__(self, name) -> None:
        self.name = name
        self.path = fR"{File.mother_dir}\{self.name}"
        self.file_open()
        self.df = self.data_frame_maker(self.path)


    def data_frame_maker(self, path):
        df = pd.read_csv(fR"Uni\csv files\{self.name}", delimiter=' ', names=["book", "release_date", "author", "genre"])
        return df


    def file_open(self):
        with open(self.path, 'a') as file:
            ...


    def book_initializer(self, libname):
        books = []
        for x in self.df.index:
            name = self.df.loc[x, 'book']
            release_date = self.df.loc[x, 'release_date']
            author = self.df.loc[x, 'author']
            genre = self.df.loc[x, 'genre']
            b = Book(libname, name, release_date, author, genre)
            books.append(b)
        return books


    def csv_writer(self):
        self.df.to_csv(self.path,header=False, index=False, sep=' ')


    def remove_line(self, book_name):
        for index in self.df.index:
            if self.df.loc[index, 'book'] == book_name:
                self.df.drop(index, axis=0, inplace=True)
        self.csv_writer()



    def create_line(self, book):
        data = {"book": [book.name], "release_date": [book.rel_date], "author": [book.author], "genre": [book.genre]}
        df2 = pd.DataFrame(data)
        self.df = pd.concat([self.df, df2], ignore_index=True)
        self.csv_writer()


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
        

