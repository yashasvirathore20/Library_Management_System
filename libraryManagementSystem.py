"""
Library Management System 

Features:
1. Add Book
2. Borrow Book
3. Show High Rated Books
4. List Books by Language
5. Show Top Sellers
6. List Books by Author Name

CSV is used as the database.
"""

import csv
import os
import random

CSV_FILE = "library.csv"

# -------------------------------
# Setup Functions
# -------------------------------

def setup_csv():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["id","name","author","year","top_seller","rating","availability","language"])

def generate_id():
    return str(random.randint(1000, 9999))

def read_books():
    if not os.path.exists(CSV_FILE):
        setup_csv()
    with open(CSV_FILE, "r") as f:
        return list(csv.DictReader(f))

def write_books(books):
    with open(CSV_FILE, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=books[0].keys())
        writer.writeheader()
        writer.writerows(books)

# -------------------------------
# Book Management Functions
# -------------------------------
def show_books():
    books = read_books()
    print("\nBooks in Library:")
    for book in books:
        print(f"{book['name']} by {book['author']}, Published in {book['year']}, Rating: {rating}")


def add_book(name, author, year, top_seller, rating, availability, language):
    try:
        rating = float(rating)
    except ValueError:
        print("Rating must be a number.")
        return
    books = read_books()
    new_book = {
        "id": generate_id(),
        "name": name,
        "author": author,
        "year": str(year),
        "top_seller": str(top_seller),
        "rating": str(rating),
        "availability": str(availability),
        "language": language
    }
    books.append(new_book)
    write_books(books)
    print(f"Book '{name}' added successfully.")

def borrow_book(book_name):
    books = read_books()
    found = False
    for book in books:
        if book["name"].lower() == book_name.lower():
            found = True
            if int(book["availability"]) > 0:
                book["availability"] = str(int(book["availability"]) - 1)
                write_books(books)
                print(f"You borrowed '{book['name']}' by {book['author']}, Published in {book['year']}, Rating: {book['rating']}")
            else:
                print("Book out of stock.")
            break
    if not found:
        print("Not found or invalid.")

def show_high_rated():
    books = read_books()
    print("\nBooks with rating > 4.5:")
    for book in books:
        try:
            rating = float(book["rating"].strip())
        except ValueError:
            continue
        if rating > 4.5:
            print(f"{book['name']} by {book['author']}, Published in {book['year']}, Rating: {rating}")

def list_by_language(lang):
    books = read_books()
    found = False
    print(f"\nBooks in {lang}:")
    for book in books:
        if book["language"].strip().lower() == lang.lower():
            print(f"{book['name']} by {book['author']}, Published in {book['year']}, Rating: {book['rating']}")
            found = True
    if not found:
        print("Not Found!!!")

def show_top_sellers():
    books = read_books()
    found = False
    print("\nTop Sellers with rating > 4.5:")
    for book in books:
        try:
            rating = float(book["rating"].strip())
        except ValueError:
            continue
        if book["top_seller"].strip().lower() == "yes" and rating > 4.5:
            print(f"{book['name']} by {book['author']}, Published in {book['year']}, Rating: {rating}")
            found = True
    if not found:
        print("No top sellers found with rating > 4.5.")

def list_by_author(author_name):
    books = read_books()
    found = False
    print(f"\nBooks by {author_name}:")
    for book in books:
        if book["author"].strip().lower() == author_name.lower():
            print(f"{book['name']} by {book['author']}, Published in {book['year']}, Rating: {book['rating']}")
            found = True
    if not found:
        print("Not Found!!!")

# -------------------------------
# Menu System
# -------------------------------

def menu():
    setup_csv()
    while True:
        print("\nLibrary Menu")
        print("1. Add Book")
        print("2. Borrow Book")
        print("3. Show High Rated Books")
        print("4. List Books by Language")
        print("5. Show Top Sellers")
        print("6. List Books by Author")
        print("7. Exit")
        print("8. Show Books")
        
        choice = input("Enter choice: ")
        
        if choice == "1":
            name = input("Book name: ")
            author = input("Author: ")
            year = input("Year: ")
            top_seller = input("Top seller (yes/no): ")
            rating = input("Rating: ")
            availability = input("Availability (number of copies): ")
            language = input("Language: ")
            add_book(name, author, year, top_seller, rating, availability, language)
        elif choice == "2":
            book_name = input("Enter Book Name to borrow: ")
            borrow_book(book_name)
        elif choice == "3":
            show_high_rated()
        elif choice == "4":
            lang = input("Enter language: ")
            list_by_language(lang)
        elif choice == "5":
            show_top_sellers()
        elif choice == "6":
            author_name = input("Enter author name: ")
            list_by_author(author_name)
        elif choice == "7":
            print("Exit!!")
            break
        elif choice == "8":
            show_books()
            break
        else:
            print("Invalid choice, try again!!!!")

if __name__ == "__main__":
    menu()