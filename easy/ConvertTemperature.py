# https://leetcode.com/problems/convert-the-temperature/description/
from typing import List
celsius = 36.50
def convertTemperature(celsius: float) -> List[float]:
    kelvin = celsius + 273.15
    fahrenheit = celsius * 1.80 + 32.00
    return [kelvin, fahrenheit]

print(convertTemperature(celsius))