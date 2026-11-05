from datetime import date

class Person:
    """
    A Person, with a name and a date of birth.
    """
    def __init__(self, name, birth):
        """
        Constructor for Person.
        Raises TypeError if name is not a string or birth is not a date object.
        Raises ValueError if name is an empty string.
        """
        if not isinstance(name, str):
            raise TypeError
        if name == "":
            raise ValueError
        if not isinstance(birth, date):
            raise TypeError
        self.name = name
        self.birth = birth

    def initials(self):
        """Return uppercase initials from each part of the name."""
        parts = self.name.split()
        return ''.join(p[0].upper() for p in parts)

    def is_birthday(self):
        """Return True if today is the person's birthday, False otherwise."""
        today = date.today()
        return today.month == self.birth.month and today.day == self.birth.day