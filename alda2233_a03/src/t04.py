"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Mohamed
ID:      169072233
Email:   alda2233@mylaurier.ca
__updated__ = "2023-10-21"
-------------------------------------------------------
"""
# Imports
from functions import multiply_fractions
# Constants

num1 = int(input("Enter the numerator of the first fraction: "))
den1 = int(input("Enter the denominator of the first fraction: "))
num2 = int(input("Enter the numerator of the second fraction: "))
den2 = int(input("Enter the denominator of the second fraction: "))


num, den, product = multiply_fractions(num1, den1, num2, den2)
print(num, den, product)
