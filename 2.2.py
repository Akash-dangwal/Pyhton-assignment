from datetime import datetime, timedelta

class Library:
    def __init__(self):
        self.books = {
            1: {"title": "Book1", "author": "Author1", "quantity": 5},
            2: {"title": "Book2", "author": "Author2", "quantity": 3},
            3: {"title": "Book3", "author": "Author3", "quantity": 2}
        }
        self.users = {}
        self.transactions = {}

    def display_books(self):
        print("Available Books:")
        for book_id, book_info in self.books.items():
            availability = "Available" if book_info["quantity"] > 0 else "Not Available"
            print(f"ID: {book_id}, Title: {book_info['title']}, Author: {book_info['author']}, Availability: {availability}")

    def register_user(self, user_id, name):
        self.users[user_id] = {"name": name, "books_checked_out": []}

    def checkout_book(self, user_id, book_id, checkout_date):
        if user_id not in self.users:
            print("User not registered.")
            return

        if book_id not in self.books:
            print("Book not found.")
            return

        if len(self.users[user_id]["books_checked_out"]) >= 3:
            print("Maximum limit of checked out books reached.")
            return

        if self.books[book_id]["quantity"] == 0:
            print("Book not available.")
            return

        self.users[user_id]["books_checked_out"].append({"book_id": book_id, "checkout_date": checkout_date})
        self.books[book_id]["quantity"] -= 1
        self.transactions[(user_id, book_id)] = checkout_date
        print("Book checked out successfully.")

    def return_book(self, user_id, book_id, return_date):
        if (user_id, book_id) not in self.transactions:
            print("This book was not checked out by this user.")
            return

        checkout_date = self.transactions[(user_id, book_id)]
        del self.transactions[(user_id, book_id)]
        self.users[user_id]["books_checked_out"] = [book for book in self.users[user_id]["books_checked_out"] if book["book_id"] != book_id]
        self.books[book_id]["quantity"] += 1

        due_date = checkout_date + timedelta(days=14)
        if return_date > due_date:
            overdue_days = (return_date - due_date).days
            fine = overdue_days * 1  # $1 per day overdue
            print(f"Book returned {overdue_days} days overdue. Fine: ${fine}")
        else:
            print("Book returned successfully.")

    def list_overdue_books(self, user_id):
        overdue_books = []
        total_fine = 0
        for book in self.users[user_id]["books_checked_out"]:
            book_id = book["book_id"]
            checkout_date = book["checkout_date"]
            due_date = checkout_date + timedelta(days=14)
            if datetime.now() > due_date:
                overdue_days = (datetime.now() - due_date).days
                fine = overdue_days * 1  # $1 per day overdue
                total_fine += fine
                overdue_books.append({"book_id": book_id, "fine": fine})
        if overdue_books:
            print("Overdue Books:")
            for overdue_book in overdue_books:
                print(f"Book ID: {overdue_book['book_id']}, Fine: ${overdue_book['fine']}")
            print(f"Total Fine Due: ${total_fine}")
        else:
            print("No overdue books for this user.")


lib = Library()

# Display the current catalog
lib.display_books()

# Register a user
lib.register_user(1, "Akash")

# Checkout books for the user
lib.checkout_book(1, 1, datetime.now() - timedelta(days=2))
lib.checkout_book(1, 2, datetime.now() - timedelta(days=5))

# Return books for the user
lib.return_book(1, 1, datetime.now() - timedelta(days=1))
lib.return_book(1, 2, datetime.now())

# List overdue books for the user
lib.list_overdue_books(1)
