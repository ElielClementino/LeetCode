# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
from typing import List
candies = [12,1,12]
extra_candies = 10
def kidsWithCandies(candies: List[int], extraCandies: int) -> List[bool]:
    maior_numero_candies = 0
    boolean_array_of_candies = []
    for candy in candies:
        if int(candy) > maior_numero_candies:
            maior_numero_candies = int(candy)
    for greatest_number_of_candies in candies:
        if int(greatest_number_of_candies) + extraCandies >= maior_numero_candies:
            boolean_array_of_candies.append(True)
        else:
            boolean_array_of_candies.append(False)
    return boolean_array_of_candies

print(kidsWithCandies(candies, extra_candies))
