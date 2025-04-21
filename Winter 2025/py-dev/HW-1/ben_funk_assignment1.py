# Imports
import itertools

'''
Helpers for printing
'''

TOGGLE_PRINT = False


def _set_print(set_type: bool):
    global TOGGLE_PRINT
    TOGGLE_PRINT = set_type


def _print(string):
    if TOGGLE_PRINT:
        print(string)


'''
Question 1
'''


def _return_average_val(num_list):

    """
    Calculates average values floored

    Args:
        num_list list: a list of numbers

    Returns:
        The average of the numbers in num_list
    """

    return sum(num_list) // len(num_list)


def paired_list(name_list: list = None,
                num_list: list = None) -> list:
    """

    This takes in 2 lists and combines them into one list, accounting for the three different possibilities of input list length.


    Args:
        name_list (list): A list of names as strings.
        num_list (list): A list of integers.

    Returns:
        list: A list of tuples combining elements from `name_list` and `num_list`.

    Raises:
        ValueError: If `name_list` or `num_list` is empty or None.
    """

    if name_list is None or num_list is None or len(name_list) == 0 or len(num_list) == 0:
        raise ValueError("Inputs did not conform to defined parameters. Try again")

    if len(name_list) > len(num_list):
        extra_num = _return_average_val(num_list)
        comb_list = list(itertools.zip_longest(name_list, num_list, fillvalue=extra_num))

    elif len(name_list) < len(num_list):
        comb_list = list(itertools.zip_longest(name_list, num_list, fillvalue='FNU'))

    else:
        comb_list = list(zip(name_list, num_list))

    return comb_list


'''
Question 2
'''


def even_odd_pairs(paired_list: list,
                   even: bool = True) -> list:
    """
    filters a list of tuples based on even/odd int in the tuple.

    Args:
        paired_list (list): A list of tuples, second element is integer.
        even (bool): A flag to determine filter for even numbers (True) or
                     odd numbers (False). Defaults True.

    Returns:
        list: Filtered list of tuples containing only those tuples where the integer
              matches the even/odd condition.

    Raises:
        ValueError: Checks that inputs meet required conditions.
    """

    if not all(isinstance(pair, tuple) and len(pair) == 2 and isinstance(pair[1], int) for pair in paired_list):
        raise ValueError("Input must be a list of tuples with the second element being an integer.")

    if even:
        return [pair for pair in paired_list if pair[1] % 2 == 0]

    else:
        return [pair for pair in paired_list if pair[1] % 2 != 0]


'''
Question 3:
'''


