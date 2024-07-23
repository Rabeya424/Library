import os
import platform

# Global variable to store the list of books in the library
listBooks = [
    {"title": "Rabeya Cooks", "author": "Rabeya Begum", "ISBN": "786786", "copies": 5},
    {"title": "Sahara Cars", "author": "Sahara Rahman", "ISBN": "143143", "copies": 3},
    {"title": "Mikael Designs", "author": " Mikael", "ISBN": "246246", "copies": 7},
    {"title": "Issa Homes", "author": "Mohammed Issa", "ISBN": "139139", "copies": 4}
]

# Dictionary to track borrowed books by user
borrowed_books = {}

# Dictionary for staff login credentials with staff IDs
staff_credentials = {"kai": {"password": "cat", "id": "S001"}, "shai": {"password": "bird", "id": "S002"},
                     "iza": {"password": "cow", "id": "S003"}}

# Dictionary for user login credentials
user_credentials = {"adam": "burger", "idris": "pizza", "max": "fries"}

# Variable to store the role of the logged-in person
current_role = None


def login(role):
    """Function to authenticate users"""
    print(f"Enter your {role} username:")
    username = input()
    password = input(f"Enter your {role} password:")

    if role == "staff":
        staff_id = input("Enter your staff ID: ")
        if username in staff_credentials and staff_credentials[username]["password"] == password and \
                staff_credentials[username]["id"] == staff_id:
            global current_role
            current_role = "staff"
            return True
        else:
            print("Invalid username, password, or staff ID")
            return False
    elif role == "user" and username in user_credentials and user_credentials[username] == password:
        current_role = "user"
        return True
    else:
        print("Invalid username or password")
        return False


def register(role):
    """Function to register new users"""
    print(f"Registering a new {role}:")
    username = input("Enter a username: ")
    if role == "staff":
        if username in staff_credentials:
            print("This username is already taken.")
            return
        password = input("Enter a password: ")
        staff_id = input("Enter a unique staff ID: ")
        if any(staff["id"] == staff_id for staff in staff_credentials.values()):
            print("This staff ID is already taken.")
            return
        staff_credentials[username] = {"password": password, "id": staff_id}
        print(f"{role.capitalize()} registered successfully.")
    elif role == "user":
        if username in user_credentials:
            print("This username is already taken.")
            return
        password = input("Enter a password: ")
        user_credentials[username] = password
        print(f"{role.capitalize()} registered successfully.")


def manageLibrary():
    """main function to manage library operations"""
    print(""" 

  ------------------------------------------------------
 |======================================================| 
 |======== The Great Hartland Community Library ========|
 |======================================================|
  ------------------------------------------------------

Enter 1 : Staff Login
Enter 2 : User Login
Enter 3 : Register
Enter 4 : Exit 

       """)

    try:
        userInput = int(input("Please select an option: "))
    except ValueError:
        exit("\nInvalid Input. Please enter a number.")
    else:
        print("\n")

    if userInput == 1:
        if login("staff"):
            staff_menu()
        else:
            manageLibrary()

    elif userInput == 2:
        if login("user"):
            user_menu()
        else:
            manageLibrary()

    elif userInput == 3:
        print("Register as:\n1. Staff\n2. User")
        reg_choice = int(input())
        if reg_choice == 1:
            register("staff")
        elif reg_choice == 2:
            register("user")
        else:
            print("Invalid option.")
        manageLibrary()

    elif userInput == 4:
        print("Exiting Library Management System.")
        return

    else:
        print("Please Enter a Valid Option")

    manageLibrary()


def staff_menu():
    """Menu for staff operations"""
    while True:
        print("\nStaff Menu:")
        print("1. Add Book")
        print("2. Delete Book")
        print("3. Search Book")
        print("4. Update Book")
        print("5. Return to Login")
        print("Enter your choice:")
        staff_choice = int(input())

        if staff_choice == 1:
            add_book()
        elif staff_choice == 2:
            delete_book()
        elif staff_choice == 3:
            search_book()
        elif staff_choice == 4:
            update_book()  # Option for updating book details
        elif staff_choice == 5:
            break
        else:
            print("Invalid choice. Please enter a valid option.")


