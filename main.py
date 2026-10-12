from custom_classes import MediaItem


def main():
    book = MediaItem("The Hobbit", "J.R.R. Tolkien")        # is_available = True by default
    movie = MediaItem("Inception", "Christopher Nolan")     # is_available = True by default

    print("*" * 40)
    print("Library items:")
    print(book)
    print(movie)

    print("*" * 40)
    print("\nChecking out the book...")
    print(book.checkout())
    print(book)

    print("*" * 40)
    print("\nTrying to check out the book again...")
    print(book.checkout())

    print("*" * 40)
    print("\nReturning the book...")
    book.return_item()
    print(book)
    print("*" * 40)


if __name__ == "__main__":
    main()
