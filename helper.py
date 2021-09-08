from enum import Enum
import random


class CannotBreed(Exception):
    """
    Cannot breed pantheras of the same gender
    """
    pass


class Gender(Enum):
    FEMALE = ("FEMALE")
    MALE = ("MALE")

    def random():
        """
        Generate a random gender

        Returns:
            Gender: 
        """
        return random.choice([Gender.MALE, Gender.FEMALE])


name_dict = {
    Gender.MALE: {
        "Tiger" + "Tigress": "Tiger",
        "Tiger" + "Lioness": "Tigon",
        "Tiger" + "Jaguaress": "Tiguar",
        "Tiger" + "Leopardess": "Tigard",

        "Lion" + "Tigress": "Liger",
        "Lion" + "Lioness": "Lion",
        "Lion" + "Jaguaress": "Liguar",
        "Lion" + "Leopardess": "Lipard",

        "Jaguar" + "Tigress": "Jagger",
        "Jaguar" + "Lioness": "Jaglion",
        "Jaguar" + "Jaguaress": "Jaguar",
        "Jaguar" + "Leopardess": "Jagupard",

        "Leopard" + "Tigress": "Leoger",
        "Leopard" + "Lioness": "Leopon",
        "Leopard" + "Jaguaress": "Leguar",
        "Leopard" + "Leopardess": "Leopard",
    },
    Gender.FEMALE: {
        "Tiger" + "Tigress": "Tigress",
        "Tiger" + "Lioness": "Tigoness",
        "Tiger" + "Jaguaress": "Tiguaress",
        "Tiger" + "Leopardess": "Tigardess",

        "Lion" + "Tigress": "Ligress",
        "Lion" + "Lioness": "Lioness",
        "Lion" + "Jaguaress": "Liguaress",
        "Lion" + "Leopardess": "Lipardess",

        "Jaguar" + "Tigress": "Jaggress",
        "Jaguar" + "Lioness": "Jaglioness",
        "Jaguar" + "Jaguaress": "Jaguaress",
        "Jaguar" + "Leopardess": "Jagupardess",

        "Leopard" + "Tigress": "Leogress",
        "Leopard" + "Lioness": "Leoponess",
        "Leopard" + "Jaguaress": "Leguaress",
        "Leopard" + "Leopardess": "Leopardess",
    }
}


def get_parent(a, b):
    """
    Determine the male and female parent, given two instance of panthera.

    Args:
        a (Panthera): 
        b (Panthera): 

    Returns:
        Tuple(Panthera, Panthera): Tuple of male and female parent
    """
    if a.sire == None and b.sire == None:
        return (a, b) if a.gender == Gender.MALE else (b, a)
    elif a.sire == None:
        if (a.gender == Gender.MALE):
            return (a, b.dam)
        else:
            return (b.sire, a)
    elif b.sire == None:
        if (a.gender == Gender.MALE):
            return (a.dam, b)
        else:
            return (b, a.sire)
    else:
        if (a.gender == Gender.MALE):
            return (a.sire, b.dam)
        else:
            return (b.sire, a.dam)


def get_new_generation(a, b):
    if a.gender == Gender.FEMALE:
        return a.generation + 1
    return b.generation + 1


def copulate(sire, dam):
    """
    Breeds two instance of panthera

    Args:
        sire (Panthera): male parent
        dam (Panthera): female parent

    Returns:
        Tuple(string, string): Tuple of new name and gender
    """
    new_gender = Gender.random()
    new_name = ""
    if sire.name == "Tiger":
        new_name = "Tig"
    elif sire.name == "Lion":
        new_name = "Li"
    elif sire.name == "Jaguar":
        new_name = "Jag"
    elif sire.name == "Leopard":
        new_name = "Leo"

    if dam.name == "Tigress":
        if not sire.name == "Tiger":
            new_name += "g"
        if (new_gender == Gender.FEMALE):
            new_name += "r"
        else:
            new_name += "er"
    elif dam.name == "Lioness":
        if sire.name == "Leopard":
            new_name += "pon"
        elif sire.name == "Jaguar":
            new_name += "lion"
        else:
            new_name += "on"
    elif dam.name == "Jaguaress":
        if sire.name == "Leopard":
            new_name = new_name[0:-1] + "guar"
        elif sire.name == "Lion":
            new_name += "guar"
        else:
            new_name += "uar"
    elif dam.name == "Leopardess":
        if sire.name in ["Leopard", "Lion"]:
            new_name += "pard"
        elif sire.name == "Jaguar":
            new_name += "upard"
        else:
            new_name += "ard"

    if new_gender == Gender.FEMALE:
        new_name += "ess"
    return (new_name, new_gender)
