from book import Book
# I have moved Book class to the book.py file on "Part 6" of the lab as I have created it initially in main.py by error


book1 = Book("The Little Prince", "Antoine de Saint-Exupery", False)
book2 = Book("1984", "George Orwell")
# ==== Tests ====
book1.display_info()
book2.display_info()
print("==== tests borrow(), return_book() and display_info() =====")
book1.borrow()
book1.return_book()
book2.return_book()

book1.display_info()
book2.display_info()

print("=== test library name change ===")
print(Book.library_name)
Book.change_library_name("Bibliotheque de Vieux Saint-Laurent")
print("Library name changed to:", Book.library_name)

print("=== test static method ===")
print(Book.is_valid("New Title"))
print(Book.is_valid(""))
book3 = Book("", "Any Author")
book3 = Book("Clean Code", "Robert C.")
print(f"Book3 has been created with the title: '{book3.title}', and the author: {book3.author}")

print("=== tests after display_info method changed ===")
book3.display_info()
book3.borrow()
book3.display_info()

print("=== Test for show_count() class method ===")
Book.show_count()

print("=== Test an alternative constructor ===")
book4 = Book.from_string("The Pragmatic Programmer,David Tomas")
book4.display_info()