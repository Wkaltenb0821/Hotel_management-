from Guest import Guest

class HotelAlphabetical:
    """Class representing a hotel where guests are stored in rooms based on
    the first initial of their names. Each room is a linked list of guests.
    """
    
    #Constants for hotel
    _DEFAULT_CAPACITY = 26
    _ASCII_LEFT_EDGE = ord("A")
    _ASCII_RIGHT_EDGE = ord("Z")
    _EMPTY = "boohoo, your hotel is empty."
    _NEXT_GUEST = " --> "

    _LOAD_FACTOR_THRESHOLD = 0.7
    _INCREMENT_FACTOR = 2

    def __init__(self, capacity: int = _DEFAULT_CAPACITY):
        self._capacity = capacity
        self._hotel = [None] * capacity  # Array of linked lists for each letter
        self._usage = 0  # number of array slots used
        self._size = 0

    def _get_index(self, name: str) -> int:
        """Compute the index in the hotel array based on the first
        initial of the guest's name."""
        # Default to 0 if name is None or empty or not A-Z
        room_index = 0
        if name is not None and len(name) > 0:
            # DISCUSSION POINT: should we be computing the first initial
            # here or should it be done in object Guest?
            initial_ascii = ord(name.upper()[0])
            if self._ASCII_LEFT_EDGE <= initial_ascii <= self._ASCII_RIGHT_EDGE:
                room_index = initial_ascii % self._capacity
        return room_index

    def _check_load_factor(self) -> bool:
        """Check if the load factor exceeds the threshold."""
        load_factor = self._usage / self._capacity
        return load_factor > self._LOAD_FACTOR_THRESHOLD

    def _rehash(self) -> None:
        """Rehash the hotel by increasing its capacity and reassigning guests."""
        # Preserve old hotel array and its capacity
        old_hotel = self._hotel
        old_capacity = self._capacity
        # Create new hotel array with increased capacity
        self._capacity *= self._INCREMENT_FACTOR
        # Initialize new hotel array and reset usage
        self._hotel = [None] * self._capacity
        self._usage = 0
        self._size = 0       # UPDATE Oct 16
        # Reinsert all guests into the new hotel array
        
        for room in range(old_capacity):
            guest_in_room = old_hotel[room]
            while guest_in_room is not None:
                self.add_guest(guest_in_room.get_name())
                guest_in_room = guest_in_room.get_next()

    def add_guest(self, name: str) -> None:
        """Add a guest to the hotel."""
        if self._check_load_factor():
            self._rehash()
        # Compute the room index based on the first initial of the name
        room = self._get_index(name)
        # Create a new guest object
        guest = Guest(name)
        # Insert guest at the front of the linked list for that room
        if self._hotel[room] is None:
            self._hotel[room] = guest
            self._usage += 1
        else:
            guest.set_next(self._hotel[room])
            self._hotel[room] = guest
        # Increment the current occupancy of the hotel
        self._size += 1

    def exists(self, guest_name: str) -> bool:  
        """Check if a guest with provided name is in the hotel.
        Returns True if present, False if otherwise. 
        """
        #Get room index for guest_name
        room_index = self._get_index(guest_name)
        #Set current_guest to head of room index
        current_guest = self._hotel[room_index]
        found = False
        while current_guest is not None:
            #If current guest_name matches guest name return true. 
            if current_guest.get_name() == guest_name:
                found = True
            current_guest = current_guest.get_next()
        return found

    def remove(self, guest_name: str):
        """Remove a guest by the provided name from the hotel.
        Returns the Guest object if removal succeeded; None if not found.
        """
        #Get current index from guest_name.
        room_index = self._get_index(guest_name)
        #Set current guest to head of room list. 
        current_guest = self._hotel[room_index]
        previous_guest = None
        removed_guest = None
        while current_guest is not None: 
            if current_guest.get_name() == guest_name:
                removed_guest = current_guest
                if previous_guest is None:
                    self._hotel[room_index] = current_guest.get_next()
                    if self._hotel[room_index] is None:
                        self._usage -= 1 #Decrement usage
                else:
                    #Sets previous_guest's name to current_guest's next decrement size
                    previous_guest.set_next(current_guest.get_next())
                self._size -= 1
            else:
                previous_guest = current_guest #Set previous_guest next to current_guest next. 
            current_guest = current_guest.get_next() #Move to next guest in the list. 
        return removed_guest

    def __repr__(self) -> str:
        hotel_string = self._EMPTY
        if self._size > 0: 
            hotel_string = f"\nThere are {self._size} guest(s) in your hotel."
            hotel_string += f"\nThe hotel has a capacity of {self._capacity} rooms."
            hotel_string += f" and is using {self._usage} room(s)."
            hotel_string += f"\nThe load factor is {self._usage/self._capacity:.2f}."
            hotel_string += f" The {self._size} guest(s) are:"
            for room in range(self._capacity):
                if self._hotel[room] is not None:
                    hotel_string += f"\n\tRoom {room:02d}: "
                    guest_in_room = self._hotel[room]
                    while guest_in_room is not None:
                        hotel_string += f"{guest_in_room.get_name()}{self._NEXT_GUEST}"
                        guest_in_room = guest_in_room.get_next()
                    hotel_string += ""
        return hotel_string

#Testing the code

"""Create hotel, add guests"""
if __name__ == "__main__":
    hotel = HotelAlphabetical()
    hotel.add_guest("Wallis")
    hotel.add_guest("Willow")
    hotel.add_guest("Will")
    hotel.add_guest("Wendy")
    hotel.add_guest("Wynona")
    hotel.add_guest("Zoe")
    hotel.add_guest("Ann") 

    print(hotel)

    print ("\nDoes Zoe exist?", hotel.exists ("Zoe"))
    print("Removal of Zoe...")
    hotel.remove("Zoe")

    print("\nAfter removing Zoe:")
    print(hotel)

    

