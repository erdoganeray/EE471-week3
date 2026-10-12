class MediaItem:
    """A generic library item, such as a book or a movie."""

    def __init__(self, title, author, is_available=True):
        self.title = title
        self.author = author
        self.is_available = is_available

    def checkout(self):
        if self.is_available:
            self.is_available = False
            return "Successful checkout"
        return "Already out"

    def return_item(self):
        self.is_available = True

    def __str__(self):
        status = "Available" if self.is_available else "Checked Out"
        return f"{self.title} by {self.author} [{status}]"


class Book(MediaItem):
    def __init__(self, title, author, page_count, is_available=True):
        super().__init__(title, author, is_available)
        self.page_count = page_count

    def __str__(self):
        return f"{super().__str__()} ({self.page_count} pages)"


class DVD(MediaItem):
    def __init__(self, title, author, duration, is_available=True):
        super().__init__(title, author, is_available)
        self.duration = duration

    def checkout(self):
        was_available = self.is_available
        result = super().checkout()
        # Decide by state, not by the message text, so rewording the message
        # in MediaItem.checkout() cannot silently break this reminder.
        if was_available and not self.is_available:
            print("Handle with care: Do not scratch the disc.")
        return result


class LibraryCollection:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def list_available(self):
        return [item.title for item in self.items if item.is_available]
