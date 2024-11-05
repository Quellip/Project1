from typing import Union


def circle_area(r: Union[int, float]) -> float:
    """ Фунцкия вычисления площади круга """
    PI = 3.14
    my_circle_area = PI * r ** 2
    return my_circle_area


def format_description(r: Union[int, float], area: float) -> str:
    """ Функция вывода описания окружности """
    return f"Radius is {str(r)}; area is {str(round(area, 2))}"


def get_info(r: Union[int, float]) -> None:
    """ Функция вывода информации """
    area = circle_area(r)
    description = format_description(r, area)
    print(description)


radius = int(input("Enter circle radius (int): "))
get_info(radius)
