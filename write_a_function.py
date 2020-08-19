"""
Write a function.

Given a year, determine whether it is a leap year.
If it is a leap year, return the Boolean True, otherwise return False.

three conditions are used to identify a leap year:

- the year can be evenly divided by 4
- the year can be evenly divided by 100
- The year is also evenly divisible by 400

E.g., 2000 and 2400 are leap years
"""


def leap_year_checker(year):
    """
    Check if year meets all three requirement to be a leap year.
    """

    year_bool = bool(year % 4 == 0)
    print(year_bool)

    if year_bool is True:
        year_bool = bool(year % 10 == 0)
        print(year_bool)

        if year_bool is True:
            year_bool = bool(year % 400 == 0)
            return year_bool

    else:
        return year_bool


YEAR = 1900
LEAP_TF = leap_year_checker(YEAR)
print(LEAP_TF)
