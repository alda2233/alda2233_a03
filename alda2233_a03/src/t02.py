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
from functions import lawn_mow_time
# Constants

width = float(input("Enter the width of the lawn (in meters): "))
length = float(input("Enter the length of the lawn (in meters): "))
speed = float(input("Enter the mowing speed (square meters cut per minute): "))

time_required = lawn_mow_time(width, length, speed)
print(f"{time_required:.1f}")
