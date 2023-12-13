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
from functions import falling_distance
# Constants


falling_time = float(input("Enter the time the object has fallen (in seconds): "))
distance = falling_distance(falling_time)
print(distance)
