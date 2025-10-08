import re

def count_items(items):
    # TODO: Return the number of items in the list
    return len(items)

def sum_numbers(numbers):
    # TODO: Return the sum of all numbers in the list
    max = 0
    for i in numbers:
        max += i
    return max

def find_largest(numbers):
    # TODO: Return the largest number in the list
    return max(numbers)

def count_even_numbers(numbers):
    # TODO: Return the count of even numbers in the list
    count = 0
    for i in numbers:
        if i % 2 == 0:
            count += 1
    return count

def sum_digits(number):
    # TODO: Return the sum of digits in the given number
    number = str(number)
    list1 = []
    for i in number:
        list1.append(int(i))
    count = 0
    for i in list1:
        count += i
    return count

def count_vowels(string):
    # TODO: Return the count of vowels in the string (case-insensitive)
    # vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    v = r'[aeiouAEIOU\s]'
    count = 0
    for i in string:
        if i in v:
            count += 1
    return count

def multiply_list_elements(numbers):
    # TODO: Return the product of all elements in the list
    count = 1
    for i in numbers:
        count *= i
    return count
