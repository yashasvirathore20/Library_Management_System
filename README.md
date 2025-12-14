# Library Management System (Python + CSV)

A simple command-line based Library Management System built using Python. This project uses a CSV file as a lightweight database to store and manage book records. It is suitable for beginners who want to understand file handling, CSV operations, and menu-driven programs in Python.

Features:

1)Add new books to the library
2)Borrow books with availability tracking
3)Display high-rated books
4)List books based on language
5)Show top-selling books with high ratings
6)Search and list books by author name
7)View all books stored in the library

All data is stored persistently using a CSV file, so the records remain available even after the program exits.

Technologies Used:

Python
CSV file handling
Standard Python libraries: csv, os, random

How It Works:

On the first run, the program automatically creates a library.csv file if it does not exist.

Each book record contains the following fields:
ID
Book Name
Author
Publication Year
Top Seller status (yes/no)
Rating
Availability (number of copies)
Language

A menu-driven interface allows users to interact with the system easily.
