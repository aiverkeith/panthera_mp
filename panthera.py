from helper import CannotBreed
from helper import CannotBreed
from helper import copulate
from helper import Gender
from helper import get_new_generation
from helper import get_parent
from helper import name_dict
from helper import random

# Okay lang ba na ganito i expose si name_dict?


class Panthera:
    """
    Panthera Base Class
    """

    def __init__(self, name, gender, generation, sire=None, dam=None):
        """

        Args:
            name (String): Name of the panthera
            gender (Gender): Gender
            generation (int): generation
            sire (Panthera, optional): Male Parent. Defaults to None.
            dam (Panthera, optional): Female Parent. Defaults to None.
        """
        self.name = name
        self.gender = gender
        self.generation = generation
        self.sire = sire
        self.dam = dam

    def __repr__(self) -> str:
        """
        For print purpose
        """
        return self.__str__()

    def __str__(self) -> str:
        """
        For print purpose
        """
        return self.name

    def __lt__(self, other):
        """
        For sorting purposes
        """
        if self.generation == other.generation:
            return self.name < other.name
        else:
            return self.generation < other.generation

    def __gt__(self, other):
        """
        For sorting purposes
        """
        if self.generation == other.generation:
            return self.name > other.name
        else:
            return self.generation > other.generation

    def __add__(self, other):
        """
        Breeds two panthera instance
        """
        if self.gender == other.gender:
            raise CannotBreed
        [sire, dam] = get_parent(self, other)
        [new_name, new_gender] = copulate(sire, dam)
        new_generation = get_new_generation(self, other)
        return Panthera(
            new_name,
            new_gender,
            new_generation,
            sire,
            dam
        )

    def random_first_gen():
        """
        Returns:
            Panthera: a subclass of panthera
        """
        return random.choice([Tiger, Lion, Jaguar, Leopard])


class Tiger(Panthera):
    """
    1st generation Tiger with random gender.
    """
    base_name = {
        Gender.FEMALE: "Tigress",
        Gender.MALE: "Tiger",
    }

    def __init__(self, gender=Gender.random()):
        """
        Args:
            gender (Gender, optional): If you want to set the gender manually.
            Defaults to Gender.random().
        """
        super().__init__(Tiger.base_name[gender], gender, 1)


class Lion(Panthera):
    """
    1st generation Lion with random gender.
    """
    base_name = {
        Gender.FEMALE: "Lioness",
        Gender.MALE: "Lion",
    }

    def __init__(self, gender=Gender.random()):
        """
        Args:
            gender (Gender, optional): If you want to set the gender manually.
            Defaults to Gender.random().
        """
        super().__init__(Lion.base_name[gender], gender, 1)


class Jaguar(Panthera):
    """
    1st generation Jaguar with random gender.
    """
    base_name = {
        Gender.FEMALE: "Jaguaress",
        Gender.MALE: "Jaguar",
    }

    def __init__(self, gender=Gender.random()):
        """
        Args:
            gender (Gender, optional): If you want to set the gender manually.
            Defaults to Gender.random().
        """
        super().__init__(Jaguar.base_name[gender], gender, 1)


class Leopard(Panthera):
    """
    1st generation Leopard with random gender.
    """
    base_name = {
        Gender.FEMALE: "Leopardess",
        Gender.MALE: "Leopard",
    }

    def __init__(self, gender=Gender.random()):
        """
        Args:
            gender (Gender, optional): If you want to set the gender manually.
            Defaults to Gender.random().
        """
        super().__init__(Leopard.base_name[gender], gender, 1)
