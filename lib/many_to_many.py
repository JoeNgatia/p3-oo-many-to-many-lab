class Book:
    # Class variable to keep track of all Book instances
    all_books = []

    def __init__(self, title=""):
        """Initialize a new Book instance with the title."""
        self.title = title  # Set the book's title
        Book.all_books.append(self)  # Add the book to the list of all books

    @property
    def title(self):
        """Getter for the book title."""
        return self._title

    @title.setter
    def title(self, value):
        """Setter for the book title. Ensures the title is a string."""
        if not isinstance(value, str):
            raise Exception("Title must be a string.")  # Raise an error if the title is not a string
        self._title = value


class Author:
    # Class variable to keep track of all Author instances
    all_authors = []

    def __init__(self, name=""):
        """Initialize a new Author instance with the name."""
        self.name = name  # Set the author's name
        self._contracts = []  # List to hold the author's contracts
        Author.all_authors.append(self)  # Add the author to the list of all authors

    @property
    def name(self):
        """Getter for the author's name."""
        return self._name

    @name.setter
    def name(self, value):
        """Setter for the author's name. Ensures the name is a string."""
        if not isinstance(value, str):
            raise Exception("Name must be a string.")  # Raise an error if the name is not a string
        self._name = value

    def contracts(self):
        """Returns a list of contracts related to the author."""
        return self._contracts  # Return the list of contracts the author is part of

    def books(self):
        """Returns a list of books related to the author via contracts."""
        # Use the Contract class to find all books the author is involved with
        return [contract.book for contract in self._contracts]

    def sign_contract(self, book, date, royalties):
        """Create and return a new Contract between the author and a book."""
        # Validate inputs
        if not isinstance(book, Book):
            raise Exception("book must be an instance of Book.")  # Ensure the book is a Book object
        if not isinstance(date, str):
            raise Exception("date must be a string.")  # Ensure the date is a string
        if not isinstance(royalties, int) or not (0 <= royalties <= 100):
            raise Exception("royalties must be an integer between 0 and 100.")  # Ensure royalties are within valid range
        
        # Create a new contract
        contract = Contract(self, book, date, royalties)
        self._contracts.append(contract)  # Add the new contract to the author's list of contracts
        return contract

    def total_royalties(self):
        """Returns the total royalties earned from all of the author's contracts."""
        # Sum the royalties from all contracts associated with this author
        return sum(contract.royalties for contract in self._contracts)


class Contract:
    # Class variable to keep track of all Contract instances
    all_contracts = []

    def __init__(self, author, book, date, royalties):
        """Initialize a new Contract with the given author, book, date, and royalties."""
        self.author = author  # The Author associated with this contract
        self.book = book  # The Book associated with this contract
        self.date = date  # The date the contract was signed
        self.royalties = royalties  # The percentage of royalties for the author
        Contract.all_contracts.append(self)  # Add the contract to the list of all contracts

    @classmethod
    def contracts_by_date(cls, date):
        """Class method that returns all contracts signed on the specified date."""
        return [contract for contract in cls.all_contracts if contract.date == date]  # Filter contracts by date

    @property
    def royalties(self):
        """Getter for the royalties value."""
        return self._royalties

    @royalties.setter
    def royalties(self, value):
        """Setter for the royalties value. Ensures royalties are within the range 0-100."""
        if not isinstance(value, int) or not (0 <= value <= 100):
            raise Exception("Royalties must be an integer between 0 and 100.")  # Raise an error if royalties are invalid
        self._royalties = value  # Set the royalties value
