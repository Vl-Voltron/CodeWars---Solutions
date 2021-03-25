""" Love vs friendship
Task Overview:

If　a = 1, b = 2, c = 3 ... z = 26

Then l + o + v + e = 54

and f + r + i + e + n + d + s + h + i + p = 108

So friendship is twice stronger than love :-)

The input will always be in lowercase and never be empty.

Tags: FUNDAMENTALS
https://www.codewars.com/kata/59706036f6e5d1e22d000016/train/python
"""

#############################################################
#                        MY SOLUTIONS                       #
#############################################################

def words_to_marks(s):
    numbers = []
    for letter in s:
        number = ord(letter) - 96
        numbers.append(number)
    return sum(numbers)
