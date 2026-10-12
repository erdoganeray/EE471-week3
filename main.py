from custom_classes import DVD, Book, MediaItem


def print_separator():
    print("*" * 40)


def demo_media_items():
    book = MediaItem("The Hobbit", "J.R.R. Tolkien")        # is_available = True by default
    movie = MediaItem("Inception", "Christopher Nolan")     # is_available = True by default

    print_separator()
    print("Library items:")
    print(book)
    print(movie)

    print_separator()
    print("\nChecking out the book...")
    print(book.checkout())
    print(book)

    print_separator()
    print("\nTrying to check out the book again...")
    print(book.checkout())

    print_separator()
    print("\nReturning the book...")
    book.return_item()
    print(book)


def demo_book():
    novel = Book("Dune", "Frank Herbert", page_count=412)

    print_separator()
    print("Book with a page count:")
    print(novel)


def demo_dvd():
    dvd = DVD("Interstellar", "Christopher Nolan", duration=169)   # duration in minutes

    print_separator()
    print("DVD:")
    print(dvd)
    print(f"Duration: {dvd.duration} minutes")

    print_separator()
    print("\nChecking out the DVD...")
    print(dvd.checkout())
    print(dvd)

    print_separator()
    print("\nTrying to check out the DVD again...")
    print(dvd.checkout())
    print_separator()


def main():
    demo_media_items()
    demo_book()
    demo_dvd()


if __name__ == "__main__":
    main()
