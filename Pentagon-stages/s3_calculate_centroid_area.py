import math
from dataclasses import dataclass
from enum import Enum


class Gas(Enum):
    C2H2 = "C2H2"
    H2 = "H2"
    C2H6 = "C2H6"
    CH4 = "CH4"
    C2H4 = "C2H4"


@dataclass
class Coordinates:
    x: float
    y: float

# cálculo da área do poligono baseado nas cooordenadas de cada vértice
def calcuate_polygon_area(gases_coords: list[Coordinates]) -> float:
    sum = 0

    gases_coords.append(gases_coords[0])

    for i in range(len(gases_coords) - 1):
        current_coords = gases_coords[i]
        next_coords = gases_coords[i + 1]

        sum += current_coords.x * next_coords.y - next_coords.x * current_coords.y

    return sum / 2

# cálculo da centroide do poligonos
def calculate_polygon_centroid_coords(
    gases_coords: list[Coordinates], area: float
) -> Coordinates:
    x_sum = 0
    y_sum = 0

    gases_coords.append(gases_coords[0])

    for i in range(len(gases_coords) - 1):
        current_coords = gases_coords[i]
        next_coords = gases_coords[i + 1]

        x_sum += (current_coords.x + next_coords.x) * (
            current_coords.x * next_coords.y - next_coords.x * current_coords.y
        )

        y_sum += (current_coords.y + next_coords.y) * (
            current_coords.x * next_coords.y - next_coords.x * current_coords.y
        )

    x = x_sum / (6 * area)
    y = y_sum / (6 * area)

    return Coordinates(x, y)

if __name__ == "__main__":
    pass
