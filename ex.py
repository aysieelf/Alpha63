class LibraryItem:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value: str):
        if not value.isalpha():
            raise ValueError("Title must be only letters")
        if len(value) > 16:
            raise ValueError("Title can't be longer that 16 characters")

        self._title = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value: str):
        if not value.isalpha():
            raise ValueError("Author must be only letters")

        self._author = value.capitalize()

    def get_description(self) -> str:
        return f"Book name: {self.title}, Author: {self.author}"
