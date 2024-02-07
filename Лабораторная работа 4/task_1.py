import math
from abc import ABC, abstractmethod


class Point(ABC):
    """Abstract point class"""

    def __init__(self, label: str):
        """
        The usual constructor of an abstract class that initializes label
        :param label: point label
        """
        self._label = None
        self.label = label

    @property
    def label(self) -> str:
        """
        Get the label of the point
        :return: label of point
        """
        return self._label

    @label.setter
    def label(self, label: str) -> None:
        """
        Set the label of the point.
        :param label: the new label for the point
        :return: None
        :raise TypeError: if label is not a string.
        :raise ValueError: if label is an empty string.
        """
        if not isinstance(label, str):
            raise TypeError(f'Invalid type for the pages argument: {type(label)}, required type: str')
        if len(label.strip()) == 0:
            raise ValueError("The label of the point is incorrect, it cannot be empty")
        self._label = label.strip()

    def __str__(self) -> str:
        """
        Getting a string representation of a point with a label field
        :return: string representation
        """
        return f'Point "{self._label}"'

    @abstractmethod
    def calculate_distance(self, another_point: 'Point') -> float:
        """
        A method for calculating the distance between points
        :param another_point: the point to which the distance needs to be calculated
        :return: distance
        """
        ...

    @abstractmethod
    def get_coordinate_system_name(self) -> str:
        """
        A method that returns the name of the coordinate system in which the point exists
        :return: the name of the coordinate system
        """
        ...

    def add_coordinate_system_name_to_label(self) -> str:
        """
        The method that transforms the label adds the name of the coordinate system to the beginning
        :return: converted label
        """
        self._label = f'{self.get_coordinate_system_name()}, {self._label}'
        return self._label


class CartesianPlanePoint(Point):
    """ A point in the Cartesian coordinate system on the plane"""

    def __init__(self, label: str, x: (float, int), y: (float, int)):
        """
        The usual constructor of a CartesianPlanePoint class that initializes label, x, y
        :param label: point label
        :param x: the coordinate on the abscissa axis
        :param y: the coordinate on the ordinate axis
        """
        super().__init__(label)
        self._x = None
        self._y = None
        self.x = x
        self.y = y

    @property
    def x(self) -> (float, int):
        """
        Get the coordinate on the abscissa axis of point
        :return: the coordinate on the abscissa axis of point
        """
        return self._x

    @property
    def y(self) -> (float, int):
        """
        Get the coordinate on the ordinate axis of point
        :return: the coordinate on the ordinate axis of point
        """
        return self._y

    @x.setter
    def x(self, x: float) -> None:
        """
        Set the coordinate on the abscissa axis of point
        :param x: the coordinate on the abscissa axis of point
        :return: None
        :raise TypeError if coordinate on the abscissa axis is not a float or int.
        """
        if not isinstance(x, (float, int)):
            raise TypeError(f'Invalid type for the x argument: {type(x)}, required types: float, int')
        self._x = x

    @y.setter
    def y(self, y: float) -> None:
        """
        Set the coordinate on the ordinate axis of point
        :param y: the coordinate on the ordinate axis of point
        :return: None
        :raise TypeError if coordinate on the ordinate axis is not a float or int.
        """
        if not isinstance(y, (float, int)):
            raise TypeError(f'Invalid type for the y argument: {type(y)}, required types: float, int')
        self._y = y

    def calculate_distance(self, another_point: 'CartesianPlanePoint') -> float:
        """
        A method for calculating the distance between points
        :param another_point: the point to which the distance needs to be calculated
        :return: distance
        :raise TypeError if another point is not a CartesianPlanePoint
        Реализация абстрактного метода
        """
        if not isinstance(another_point, CartesianPlanePoint):
            raise TypeError(
                f'Invalid type for the another_point argument: {type(another_point)},'
                f' required type: CartesianPlanePoint')
        return math.sqrt((self._y - another_point._y) ** 2 + (self._x - another_point._x) ** 2)

    def get_coordinate_system_name(self) -> str:
        """
        A method that returns the name of the coordinate system in which the point exists
        :return: the name of the coordinate system
        Реализация абстрактного метода
        """
        return "Cartesian on the plane"

    def __str__(self) -> str:
        """
        Getting a string representation of a point with a label, x, y fields
        :return: string representation
        """
        return f'{super().__str__()}, x = {self._x}, y = {self._y}'

    def __repr__(self) -> str:
        """
        Getting a string to create the same point object
        :return: string to create the same point object
        """
        return f"{self.__class__.__name__}(label={self._label!r}, x={self._x}, y={self._y})"


