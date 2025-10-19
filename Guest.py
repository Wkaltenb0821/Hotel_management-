class Guest:
    """
    Class representing a guest in the hotel.
    Each guest stores their name and a reference to the next guest
    (used for constructing a linked list in each hotel room).
    """

    def __init__(self, name):
        """
        Initialize a Guest object with the provided name.

        Args:
            name (str): The name of the guest.
        """
        self._name = name
        self._next = None

    def get_name(self):
        """
        Return the name of the guest.

        Returns:
            str: The guest's name.
        """
        return self._name

    def get_next(self):
        """
        Return the next guest linked to this one.

        Returns:
            Guest or None: The next guest in the linked list, or None.
        """
        return self._next

    def set_next(self, next_guest):
        """
        Set the next guest linked to this one.

        Args:
            next_guest (Guest): The guest to link as next in the list.
        """
        self._next = next_guest

    def __repr__(self):
       """
        Return a string representation of the guest.

        Returns:
            str: Representation of the guest.
        """
        return f"Guest({self._name})"