def user_menu():
    """Menu for user operations"""
    while True:
        print("\nUser Menu:")
        print("1. Borrow Book")
        print("2. Return Book")
        print("3. Return to Login")
        print("Enter your choice:")
        user_choice = int(input())

        if user_choice == 1:
            borrow_book()
        elif user_choice == 2:
            return_book()
        elif user_choice == 3:
            break
        else:
            print("Invalid choice. Please enter a valid option.")


def add_book():
    """Function to add a new book to the library"""
    print("Enter Title of the Book:")
    title = input()
    print("Enter Author of the Book:")
    author = input()
    print("Enter ISBN of the Book:")
    isbn = input()
    print("Enter Number of Copies:")
    copies = int(input())

    if any(book["ISBN"] == isbn for book in listBooks):
        print(f"\nThis Book with ISBN {isbn} Already Exists in the Library")
    else:
        listBooks.append({"title": title, "author": author, "ISBN": isbn, "copies": copies})
        print("\n=> New Book Added Successfully \n")
        for book in listBooks:
            print("Title: {}, Author: {}, ISBN: {}, Copies Available: {}".format(book["title"], book["author"],
                                                                                 book["ISBN"], book["copies"]))


def delete_book():
    """Function to delete a book from the library"""
    print("Enter Title of the Book to Delete:")
    delete_title = input()
    print("Enter Author of the Book to Delete:")
    delete_author = input()

    found = False
    for book in listBooks:
        if book["title"] == delete_title and book["author"] == delete_author:
            listBooks.remove(book)
            print("Book Removed Successfully")
            found = True
            break

    if not found:
        print("No Book Found with Title {} and Author {}".format(delete_title, delete_author))


def search_book():
    """Function to search for a book in the library"""
    print("Enter Title or Author to Search:")
    search_criteria = input().lower()

    found = False
    for book in listBooks:
        if search_criteria in book["title"].lower() or search_criteria in book["author"].lower():
            print("Book Found - Title: {}, Author: {}, ISBN: {}, Copies Available: {}".format(book["title"],
                                                                                              book["author"],
                                                                                              book["ISBN"],
                                                                                              book["copies"]))
            found = True

    if not found:
        print("No Book Found with Title or Author {}".format(search_criteria))


def update_book():
    """Function to update details of an existing book in the library"""
    print("Enter ISBN of the Book to Update:")
    isbn = input()

    found = False
    for book in listBooks:
        if book["ISBN"] == isbn:
            print("Enter New Title of the Book:")
            new_title = input()
            print("Enter New Author of the Book:")
            new_author = input()
            print("Enter New Number of Copies:")
            new_copies = int(input())

            # Update book details
            book["title"] = new_title
            book["author"] = new_author
            book["copies"] = new_copies

            print("Book Updated Successfully")
            found = True
            break

    if not found:
        print("No Book Found with ISBN")


def borrow_book():
    """Function for users to borrow a book from the library"""
    print("Enter Title of the Book to Borrow:")
    title = input()
    print("Enter Author of the Book:")
    author = input()
    name = input("Enter Your Name: ")

    for book in listBooks:
        if book["title"] == title and book["author"] == author:
            if book["copies"] > 0:
                book["copies"] -= 1
                if name not in borrowed_books:
                    borrowed_books[name] = []
                borrowed_books[name].append({"title": title, "author": author})
                print("Book Borrowed Successfully")
                return
            else:
                print("No Copies Available for Borrowing")
                return
    print("Book Not Found")


def return_book():
    """Function for users to return a borrowed book to the library"""
    print("Enter Title of the Book to Return:")
    title = input()
    print("Enter Author of the Book:")
    author = input()
    name = input("Enter Your Name: ")

    if name in borrowed_books:
        for book in borrowed_books[name]:
            if book["title"] == title and book["author"] == author:
                borrowed_books[name].remove(book)
                for book in listBooks:
                    if book["title"] == title and book["author"] == author:
                        book["copies"] += 1
                        print("Book Returned Successfully")
                        return
    print("Book Not Found in Borrowed List")


def runAgain():
    """Function to prompt user to continue managing library or exit"""
    run_again = input("\nDo you want to continue managing library (y/n)?: ").lower()
    if run_again == 'y':
        if platform.system() == "Windows":
            os.system('cls')
        else:
            os.system('clear')
        manageLibrary()
        runAgain()
    else:
        print("Exiting Library Management System.")


if __name__ == "__main__":
    manageLibrary()
    runAgain()

