# Given a year, determine whether it is a leap year.
# If it is a leap year, return the Boolean True, otherwise return False.

# Constraints: 1900 <= year <= 10^5


def is_leap(year):
    """ Return True if year is leap, otherwise return False

    >>> is_leap(2000)
    True
    >>> is_leap(2100)
    False
    >>> is_leap(2016)
    True
    >>> is_leap(2015)
    False
    >>> is_leap(1899)
    Traceback (most recent call last):
        ...
    ValueError: year must be >= 1900 and <= 10^5
    >>> is_leap(10**5 + 1)
    Traceback (most recent call last):
        ...
    ValueError: year must be >= 1900 and <= 10^5
    """

    if 1900 <= year <= 10**5:
        return year % 400 == 0 or year % 4 == 0 and year % 100 != 0
    else:
        raise ValueError("year must be >= 1900 and <= 10^5")


if __name__ == "__main__":
    import doctest
    doctest.testmod()
