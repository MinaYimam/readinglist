""" Program to create and manage a list of books that the user wishes to read, and books that the user has read. """

from bookstore import Book, BookStore
from menu import Menu
import ui

store = BookStore()

def main():

    menu = create_menu()

    while True:
        choice = ui.display_menu_get_choice(menu)
        action = menu.get_action(choice)
        action()
        # if the user enters the lowercase q the program will pass 
        if choice == 'Q':
            break



def create_menu():
    menu = Menu()
    menu.add_option('1', 'Add Book', add_book)
    menu.add_option('2', 'Search For Book', search_book)
    menu.add_option('3', 'Show Unread Books', show_unread_books)
    menu.add_option('4', 'Show Read Books', show_read_books)
    menu.add_option('5', 'Show All Books', show_all_books)
    menu.add_option('6', 'Change Book Read Status', change_read)
    menu.add_option('7', 'Delete', delete_books)
    menu.add_option('Q', 'Quit', quit_program)
    
    return menu


def add_book():
    new_book = ui.get_book_info()
    new_book.save()
    

def show_read_books():
    read_books = store.get_books_by_read_value(True)
    ui.show_books(read_books)


def show_unread_books():
    unread_books = store.get_books_by_read_value(False)
    ui.show_books(unread_books)


def show_all_books():
    books = store.get_all_books()
    ui.show_books(books)


def search_book():
    search_term = ui.ask_question('Enter search term, will match partial authors or titles.')
    matches = store.book_search(search_term)
    ui.show_books(matches)


def change_read():
    book_id = ui.get_book_id()

    book = store.get_book_by_id(book_id)
    if book:
        new_read = ui.get_read_value()
        book.read = new_read
        book.save()
    else:
        print('There is no book found with that id!')


def delete_books():
    try:
        book_id = ui.get_book_id()
        book = store.get_book_by_id(book_id)  
        store._delete_book(book)

    except :
        print('This id book not found')


       




def quit_program():
    ui.message('Thanks and bye!')


if __name__ == '__main__':
    main()
