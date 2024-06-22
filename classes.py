import os

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


    def add_lib(self, lib: "Library") -> None:
        """this method is doing:
        1 - adding a library to libraries attribute of the university object
        2 - adding a file to the Uni directory with <id-name.txt> format; where name and id are library's

        :param lib: a library object that we're adding
        :type lib: Library
        """
        self.libraries[lib.name] = lib
        with open(lib.path, "w") as lib_file:
            lib_file.close()


    def remove_lib(self, lib: "Library") -> None:
        """this method is doing:
        1 - removing a function from libraries attribute of the university object
        2 - deleting file with <id-name.text> format; where name and id are library's

        :param lib: a library object
        :type lib: Library
        """
        del self.libraries[lib.name]
        os.remove(lib.path) 


    def show_lib(self):
        print("*"*40)
        print("\tlibraries: ")
        for lib in self.libraries.keys():
            print(lib)    
        print("*"*40)




class Library():
    mother_dir = R"C:\Users\PSK\Documents\GitHub\library-management\library-management\Uni"
    def __init__(self, name, id, books = []) -> None:
        self.name = name
        self.id = id
        self.books = books
        self.path = fR"{self.mother_dir}/{self.id}-{self.name}.txt"


    def add_book(self, book):
        """this method is doing:
        1 - adds the input book to the book sattribute of hte library object
        2 - adds the information of the book to the library file with <id-name.txt> name  

        :param book: an book object that we wawnt to add
        :type book: Book
        """
        self.books.append(book)
        with open(self.path, "a") as lib_file:
            lib_file.write(f"\n{book.name} {book.rel_date} {book.author} {book.genre}")    


    def remove_book(self, book):
        """removing a book object:
        from the list: library's books attribute
        from the library's file
        """
        self.books.remove(book) # removes the book from the books attribute of the library objects

        with open(self.path, "r") as lib_file: # open library file
            book_list = lib_file.readlines() # reading the lines of it
            # removing the book from the book_list
            for b in book_list:
                if book.name in b:
                    book_list.remove(b)
                    lib_file.close()
                    break
        with open(self.path, "w") as lib_file:
            lib_file.writelines(book_list)

            

    def edit_book(self, book, new_name, new_rel_data, new_author, new_genre):
        new_book = Book(new_name, new_rel_data, new_author, new_genre)
        self.add_book(new_book)
        self.remove_book(book)


    def lib_info(self):
        """prints out the library information by it's name
        """
        print("-" * 40)
        print(f"name: {self.name}\nid: {self.id}\n\tlist of the books:")
        for book in self.books:
            book.book_info()
        print("-" * 40)


class Book():
    def __init__(self, name, rel_date, author, genre) -> None:
        self.name = name.lower()
        self.rel_date = rel_date
        self.author = author.lower()
        self.genre = genre.lower()


    def book_info(self):
        """prints out the object book's information
        """
        print("-" * 40)
        print(f"name: {self.name}\nrelease date: {self.rel_date}\nauthor/writer: {self.author}\ngenre: {self.genre}")
        print("-" * 40)