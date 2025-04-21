class Shelter:
    """
    Class representing a Shelter (parent class for Tent, Hammock, and Tarp).

    Attributes:
        num_occupants (int): Number of occupants the shelter can fit.
        material (str): Shelter material.
        setup_time (int): Setup time (minutes).
        weight (float): Weight of the shelter in ounces.
        seasons (int): Season rating (default: 3).

    Methods:
        is_better: Compares shelters by weight, setup_time, and seasons to determine the "better" one.
        total_sleep_spots: Returns the total sleeping spots from a list of Shelters.
        __str__: Returns a user-friendly string representation of a Shelter.
        __repr__: Returns a developer-friendly string representation of a Shelter.
        __lt__: Handles comparisons between different subclasses of Shelter.
    """

    def __init__(self,
                 num_occupants: int,
                 material: str,
                 setup_time: int,
                 weight: float,
                 seasons: int = 3):
        """
        Init function for the Shelter class.

        Args:
            num_occupants (int): Number of occupants the shelter can fit.
            material (str): The shelter material.
            setup_time (int): Setup time in minutes.
            weight (float): Weight of the shelter in ounces.
            seasons (int): Season rating (default: 3).
        """
        self.num_occupants = num_occupants
        self.material = material
        self.setup_time = setup_time
        self.weight = weight
        self.seasons = seasons

    def is_better(self, other: 'Shelter') -> bool:
        """
        Determines if this shelter is "better" than another.

        Args:
            other (Shelter): The other shelter to compare.

        Returns:
            bool: True if this shelter is better; False otherwise.
        """
        if not isinstance(other, Shelter):
            return NotImplemented

        return (
                self.weight < other.weight and
                self.setup_time < other.setup_time and
                self.seasons >= other.seasons)

    @staticmethod
    def total_sleep_spots(shelters: list) -> int:
        """
        Returns total number of sleeping spots available across a list of shelters.

        Args:
            shelters (list): List of Shelter objects.

        Returns:
            int: Total number of sleeping spots.
        """
        return sum(shelter.num_occupants for shelter in shelters)

    def __repr__(self):
        """
        Didn't feel like having this twice anymore, so returning str.
        """
        return self.__str__()


class Tent(Shelter):
    """
    Class representing a Tent (inherits from Shelter).

    Class Level Args:
        sqft (float): Square footage of the tent.
        vestibule (bool): Whether the tent has a vestibule.
        structure_poles (bool): Whether the tent has structural poles (default: True).

    Methods:
        __lt__: Compares two Tents based on num_occupants and sqft.
        __str__: Returns a string representation of a Tent.
    """

    def __init__(self,
                 num_occupants: int,
                 material: str,
                 setup_time: int,
                 sqft: float,
                 vestibule: bool,
                 weight: float,
                 structure_poles: bool = True,
                 seasons: int = 3):
        """
        Init function for the Tent class.

        Args:
            num_occupants (int): Number of occupants the tent can fit.
            material (str): The tent material.
            setup_time (int): Setup time in minutes.
            sqft (float): Square footage of tent.
            vestibule (bool): Whether the tent has a vestibule.
            weight (float): Weight of the tent in ounces.
            structure_poles (bool): If the tent has structural poles (default: True).
            seasons (int): Season rating (default: 3).
        """
        super().__init__(num_occupants, material, setup_time, weight, seasons)
        self.sqft = sqft
        self.vestibule = vestibule
        self.structure_poles = structure_poles

    def __str__(self):
        """
        Return string representation of a Tent.
        """
        return (
            f"Tent({self.num_occupants}, {self.material}, "
            f"{self.setup_time}, {self.sqft}, {self.vestibule}, "
            f"{self.weight}, {self.structure_poles}, {self.seasons})"
        )

    def __lt__(self, other: 'Tent') -> bool:
        """
        Compares two Tents based on num_occupants and sqft.

        Args:
            other (Tent): The other tent to compare.
        Returns:
            bool: True if both num_occupants and sqft are strictly less than the other tent.
        """
        if not isinstance(other, Tent):
            return NotImplemented
        return self.num_occupants < other.num_occupants and self.sqft < other.sqft


class Hammock(Shelter):
    """
    Class representing a Hammock (inherits from Shelter).

    Class Level Args:
        length (int): Length of hammock in feet (default: 11).

    Methods:
        __lt__: Compares two Hammocks based on weight and setup_time.
        __str__: Returns a string representation of a Hammock.
    """

    def __init__(self,
                 num_occupants: int,
                 material: str,
                 setup_time: int,
                 weight: float,
                 length: int = 11,
                 seasons: int = 3):
        """
        Init function for the Hammock class.

        Args:
            num_occupants (int): Number of occupants the hammock can fit.
            material (str): Hammock material.
            setup_time (int): Setup time in minutes.
            weight (float): Weight of the hammock in ounces.
            length (int): Length of hammock in feet (default: 11).
            seasons (int): Season rating (default: 3).
        """
        super().__init__(num_occupants, material, setup_time, weight, seasons)
        self.length = length

    def __str__(self):
        """
        Return user-friendly string representation of a Hammock by appending subclass-specific attributes.
        """
        # TODO: Length was left out of the instructions in step 2 but I put it in here
        return (f"Hammock({self.num_occupants}, {self.material}, "
            f"{self.setup_time}, {self.weight}, {self.length}, {self.seasons})")

    def __lt__(self, other: 'Hammock') -> bool:
        """
        Compares two Hammocks based on weight and setup time.

        Args:
            other (Hammock): The other hammock to compare.

        Returns:
            bool: True if both weight and setup_time are strictly less than the other hammock.
        """
        if not isinstance(other, Hammock):
            return NotImplemented
        return self.weight < other.weight and self.setup_time < other.setup_time


class Tarp(Shelter):
    """
    Class representing a Tarp (inherits from Shelter).

    Class Level Args:
        sqft (float): Square footage of the tarp.

    Methods:
        __lt__: Compares two Tarps based on num_occupants and sqft.
        __str__: Returns a string representation of a Tarp.
    """

    def __init__(self,
                 num_occupants: int,
                 material: str,
                 setup_time: int,
                 sqft: float,
                 weight: float,
                 seasons: int = 3):
        """
        Init function for the Tarp class.

        Args:
            num_occupants (int): Number of occupants the tarp can accommodate.
            material (str): Tarp material.
            setup_time (int): Setup time in minutes.
            sqft (float): Square footage of tarp.
            weight (float): Weight of the tarp in ounces.
            seasons (int): Season rating (3 or 4, default: 3).
        """
        super().__init__(num_occupants, material, setup_time, weight, seasons)
        self.sqft = sqft

    def __str__(self):
        """
        Return string representation of a Tarp.
        """
        return(f"Tarp({self.num_occupants}, {self.material}, "
            f"{self.setup_time}, {self.sqft}, {self.weight}, {self.seasons})")

    def __lt__(self, other: 'Tarp') -> bool:
        """
        Compares two Tarps based on num_occupants and sqft.

        Args:
            other (Tarp): The other tarp to compare.

        Returns:
            bool: True if both num_occupants and sqft are strictly less than other tarp.
        """
        if not isinstance(other, Tarp):
            return NotImplemented
        return self.num_occupants < other.num_occupants and self.sqft < other.sqft
