class Town:
    """
    Represents a town with name and number of residents.

    :param str name: The name of the town.
    :param int residents: The number of residents in the town.
    """

    def __init__(self, name, residents):
        self.name = name
        self.residents = residents

    @property
    def name(self):
        """The name of the town."""
        return self.__name

    @name.setter
    def name(self, value):
        if value and not value.isspace():
            self.__name = value
        else:
            raise ValueError("Name cannot be null, empty or contain only white spaces.")

    @property
    def residents(self):
        """The number of residents in the town."""
        return self.__residents

    @residents.setter
    def residents(self, value):
        # Hier ist die Änderung:
        # Wir prüfen erst, ob es überhaupt eine Zahl ist
        if not isinstance(value, int):
             raise ValueError("Residents must be an integer.")
        
        # Wenn die Zahl negativ ist, setzen wir sie auf 0 (statt abzustürzen)
        if value < 0:
            self.__residents = 0
        else:
            self.__residents = value

    def __str__(self):
        """Returns a human readable string of the object."""
        return f"The town {self.name} has {self.residents} residents."

    def __repr__(self):
        """Returns a string representation of the object."""
        return f"{type(self).__name__}({self.name!r}, {self.residents!r})"