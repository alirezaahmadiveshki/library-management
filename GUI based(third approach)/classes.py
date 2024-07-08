import pandas as pd
import os
import customtkinter

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
        str = ""
        str += "*"*30
        str += "\n\tlibraries: "
        for lib in self.libraries.keys():
            str += f'\n{lib}'    
        str += "\n" + "*"*30
        return str




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
        self.remove_book(book)
        self.add_book(new_book)
        self.file.remove_line(book.name)
        self.file.create_line(new_book)



    def find_book(self, book_name):
        for book in self.books:
            if book.name.lower() == book_name.lower():
                return book
            


    def lib_info(self) -> None:
        """prints out the library information by it's name
        """
        str = ""
        str = "-" * 30
        str += f"\nname: {self.name}\nid: {self.id}\n\tlist of the books:"
        for book in self.books:
            str += book.book_info()
        return str




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
        str = ""
        str += "\n\n" \
            + f"library: {self.library}\nname: {self.name}\nrelease date: {self.rel_date}\nauthor/writer: {self.author}\ngenre: {self.genre}" 
        return str
            
        




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


class Window(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.university = Uni()
        customtkinter.set_appearance_mode("system")
        customtkinter.set_default_color_theme("dark-blue")
        self.title("Library Management")
        self.minsize(1000,500)
        #buttons
        self.grid_columnconfigure(1, weight=1)
        self.book_add = customtkinter.CTkButton(self, text = "add a book", command=self.func_book_add)
        self.book_del = customtkinter.CTkButton(self, text = "delete a book", command=self.func_book_del)
        self.book_edit = customtkinter.CTkButton(self, text = "edit a book", command=self.func_book_edit)
        self.book_info = customtkinter.CTkButton(self, text = "information of a book", command=self.func_book_info)
        self.lib_add = customtkinter.CTkButton(self, text = "adding of a library", command=self.func_lib_add)
        self.lib_del = customtkinter.CTkButton(self, text = "deleting a library", command=self.func_lib_del)
        self.lib_info = customtkinter.CTkButton(self, text = "information of a library", command=self.func_lib_info)
        self.exit_button = customtkinter.CTkButton(self, text = "Exit",command = self.destroy)
        self.book_del.grid(row=0 , column=0, padx=10, pady=6, ipadx=20, ipady=5)
        self.book_add.grid(row=1 , column=0, padx=10, pady=6, ipadx=20, ipady=5)
        self.book_edit.grid(row=2 , column=0, padx=10, pady=6, ipadx=20, ipady=5)
        self.book_info.grid(row=3 , column=0, padx=10, pady=6, ipadx=20, ipady=5)
        self.lib_add.grid(row=4 , column=0, padx=10, pady=6, ipadx=20, ipady=5)
        self.lib_del.grid(row=5 , column=0, padx=10, pady=6, ipadx=20, ipady=5)
        self.lib_info.grid(row=6 , column=0, padx=10, pady=6, ipadx=20, ipady=5)
        self.exit_button.grid(row=7 , column=0, padx=10, pady=6, ipadx=20, ipady=5) 

        self.messagebox = customtkinter.CTkTextbox(self, font=("Microsoft YaHei", 20))
        self.messagebox.grid(row=0, column=1, sticky="nesw", rowspan=8, pady=10, padx=10)

        self.button = customtkinter.CTkButton(self)
        self.entries = []
        self.text_entries = []





    def func_book_add(self):
        def submit_button_func():
            self.text_entries = []
            for entry in self.entries:
                text_entry = entry.get()
                self.text_entries.append(text_entry)
            lib_name = self.text_entries[0]
            book_name = self.text_entries[1]
            rel_date = self.text_entries[2]
            author = self.text_entries[3]
            genre = self.text_entries[4]
            lib = Uni.find_lib(lib_name)
            b = Book(lib_name, book_name, rel_date, author, genre)
            lib.add_book(b)
            output = lib.lib_info()
            self.messagebox.delete("0.0", "end")
            self.messagebox.insert("0.0", output)
        
        def submit_button_maker(n):
            self.button.destroy()
            self.button = customtkinter.CTkButton(self, text = "submit", height=70, command=submit_button_func)
            self.button.grid(row=n, column=0, columnspan=2, pady=20, padx=20, sticky="news")
        
        self.messagebox.delete("0.0", "end")
        text = self.university.show_lib()
        text = f"{text}\nEnter the Below Informations: "
        self.messagebox.insert("0.0", text)
        labels = ["library's name: ", "book's name: ", "book's release date: ", "book's author: ", "book's genre: "]
        for i in range(7):
            self.label_maker("", i+9, 0)
            self.label_maker("", i+9, 1)
        self.entries = []
        for i in range(5):
            self.label_maker(labels[i], i+9, 0)
            entry = self.entry_maker(i+9)
            self.entries.append(entry)
        submit_button_maker(14)
        


    def func_book_edit(self):
        def submit_button_func():
            self.text_entries = []
            for entry in self.entries:
                text_entry = entry.get()
                self.text_entries.append(text_entry)
            lib_name = self.text_entries[0]
            book_name = self.text_entries[1]
            new_book_name = self.text_entries[2]
            new_rel_date = self.text_entries[3]
            new_author = self.text_entries[4]
            new_genre = self.text_entries[5]
            lib = self.university.find_lib(lib_name)
            book = lib.find_book(book_name)
            print(book.book_info())
            lib.edit_book(book, new_book_name, new_rel_date, new_author, new_genre)
            output = ""
            output += f"{new_book_name} is succusfully edited"
            output = lib.lib_info()
            self.messagebox.delete("0.0", "end")
            self.messagebox.insert("0.0", output)
        
        def submit_button_maker(n):
            self.button.destroy()
            self.button = customtkinter.CTkButton(self, text = "submit", height=70, command=submit_button_func)
            self.button.grid(row=n, column=0, columnspan = 2,pady = 20,padx=30, sticky="nesw")


        self.messagebox.delete("0.0", "end")
        text = self.university.show_lib()
        text = f"{text}\nEnter the Below Informations: "
        self.messagebox.insert("0.0", text)
        labels = ["library's name: ", "book's name: ", "new book's name: ", "new book's release date: ", "new book's author: ", "new book's genre: "]
        for i in range(7):
            self.label_maker("", i+9, 0)
            self.label_maker("", i+9, 1)
        self.entries = []
        for i in range(6):
            self.label_maker(labels[i], i+9, 0)
            entry = self.entry_maker(i+9)
            self.entries.append(entry)
        submit_button_maker(15)


    def func_book_info(self):
        def submit_button_func():
            self.text_entries = []
            for entry in self.entries:
                text_entry = entry.get()
                self.text_entries.append(text_entry)
            book_name = self.text_entries[0]
            for lib in self.university.libraries.values(): # for every library in database
                book = lib.find_book(book_name) # return the object of the book with given name [output: NoneType | book object]
                if book: 
                    output = book.book_info()
            output += "\n"
            output += self.university.show_lib()
            self.messagebox.delete("0.0", "end")
            self.messagebox.insert("0.0", output)
        
        def submit_button_maker(n):
            self.button.destroy()
            self.button = customtkinter.CTkButton(self, text = "submit", height=70, command=submit_button_func)
            self.button.grid(row=n, column=0, columnspan = 2,pady = 20,padx=30, sticky="nesw")
        
        self.messagebox.delete("0.0", "end")
        text = self.university.show_lib()
        text = f"{text}\nEnter the Below Informations: "
        self.messagebox.insert("0.0", text)
        labels = ["book's name: "]
        for i in range(7):
            self.label_maker("", i+9, 0)
            self.label_maker("", i+9, 1)
        self.entries = []
        for i in range(1):
            self.label_maker(labels[i], i+9, 0)
            entry = self.entry_maker(i+9)
            self.entries.append(entry)
        submit_button_maker(10)


    def func_book_del(self):
        def submit_button_func():
            self.text_entries = []
            for entry in self.entries:
                text_entry = entry.get()
                self.text_entries.append(text_entry)
            lib_name = self.text_entries[0]
            book_name = self.text_entries[1]
            lib = self.university.find_lib(lib_name)
            book = lib.find_book(book_name)
            lib.remove_book(book)
            output = ""
            output += f"{book_name} is seccesfully removed"
            self.messagebox.delete("0.0", "end")
            self.messagebox.insert("0.0", output)
        
        def submit_button_maker(n):
            self.button.destroy()
            self.button = customtkinter.CTkButton(self, text = "submit", height=70, command=submit_button_func)
            self.button.grid(row=n, column=0, columnspan = 2,pady = 20,padx=30, sticky="nesw")
        
        self.messagebox.delete("0.0", "end")
        text = self.university.show_lib()
        text = f"{text}\nEnter the Below Informations: "
        self.messagebox.insert("0.0", text)
        labels = ["library's name: ", "book's name: "]
        for i in range(7):
            self.label_maker("", i+9, 0)
            self.label_maker("", i+9, 1)
        self.entries = []
        for i in range(2):
            self.label_maker(labels[i], i+9, 0)
            entry = self.entry_maker(i+9)
            self.entries.append(entry)
        submit_button_maker(11)



    def func_lib_add(self):
        def submit_button_func():
            self.text_entries = []
            for entry in self.entries:
                text_entry = entry.get()
                self.text_entries.append(text_entry)
            lib_name = self.text_entries[0]
            lib_id = self.text_entries[1]
            self.university.add_lib(Library(lib_name, lib_id))
            output = ""
            output += f"{lib_name} is seccesfully added"
            self.messagebox.delete("0.0", "end")
            self.messagebox.insert("0.0", output)
        
        def submit_button_maker(n):
            self.button.destroy()
            self.button = customtkinter.CTkButton(self, text = "submit", height=70, command=submit_button_func)
            self.button.grid(row=n, column=0, columnspan = 2,pady = 20,padx=30, sticky="nesw")
        
        self.messagebox.delete("0.0", "end")
        text = self.university.show_lib()
        text = f"{text}\nEnter the Below Informations: "
        self.messagebox.insert("0.0", text)
        labels = ["library's name: ", "library's id: "]
        for i in range(7):
            self.label_maker("", i+9, 0)
            self.label_maker("", i+9, 1)
        self.entries = []
        for i in range(2):
            self.label_maker(labels[i], i+9, 0)
            entry = self.entry_maker(i+9)
            self.entries.append(entry)
        submit_button_maker(11)

    
    def func_lib_del(self):
        def submit_button_func():
            self.text_entries = []
            for entry in self.entries:
                text_entry = entry.get()
                self.text_entries.append(text_entry)
            lib_name = self.text_entries[0]
            lib_name = lib_name.lower()
            lib = self.university.libraries[lib_name]
            self.university.remove_lib(lib)
            output = ""
            output += f"{lib_name} is succesfully removed\n"
            output += "remain libraries\n"
            output += self.university.show_lib()
            self.messagebox.delete("0.0", "end")
            self.messagebox.insert("0.0", output)
        
        def submit_button_maker(n):
            self.button.destroy()
            self.button = customtkinter.CTkButton(self, text = "submit", height=70, command=submit_button_func)
            self.button.grid(row=n, column=0, columnspan = 2,pady = 20,padx=30, sticky="nesw")
        
        self.messagebox.delete("0.0", "end")
        text = self.university.show_lib()
        text = f"{text}\nEnter the Below Informations: "
        self.messagebox.insert("0.0", text)
        labels = ["library's name: "]
        for i in range(7):
            self.label_maker("", i+9, 0)
            self.label_maker("", i+9, 1)
        self.entries = []
        for i in range(1):
            self.label_maker(labels[i], i+9, 0)
            entry = self.entry_maker(i+9)
            self.entries.append(entry)
        submit_button_maker(10)


    def func_lib_info(self):
        def submit_button_func():
            print(self.entries)
            self.text_entries = []
            for entry in self.entries:
                text_entry = entry.get()
                self.text_entries.append(text_entry)
            lib_name = self.text_entries[0]
            lib_name = lib_name.lower()
            lib = Uni.find_lib(lib_name)
            output = lib.lib_info()
            self.messagebox.delete("0.0", "end")
            self.messagebox.insert("0.0", output)
        
        def submit_button_maker(n):
            self.button.destroy()   
            self.button = customtkinter.CTkButton(self, text = "submit", height=70, command=submit_button_func)
            self.button.grid(row=n, column=0, columnspan = 2,pady = 20,padx=30, sticky="nesw")
        
        self.messagebox.delete("0.0", "end")
        text = self.university.show_lib()
        text = f"{text}\nEnter the Below Informations: "
        self.messagebox.insert("0.0", text)
        labels = ["library's name: "]
        for i in range(6):
            self.label_maker("", i+9, 0)
            self.label_maker("", i+9, 1)
        self.entries = []
        for i in range(1):
            self.label_maker(labels[i], i+9, 0)
            entry = self.entry_maker(i+9)
            self.entries.append(entry)
        submit_button_maker(10)



    def label_maker(self, label, row, column):
        my_label = customtkinter.CTkLabel(self, text=label, font=("Cascadia Code", 15))
        my_label.grid(row=row, column=column, sticky='nesw', pady= 10, padx= 20)
        return my_label

    def entry_maker(self, row):
        my_entry = customtkinter.CTkEntry(self, font=("Cascadia Code", 15))
        my_entry.grid(row =row, column=1, sticky='nesw', pady= 10, padx= 20)
        return my_entry