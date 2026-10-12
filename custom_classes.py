"""Classes for a small library: media items, books, DVDs and a collection."""


class MediaItem:
    """A generic library item, such as a book or a movie.

    Attributes:
        title: The title of the item.
        author: The person who made the item, such as an author or a director.
        is_available: True if the item can be checked out right now.
    """

    def __init__(self, title, author, is_available=True):
        self.title = title
        self.author = author
        self.is_available = is_available

    def checkout(self):
        """Check the item out if it is available.

        Returns:
            "Successful checkout" if the item was available and is now checked
            out, otherwise "Already out".
        """
        if self.is_available:
            self.is_available = False
            return "Successful checkout"
        return "Already out"

    def return_item(self):
        """Mark the item as available again."""
        self.is_available = True

    def __str__(self):
        status = "Available" if self.is_available else "Checked Out"
        return f"{self.title} by {self.author} [{status}]"


class Book(MediaItem):
    """A library book, which also keeps track of its length.

    Attributes:
        page_count: The number of pages in the book.
    """

    def __init__(self, title, author, page_count, is_available=True):
        super().__init__(title, author, is_available)
        self.page_count = page_count

    def __str__(self):
        return f"{super().__str__()} ({self.page_count} pages)"


class DVD(MediaItem):
    """A DVD, which reminds the borrower to be careful when it is checked out.

    Attributes:
        duration: The running time of the DVD, in minutes.
    """

    def __init__(self, title, author, duration, is_available=True):
        super().__init__(title, author, is_available)
        self.duration = duration

    def checkout(self):
        """Check the DVD out and print a care reminder if that worked.

        The checkout itself is done by MediaItem.checkout(). The reminder is
        printed only when the checkout succeeds, not when the DVD is already out.

        Returns:
            The same message that MediaItem.checkout() returns.
        """
        was_available = self.is_available
        result = super().checkout()
        # Decide by state, not by the message text, so rewording the message
        # in MediaItem.checkout() cannot silently break this reminder.
        if was_available and not self.is_available:
            print("Handle with care: Do not scratch the disc.")
        return result


class LibraryCollection:
    """A collection of library items of any type.

    Attributes:
        items: The items added so far, in the order they were added.
    """

    def __init__(self):
        self.items = []

    def add_item(self, item):
        """Add an item to the collection.

        Args:
            item: A MediaItem, or one of its subclasses such as Book or DVD.
        """
        self.items.append(item)

    def list_available(self):
        """List the titles of the items that can be checked out right now.

        Returns:
            A list of title strings, in the order the items were added.
        """
        return [item.title for item in self.items if item.is_available]