class Tent:

    """
        Class representing a Tent.

        Attributes:
            num_occupants (int): Number of occupants a tent can fit.
            material (str): Tent material.
            setup_time (int): Setup time (minutes).
            sqft (float): Square footage of a tent.
            vestibule (bool): Whether the tent has a vestibule.
            weight (float): Weight of tent in ounces.
            structure_poles (bool): If tent has structural poles (default: True).
            seasons (int): Season rating (default: 3).

        Methods:
            __str__: Returns a user string representation of Tent.
            __repr__: Returns a developer string representation of Tent.
            __lt__: Compares two Tents based on `num_occupants` and `sqft`.
            is_better: Determines if a Tent is "better" than another using weight, setup time, and season rating.
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

        self.num_occupants = num_occupants
        self.material = material
        self.setup_time = setup_time
        self.sqft = sqft
        self.vestibule = vestibule
        self.weight = weight
        self.structure_poles = structure_poles
        self.seasons = seasons

    def __str__(self):

        """
        Returns string representation of a Tent.
        """

        return (
            f"Tent(Occupants: {self.num_occupants}, Material: {self.material}, "
            f"Setup Time: {self.setup_time} mins, SqFt: {self.sqft}, Vestibule: {self.vestibule}, "
            f"Weight: {self.weight} oz, Structural Poles: {self.structure_poles}, Seasons: {self.seasons})")

    def __repr__(self):

        """
        Returns dev-friendly string representation of Tent.
        """

        return (
            f"Tent(num_occupants={self.num_occupants}, material='{self.material}', "
            f"setup_time={self.setup_time}, sqft={self.sqft}, vestibule={self.vestibule}, "
            f"weight={self.weight}, structure_poles={self.structure_poles}, seasons={self.seasons})")

    def __lt__(self, other: 'Tent') -> bool:

        """
        Compares two tents w/ `num_occupants` and `sqft`.

        Args:
            other (Tent): The other tent to compare.

        Returns:
            bool: True if both `num_occupants` and `sqft` of this tent are strictly less than the other tent.
        """

        if not isinstance(other, Tent):
            return NotImplemented
        return self.num_occupants < other.num_occupants and self.sqft < other.sqft

    def is_better(self, other: 'Tent') -> bool:

        """
        Determines if tent is "better" than another.

        Args:
            other (Tent): The other tent to compare with.

        Returns:
            bool: True if this tent is better; False otherwise.
        """

        if not isinstance(other, Tent):
            return NotImplemented

        return (
                self.weight < other.weight and
                self.setup_time < other.setup_time and
                self.seasons >= other.seasons)


'''
Question 4:
'''


class Hammock:

    """
    Class representing a Hammock.

    Attributes:
        num_occupants (int): Number of occupants the hammock can fit.
        material (str): Hammock material.
        setup_time (int): Setup time, minutes.
        weight (float): Weight of hammock ounces.
        length (int): Length of hammock feet (default: 11).
        seasons (int): Season rating (default: 3).

    Methods:
        __str__: Returns a user-friendly string representation of a Hammock.
        __repr__: Returns a developer-friendly string representation of a Hammock.
        __lt__: Compares two Hammocks based on weight and setup time.
        is_better: Determines if this Hammock is "better" than another based on weight, setup time, and season rating.

    """

    def __init__(
            self,
            num_occupants: int,
            material: str,
            setup_time: int,
            weight: float,
            length: int = 11,
            seasons: int = 3):

        """
        Init function for the hammock class.

        Args:
            num_occupants (int): Number of occupants the hammock can fit.
            material (str): Hammock material.
            setup_time (int): Setup time, minutes.
            weight (float): Weight of hammock ounces.
            length (int): Length of hammock feet (default: 11).
            seasons (int): Season rating (default: 3).
        """

        self.num_occupants = num_occupants
        self.material = material
        self.setup_time = setup_time
        self.weight = weight
        self.length = length
        self.seasons = seasons

    def __str__(self):

        """
        Returns a string representation of a Hammock.
        """

        return (
            f"Hammock(Occupants: {self.num_occupants}, Material: {self.material}, "
            f"Setup Time: {self.setup_time} mins, Weight: {self.weight} oz, "
            f"Length: {self.length} ft, Seasons: {self.seasons})")

    def __repr__(self):

        """
        Returns a developer-friendly string representation of the Hammock.
        """

        return (
            f"Hammock(num_occupants={self.num_occupants}, material='{self.material}', "
            f"setup_time={self.setup_time}, weight={self.weight}, length={self.length}, "
            f"seasons={self.seasons})")

    def __lt__(self, other: 'Hammock') -> bool:

        """
        Compares hammocks based on weight and setup time.

        Args:
            other (Hammock): The other hammock to compare.

        Returns:
            bool: True if both 'weight' and 'setup_time' of this hammock are strictly less than other hammock.
        """

        if not isinstance(other, Hammock):
            return NotImplemented

        return self.weight < other.weight and self.setup_time < other.setup_time

    def is_better(self, other: 'Hammock') -> bool:

        """
        Determines if this hammock is "better" than another.

        A hammock is considered better if its weight and setup_time are less than another hammock,
        while having an equal or better season rating.

        Args:
            other (Hammock): The other hammock to compare with.

        Returns:
            bool: True if this hammock is better; False otherwise.
        """

        if not isinstance(other, Hammock):
            return NotImplemented

        return (
                self.weight < other.weight and
                self.setup_time < other.setup_time and
                self.seasons >= other.seasons)


'''
Question 5:
'''


class Tarp:

    """
    Class representing a Tarp.

    Attributes:
        num_occupants (int): Number of occupants the tarp can accommodate.
        material (str): The material the tarp is made of.
        setup_time (int): Setup time in minutes.
        sqft (float): Square footage of the tarp.
        weight (float): Weight of the tarp in ounces.
        seasons (int): Season rating (3 or 4, default: 3).
    Methods:
        Methods:
----------------------------------------
__str__: Returns a user string representation of Tarp.
__repr__: Returns a developer string representation of Tarp.
__lt__: Compares two Tarps based on `num_occupants` and `sqft`.
is_better: Determines if this Tarp is "better" than another depending on weight, setup time, and season rating.
    """

    def __init__(
            self,
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
            material (str): The material the tarp is made of.
            setup_time (int): Setup time in minutes.
            sqft (float): Square footage of the tarp.
            weight (float): Weight of the tarp in ounces.
            seasons (int): Season rating (3 or 4, default: 3).
        """

        self.num_occupants = num_occupants
        self.material = material
        self.setup_time = setup_time
        self.sqft = sqft
        self.weight = weight
        self.seasons = seasons

    def __str__(self):

        """
        Returns a string representation of a Tarp.
        """

        return (
            f"Tarp(Occupants: {self.num_occupants}, Material: {self.material}, "
            f"Setup Time: {self.setup_time} mins, SqFt: {self.sqft}, "
            f"Weight: {self.weight} oz, Seasons: {self.seasons})")

    def __repr__(self):

        """
        Returns a developer-friendly string representation of the Tarp.
        """

        return (
            f"Tarp(num_occupants={self.num_occupants}, material='{self.material}', "
            f"setup_time={self.setup_time}, sqft={self.sqft}, weight={self.weight}, "
            f"seasons={self.seasons})")

    def __lt__(self, other: 'Tarp') -> bool:
        """
        Compares two tarps based on num_occupants and sqft.

        Args:
            other (Tarp): The other tarp to compare.

        Returns:
            bool: True if both 'num_occupants' and 'sqft' of this tarp are strictly less than other tarp.
        """
        if not isinstance(other, Tarp):
            return NotImplemented

        return self.num_occupants < other.num_occupants and self.sqft < other.sqft

    def is_better(self, other: 'Tarp') -> bool:

        """
        Determines if this tarp is "better" than another.

        Args:
            other (Tarp): The other tarp to compare.

        Returns:
            bool: True if this tarp is better; False otherwise.
        """

        if not isinstance(other, Tarp):
            return NotImplemented

        return (
                self.weight < other.weight and
                self.setup_time < other.setup_time and
                self.seasons >= other.seasons)


if __name__ == '__main__':
    # Set to False to remove output
    _set_print(True)

    _print('Question 1')

    names1 = ['matt', 'alice', 'tom', 'jake']
    names2 = ['jimmy', 'aaron', 'sam']

    nums1 = [1, 2, 90, 4]
    nums2 = [5, 6, 7, 8, 56]
    nums3 = [10, 3]

    _print(paired_list(names1, nums1))
    _print(paired_list(names1, nums2))
    _print(paired_list(names1, nums3))
    _print(paired_list(names2, nums1))
    _print(paired_list(names2, nums2))
    _print(paired_list(nums3, names2))

    _print('Question 2')

    paired = paired_list(names1, nums1)
    _print(even_odd_pairs(paired, even=True))  # filter for even nums
    _print(even_odd_pairs(paired, even=False))  # filter for odd nums

    paired = paired_list(names1, nums2)
    _print(even_odd_pairs(paired, even=True))
    _print(even_odd_pairs(paired, even=False))

    _print('Question 3')

    tent1 = Tent(num_occupants=4, material="polyester", setup_time=6, sqft=36, vestibule=False, weight=12.5,
                 structure_poles=True, seasons=3)
    tent2 = Tent(num_occupants=4, material="polyester", setup_time=5, sqft=35, vestibule=False, weight=11.5,
                 structure_poles=True, seasons=3)
    tent3 = Tent(num_occupants=3, material="polyester", setup_time=4, sqft=35, vestibule=False, weight=11.0,
                 structure_poles=True, seasons=4)

    _print(tent1 < tent2)  # False
    _print(tent1 < tent3)  # False
    _print(tent3 < tent1)  # True
    _print(tent3 < tent2)  # False

    _print(tent2.is_better(tent1))  # True
    _print(tent3.is_better(tent1))  # True
    _print(tent1.is_better(tent2))  # False

    _print('Question 4')

    hammock1 = Hammock(num_occupants=2, material="nylon", setup_time=3, weight=10.0)
    hammock2 = Hammock(num_occupants=1, material="nylon", setup_time=2, weight=8.0, length=9, seasons=4)
    hammock3 = Hammock(num_occupants=2, material="cotton", setup_time=4, weight=12.0, length=12)

    _print(hammock1 < hammock2)  # False
    _print(hammock2 < hammock1)  # True
    _print(hammock3 < hammock1)  # False

    _print(hammock2.is_better(hammock1))  # True
    _print(hammock1.is_better(hammock3))  # True
    _print(hammock3.is_better(hammock2))  # False

    _print('Question 5')

    tarp1 = Tarp(num_occupants=4, material="nylon", setup_time=8, sqft=60.0, weight=20.0, seasons=3)
    tarp2 = Tarp(num_occupants=2, material="canvas", setup_time=7, sqft=50.0, weight=15.0, seasons=4)
    tarp3 = Tarp(num_occupants=1, material="polyester", setup_time=6, sqft=30.0, weight=10.0)

    _print(tarp1 < tarp2)  # False
    _print(tarp2 < tarp1)  # True
    _print(tarp3 < tarp2)  # True

    _print(tarp2.is_better(tarp1))  # True
    _print(tarp3.is_better(tarp2))  # False
    _print(tarp1.is_better(tarp3))  # False
