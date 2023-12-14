from typing import Union
import doctest


def check_correct_positive_number(number: Union[int, float]) -> None:
    """
    The function that checks the input data.
    If the input object is not a number or not a positive number, an error is caused

    :param number: The value to check
    :return: None

    Examples:
    >>> check_correct_positive_number(1)
    >>> check_correct_positive_number("1")
    Traceback (most recent call last):
    ...
    TypeError: Sorry, value must be number
    >>> check_correct_positive_number(0)
    Traceback (most recent call last):
    ...
    ValueError: Sorry, number must be positive
    """
    if not isinstance(number, (int, float)):
        raise TypeError("Sorry, value must be number")
    if number <= 0:
        raise ValueError("Sorry, number must be positive")


class Fridge:
    """
    A fridge with information about the country of origin,
    the volume contained, the volume occupied
    """

    def __init__(self, manufacturing_country: str, capacity_volume: Union[int, float],
                 occupied_volume: Union[int, float]):
        """
        The usual constructor of the fridge object
        :param manufacturing_country: The string containing the name of the manufacturer's country
        :param capacity_volume: The number indicating the capacity of the fridge
        :param occupied_volume: The number indicating the occupied volume of the fridge

        Examples:
        >>> fridge = Fridge("Russia", 100, 10)
        >>> fridge1 = Fridge("1Russia",100,10)
        Traceback (most recent call last):
        ...
        ValueError: Sorry, country name must contain only letters
        >>> fridge2 = Fridge("Russia", 0, 0)
        Traceback (most recent call last):
        ...
        ValueError: Sorry, capacity_volume must be positive number
        >>> fridge3 = Fridge("Russia", 1, 2)
        Traceback (most recent call last):
        ...
        ValueError: Sorry, occupied_volume can't be more than capacity_volume
        """
        self.manufacturing_county = None
        self.init_manufacturing_country(manufacturing_country)

        self.capacity_volume = None
        self.init_capacity_volume(capacity_volume)

        self.occupied_volume = None
        self.init_occupied_volume(occupied_volume)

    def init_manufacturing_country(self, country: str) -> None:
        """
        The method initializing the country of origin attribute
        :param country: A string containing the name of the manufacturer's country
        :return: None

        Examples:
        >>> fridge = Fridge("Russia", 100, 1)
        >>> fridge.init_manufacturing_country("USSR")
        >>> print(fridge.manufacturing_county)
        USSR
        """
        if not isinstance(country, str):
            raise TypeError("Sorry, country must be string")
        country = country.strip()
        if country == "":
            raise ValueError("Sorry, country value can't be empty")
        if len([x for x in country if not x.isalpha()]) != 0:
            raise ValueError("Sorry, country name must contain only letters")
        self.manufacturing_county = country

    def init_capacity_volume(self, capacity_volume: Union[int, float]) -> None:
        """
        The method initializing the fridge capacity attribute
        :param capacity_volume: A number indicating the capacity of the fridge
        :return: None

        Examples:
        >>> fridge = Fridge("Russia", 100, 1)
        >>> fridge.init_capacity_volume(200)
        >>> print(fridge.capacity_volume)
        200
        """
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError("Sorry, incorrect capacity_volume value type" + str(type(capacity_volume)))
        if capacity_volume <= 0:
            raise ValueError("Sorry, capacity_volume must be positive number")
        self.capacity_volume = capacity_volume

    def init_occupied_volume(self, occupied_volume: Union[int, float]) -> None:
        """
        The method initializing the filled fridge volume attribute
        :param occupied_volume: A number indicating the occupied volume of the fridge
        :return: None

        Examples:
        >>> fridge = Fridge("Russia", 100, 1)
        >>> fridge.init_occupied_volume(50)
        >>> print(fridge.occupied_volume)
        50
        """
        if not isinstance(occupied_volume, (int, float)):
            raise TypeError("Sorry, incorrect occupied_volume value type")
        if occupied_volume < 0:
            raise ValueError("Sorry, occupied_volume must be non-negative number")
        if occupied_volume > self.capacity_volume:
            raise ValueError("Sorry, occupied_volume can't be more than capacity_volume")
        self.occupied_volume = occupied_volume

    def put_item(self, occupied_volume_by_item: Union[int, float]) -> bool:
        """
        The method that allows you to put an object of some volume in the fridge
        :param occupied_volume_by_item: The volume of the item that is planned to be put in the fridge
        :return: True if the item fits into the fridge and has been placed, otherwise false

        Examples:
        >>> fridge = Fridge("Russia", 100, 1)
        >>> fridge.put_item(10)
        True
        """
        check_correct_positive_number(occupied_volume_by_item)
        if occupied_volume_by_item + self.occupied_volume > self.capacity_volume:
            return False
        self.occupied_volume += occupied_volume_by_item
        return True

    def remove_item(self, occupied_volume_by_item: Union[int, float]) -> bool:
        """
        The method that allows you to remove an object of a certain volume from the refrigerator
        :param occupied_volume_by_item: The volume of the product that is planned to be taken out in the fridge
        :return: True if there is so much occupied volume in the fridge,
         and it turned out to be withdrawn, otherwise false
        Examples:
        >>> fridge = Fridge("Russia", 100, 20)
        >>> fridge.remove_item(10)
        True
        """
        check_correct_positive_number(occupied_volume_by_item)
        if occupied_volume_by_item > self.occupied_volume:
            return False
        self.occupied_volume -= occupied_volume_by_item
        return True


