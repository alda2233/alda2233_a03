"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Mohamed
ID:      169072233
Email:   alda2233@mylaurier.ca
__updated__ = "2023-10-20"
-------------------------------------------------------
"""
# Imports
from functions import footage_to_acres
# Constants

square_feet = float(input("squarefeet: "))
acres = footage_to_acres(square_feet)
print(acres)
