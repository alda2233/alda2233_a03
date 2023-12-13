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
from functions import extract_date
# Constants

date_number = int(input("Enter a date number (YYYYMMDD): "))
year, month, day = extract_date(date_number)
print(f"{year}, {month}, {day}")