class Dish:
    """
    A dish containing information about the name,
    weight in grams, number of calories and price
     """

    def __init__(self, name: str, grams: Union[int, float],
                 kcal: Union[int, float], price: Union[int, float]):
        """
        The usual constructor of the dish object
        :param name: The string containing the name of the dish
        :param grams: The number indicating the weight of the dish
        :param kcal: The number indicating the energy value of the dish
        :param price: The number indicating the price of the dish

        Examples:
        >>> dish = Dish("Borsch", 300, 200, 100)
        >>> dish1 = Dish("Borsch123",300 ,200,100)
        Traceback (most recent call last):
        ...
        ValueError: Sorry, symbol in string isn't alpha
        >>> dish2 = Dish("Borsch", 0, 0 ,0)
        Traceback (most recent call last):
        ...
        ValueError: Sorry, number must be positive
        """
        self.name = None
        self.init_name(name)

        check_correct_positive_number(grams)
        self.grams = grams

        check_correct_positive_number(kcal)
        self.kcal = kcal

        check_correct_positive_number(price)
        self.price = price

    def init_name(self, name: str) -> None:
        """
        The method that initializes the name of the dish
        :param name: The string containing the name of the dish
        :return: None

        Examples:
        >>> dish = Dish("Borsch", 300, 200, 100)
        >>> dish.init_name("new Borsch")
        >>> print(dish.name)
        new Borsch
        """
        if not isinstance(name, str):
            raise TypeError("Sorry, value must be string")
        name = name.strip()
        if name == "":
            raise ValueError("Sorry, string can't be empty")
        if len([x for x in name if not x.isalpha() and not x.isspace()]) != 0:
            raise ValueError("Sorry, symbol in string isn't alpha")
        self.name = name

    def raise_price_by(self, add: Union[int, float]) -> Union[int, float]:
        """
        The method to increase the price of a dish
        :param add: The number by which the price should be increased
        :return: New price

        Examples:
        >>> dish = Dish("Borsch", 300, 200, 100)
        >>> dish.raise_price_by(333)
        433
        """
        check_correct_positive_number(add)
        self.price += add
        return self.price

    def reduce_price_by(self, minus: Union[int, float]) -> Union[int, float]:
        """
        The method to reduce the price of a dish
        :param minus: The number by which the price should be reduced
        :return: New price

        Examples:
        >>> dish = Dish("Borsch", 300, 200, 100)
        >>> dish.reduce_price_by(10)
        90
        """
        check_correct_positive_number(minus)
        try:
            check_correct_positive_number(self.price - minus)
        except ValueError:
            raise ValueError(f"Sorry, it is incorrect to reduce the price by {minus},"
                             f" new price {self.price - minus} is incorrect")
        self.price -= minus
        return self.price


class Bed:
    """
    A bed containing information about the number of sleeping places,
    the number of floors, the presence of walls
    """

    def __init__(self, number_of_sleeping_places: int, number_of_floors: int, there_are_bumpers: bool):
        """
        The usual constructor of the bed object
        :param number_of_sleeping_places: The number indicating the number of sleeping places
        :param number_of_floors: The number indicating the number of floors
        :param there_are_bumpers: The boolean value indicating the presence of walls

        Examples:
        >>> bed = Bed(1, 1, False)
        >>> bed2 = Bed(1, 1, 1)
        Traceback (most recent call last):
        ...
        TypeError: the variable there_are_bumpers must be of type boolean
        >>> bed3 = Bed(0, 1, False)
        Traceback (most recent call last):
        ...
        ValueError: Sorry, number must be positive
        """
        check_correct_positive_number(number_of_sleeping_places)
        self.number_of_sleeping_places = number_of_sleeping_places
        check_correct_positive_number(number_of_floors)
        self.number_of_floors = number_of_floors

        self.there_are_bumpers = None
        self.init_there_are_bumpers(there_are_bumpers)

    def init_there_are_bumpers(self, there_are_bumpers: bool) -> None:
        """
        The method that initializes the attribute of the presence of walls by the bed
        :param there_are_bumpers: The boolean value indicating the presence of walls
        :return: None

        Examples:
        >>> bed = Bed(1, 1, False)
        >>> bed.init_there_are_bumpers(True)
        >>> print(bed.there_are_bumpers)
        True
        """
        if not isinstance(there_are_bumpers, bool):
            raise TypeError("the variable there_are_bumpers must be of type boolean")
        self.there_are_bumpers = there_are_bumpers

    def to_string(self) -> str:
        """
        A method that forms a string representation of a bed object
        :return: The string representation of a bed object

        Examples:
        >>> bed = Bed(1, 1, False)
        >>> bed.to_string()
        'Bed with 1 sleeping place, 1 floor and without bumpers'
        """
        return f"Bed with {self.number_of_sleeping_places} sleeping place, " \
               f"{self.number_of_floors} floor and " \
               f"with{'' if self.there_are_bumpers else 'out'} bumpers"

    def add_floor(self, count: int) -> int:
        """
        The method for adding floors to a bed
        :param count: The number indicating the number of floors to add
        :return: New number of floors by the bed

        Examples:
        >>> bed = Bed(1, 1, False)
        >>> bed.add_floor(100)
        101
        """
        check_correct_positive_number(count)
        self.number_of_floors += count
        return self.number_of_floors

    def make_bed(self):
        """
        The method for making the bed

        Examples:
        >>> bed = Bed(1, 1, False)
        >>> bed.make_bed() # The bed was made up
        """
        ...

    def straighten_bed(self):
        """
        The method that allows you to straighten the bed

        Examples:
        >>> bed = Bed(1, 1, False)
        >>> bed.straighten_bed() # The bed became straightened
        """
        ...


if __name__ == "__main__":
    doctest.testmod()
