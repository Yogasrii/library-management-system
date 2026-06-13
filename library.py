books = {}

while True:
    print("\n--- Library Management System ---")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        book_id = input("Enter Book ID: ")
        book_name = input("Enter Book Name: ")
        books[book_id] = book_name
        print("Book Added Successfully!")

    elif choice == "2":
        if books:
            for book_id, book_name in books.items():
                print(f"ID: {book_id}, Book: {book_name}")
        else:
            print("No Books Available!")

    elif choice == "3":
        book_id = input("Enter Book ID: ")
        if book_id in books:
            print("Book Found:", books[book_id])
        else:
            print("Book Not Found!")

    elif choice == "4":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")