class PolarPoint(Point):
    """ A point in the Polar coordinate system on the plane"""

    def __init__(self, label: str, r: (float, int), phi: (float, int)):
        """
        The usual constructor of a PolarPoint class that initializes label, r, phi
        :param label: point label
        :param r: the radius of point
        :param phi: the phi angle of point
        """
        super().__init__(label)
        self._r = None
        self._phi = None
        self.r = r
        self.phi = phi

    @property
    def r(self) -> (float, int):
        """
        Get the radius coordinate of point
        :return: the radius coordinate of point
        """
        return self._r

    @property
    def phi(self) -> (float, int):
        """
        Get the phi angle coordinate of point
        :return: the phi angle coordinate of point
        """
        return self._phi

    @r.setter
    def r(self, r: float) -> None:
        """
        Set the radius of point coordinate
        :param r: the radius coordinate of point
        :return: None
        :raise TypeError if radius coordinate is not a float or int
        :raise ValueError if radius value a negative number
        """
        if not isinstance(r, (float, int)):
            raise TypeError(f'Invalid type for the radius argument: {type(r)}, required types: float, int')
        if r < 0:
            raise ValueError('The value of the radius is incorrect, it must be a non-negative number')
        self._r = r

    @phi.setter
    def phi(self, phi: float) -> None:
        """
        Set the phi angle of point coordinate
        :param phi: the phi angle coordinate of point
        :return: None
        :raise TypeError if phi angle coordinate is not a float or int
        :raise ValueError if phi angle value not between -pi and pi
        """
        if not isinstance(phi, (float, int)):
            raise TypeError(f'Invalid data type for the phi angle argument: {type(phi)}, required types: float, int')
        if not (-math.pi < phi <= math.pi):
            raise ValueError('The value of the phi angle in radians is incorrect, it must be between -pi and pi')
        self._phi = phi

    def calculate_distance(self, another_point: 'PolarPoint') -> float:
        """
        A method for calculating the distance between points
        :param another_point: the point to which the distance needs to be calculated
        :return: distance
        :raise TypeError if another point is not a PolarPoint
        Реализация абстрактного метода
        """
        if not isinstance(another_point, PolarPoint):
            raise TypeError(
                f'Invalid type for the another_point argument: {type(another_point)}, required type: PolarPoint')
        return math.sqrt((self._r * math.cos(self._phi) - another_point._r * math.cos(another_point._phi)) ** 2 +
                         (self._r * math.sin(self._phi) - another_point._r * math.sin(another_point._phi)) ** 2)

    def get_coordinate_system_name(self) -> str:
        """
        A method that returns the name of the coordinate system in which the point exists
        :return: the name of the coordinate system
        Реализация абстрактного метода
        """
        return "Polar"

    def __str__(self) -> str:
        """
        Getting a string representation of a point with a label, radius, phi angle fields
        :return: string representation
        """
        return f'{super().__str__()}, radius = {self._r}, phi = {self._phi} rad'

    def __repr__(self) -> str:
        """
        Getting a string to create the same point object
        :return: string to create the same point object
        """
        return f"{self.__class__.__name__}(label={self._label!r}, r={self._r}, phi={self._phi})"


