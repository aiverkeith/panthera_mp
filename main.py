from helper import name_dict
from panthera import CannotBreed
from panthera import Gender
from panthera import Jaguar
from panthera import Leopard
from panthera import Lion
from panthera import Tiger


females = [
    Tiger(gender=Gender.FEMALE),
    Lion(gender=Gender.FEMALE),
    Jaguar(gender=Gender.FEMALE),
    Leopard(gender=Gender.FEMALE),
]
males = [
    Tiger(gender=Gender.MALE),
    Lion(gender=Gender.MALE),
    Jaguar(gender=Gender.MALE),
    Leopard(gender=Gender.MALE),
]


def assert_breed(a, b, male_name, female_name):
    c = a + b
    try:
        assert c.name == male_name
        print(f"{a.name} + {b.name} = {c.name}")
    except AssertionError:
        try:
            assert c.name == female_name
            print(f"{a.name} + {b.name} = {c.name}")
        except AssertionError:
            print(a, b, c)
            raise
    except CannotBreed:
        print(f"Cannot breed {a.name} and {b.name}")

    return c


def get_second_generation_breeds():
    _result = []
    for male in males:
        for female in females:
            child = assert_breed(
                male,
                female,
                name_dict[Gender.MALE][male.name + female.name],
                name_dict[Gender.FEMALE][male.name + female.name],
            )
            _result.append(child)
    return _result


def main():
    print("======================================")
    print("1st generation")
    print("======================================")
    [print(n) for n in males]
    [print(n) for n in females]

    print("======================================")
    print("Breeding 2nd generation")
    print("======================================")
    second_generations_group_a = get_second_generation_breeds()
    second_generations_group_b = get_second_generation_breeds()

    print("======================================")
    print("Breeding 3rd generation")
    print("======================================")
    third_generation = []
    for a in second_generations_group_a:
        for b in second_generations_group_b:
            try:
                print(f"Breeding {a.name} and {b.name}...")
                c = a + b
                print(f"Result is: {c} gen {c.generation}")
                third_generation.append(c)
            except CannotBreed:
                print(f"Cannot breed the same gender")

    [print(n) for n in third_generation]

    print("======================================")
    print("Sort")
    print("======================================")
    to_sort = [
        *third_generation,
        *females,
        *second_generations_group_a,
        *males
    ]
    to_sort.sort()
    [print(f"gen{n.generation} {n}") for n in to_sort]


if __name__ == '__main__':
    main()
