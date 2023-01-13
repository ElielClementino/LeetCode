# https://leetcode.com/problems/integer-to-roman/
num = 58
numero = []
tabela = {
    "M": 1000,
    "CM": 900,
    "D": 500,
    "CD": 400, 
    "C": 100,
    "XC": 90,
    "L": 50,
    "XL": 40,
    "X": 10,
    "IX": 9, 
    "V": 5,
    "IV": 4,
    "I": 1
}


def intToRoman(num: int) -> str:
    for i in tabela:
        quociente = num // tabela[i]
        resto = num % tabela[i]
        num = resto
        numero.append(i * quociente)
    return ''.join(numero)

roman = intToRoman(num)
print(roman)