class CartesianSpacePoint(CartesianPlanePoint):
    """ A point in the Cartesian coordinate system in space"""

    def __init__(self, label: str, x: (float, int), y: (float, int), z: (float, int)):
        """
        The usual constructor of a CartesianSpacePoint class that initializes label, x, y, z
        :param label: point label
        :param x: the coordinate on the abscissa axis
        :param y: the coordinate on the ordinate axis
        :param z: the coordinate on the z axis
        """
        super().__init__(label, x, y)
        self._z = None
        self.z = z

    @property
    def z(self) -> (float, int):
        """
        Get the coordinate on the z axis of point
        :return: the coordinate on the z axis of point
        """
        return self._z

    @z.setter
    def z(self, z: float) -> None:
        """
        Set the coordinate on the z axis of point
        :param z: the coordinate on the z axis of point
        :return: None
        :raise TypeError if coordinate on the z axis is not a float or int.
        """
        if not isinstance(z, (float, int)):
            raise TypeError(f'Invalid type for the z argument: {type(z)}, required types: float, int')
        self._z = z

    def calculate_distance(self, another_point: 'CartesianSpacePoint') -> float:
        """
        A method for calculating the distance between points
        :param another_point: the point to which the distance needs to be calculated
        :return: distance
        :raise TypeError if another point is not a CartesianSpacePoint
        Перегрузка необходима, тк формула нахождения расстояния точки в пространстве отличается
        """
        if not isinstance(another_point, CartesianPlanePoint):
            raise TypeError(
                f'Invalid type for the another_point argument: {type(another_point)},'
                f' required type: CartesianSpacePoint')
        return math.sqrt(
            (self._y - another_point._y) ** 2 + (self._x - another_point._x) ** 2 + (self._z - another_point._z))

    def get_coordinate_system_name(self) -> str:
        """
        A method that returns the name of the coordinate system in which the point exists
        :return: the name of the coordinate system
        Перегрузка необходима, тк система координат имеет отличное имя
        """
        return "Cartesian in space"

    def __str__(self) -> str:
        """
        Getting a string representation of a point with a label, x, y, z fields
        :return: string representation
        """
        return f'{super().__str__()}, z = {self._z}'

    def __repr__(self) -> str:
        """
        Getting a string to create the same point object
        :return: string to create the same point object
        """
        return f"{self.__class__.__name__}(label={self._label!r}, x={self._x}, y={self._y}, z={self._z})"


class CylindricalPoint(PolarPoint):
    """ A point in the Cylindrical coordinate system in space"""

    def __init__(self, label: str, r: (float, int), phi: (float, int), z: (float, int)):
        """
        The usual constructor of a CylindricalPoint class that initializes label, r, phi, z
        :param label: point label
        :param r: the radius of point
        :param phi: the phi angle of point
        :param z: the coordinate on the z axis
        """
        super().__init__(label, r, phi)
        self._z = None
        self.z = z

    @property
    def z(self) -> (float, int):
        """
        Get the coordinate on the z axis of point
        :return: the coordinate on the z axis of point
        """
        return self._z

    @z.setter
    def z(self, z: float) -> None:
        """
        Set the coordinate on the z axis of point
        :param z: the coordinate on the z axis of point
        :return: None
        :raise TypeError if coordinate on the z axis is not a float or int.
        """
        if not isinstance(z, (float, int)):
            raise TypeError(f'Invalid type for the z argument: {type(z)}, required types: float, int')
        self._z = z

    def calculate_distance(self, another_point: 'CylindricalPoint') -> float:
        """
        A method for calculating the distance between points
        :param another_point: the point to which the distance needs to be calculated
        :return: distance
        :raise TypeError if another point is not a CylindricalPoint
        Перегрузка необходима, тк формула нахождения расстояния точки в пространстве отличается
        """
        if not isinstance(another_point, CylindricalPoint):
            raise TypeError(
                f'Invalid type for the another_point argument: {type(another_point)},'
                f' required type: CylindricalPoint')
        return math.sqrt((self._r * math.cos(self._phi) - another_point._r * math.cos(another_point._phi)) ** 2 +
                         (self._r * math.sin(self._phi) - another_point._r * math.sin(another_point._phi)) ** 2 +
                         (self._z - another_point._z) ** 2)

    def get_coordinate_system_name(self) -> str:
        """
        A method that returns the name of the coordinate system in which the point exists
        :return: the name of the coordinate system
        Перегрузка необходима, тк система координат имеет отличное имя
        """
        return "Cylindrical"

    def __str__(self) -> str:
        """
        Getting a string representation of a point with a label, radius, phi angle, z fields
        :return: string representation
        """
        return f'{super().__str__()}, z = {self._z}'

    def __repr__(self) -> str:
        """
        Getting a string to create the same point object
        :return: string to create the same point object
        """
        return f"{self.__class__.__name__}(label={self._label!r}, r={self._r}, phi={self._phi}, z={self._z})"
