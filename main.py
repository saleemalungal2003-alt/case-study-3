from library import Library



books_data = {
    "B101": {"title": "Python Basics", "author": "Anu", "copies": 2},
    "B102": {"title": "Data Science 101", "author": "Binu", "copies": 1},
    "B103": {"title": "AWS Guide", "author": "Cathy", "copies": 3},
    "B104": {"title": "Statistics Made Easy", "author": "Dev", "copies": 1},
}

members_data = [
    {"id": "M1", "name": "Anu", "type": "student"},
    {"id": "M2", "name": "Binu", "type": "teacher"},
    {"id": "M3", "name": "Cathy", "type": "student"},
]


def main():
    library = Library()

    
    print("Task 1: Book catalogue")
    library.load_books(books_data)
    library.load_members(members_data)
    library.show_books()

    
    print("\nTask 2: Members")
    library.show_members()

    print("\nTask 3: Issue books")
    print(library.issue_book("M1", "B101"))
    print(library.issue_book("M1", "B102"))
    print(library.issue_book("M1", "B103"))
    print(library.issue_book("M3", "B102"))
    print(library.issue_book("M3", "B999"))

    
    print("\nTask 4: Teacher borrows")
    print(library.issue_book("M2", "B101"))
    print(library.issue_book("M2", "B103"))
    print(library.issue_book("M2", "B104"))
    print(library.issue_book("M2", "B102"))
    print(library.members["M2"])

   
    print("\nTask 5: Return books")
    print(library.return_book("M1", "B102"))
    print(library.return_book("M1", "B102"))
    print(library.issue_book("M3", "B102"))

    
    print("\nTask 6: Final status")
    library.show_books()
    library.show_members()
    total_on_loan = sum(len(m.borrowed) for m in library.members.values())
    print(f"Books on loan: {total_on_loan}")


if __name__ == "__main__":
    main()