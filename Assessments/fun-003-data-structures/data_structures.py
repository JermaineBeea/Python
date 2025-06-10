import random

def generate_random_list(length):
    """Generate a list of random numbers of a given length"""
    return random.choices(range(1, 100), k = length)

def find_max(numbers):
    """Find the largest(maximum) number in a list of numbers"""
    return max(numbers)

def find_min(numbers):
    """Find the smallest(minimum) number in a list of numbers"""
    return min(numbers)

def find_average(numbers):
    """Find the average of a list of numbers int the list 'numbers' and return 
    it as a float to one decimal point"""
    return round(float(sum(numbers)/ len(numbers)),1)

def find_even_pairs(numbers):
    """Find the neigbouring pairs of numbers that sum up to an even number and 
    then return a list of tuples with the pairs' index numbers 
    ie: [1,3,5] returns [(0,1)]
    """
    list_indx = []
    for indx, next_indx in zip(range(0, len(numbers)), range(1, len(numbers))):
        if (numbers[indx] + numbers[next_indx]) % 2 == 0:
            list_indx.append((indx, next_indx))
    
    return list_indx
        

def find_odd_pairs(numbers):
    """Find the neigbouring pairs of numbers that sum up to an even number and 
    then return a list of tuples with the pairs' index numbers 
    ie: [1,3,5] returns [(1,2)]
    """
    list_indx = []
    for indx, next_indx in zip(range(0, len(numbers)), range(1, len(numbers))):
        if not (numbers[indx] + numbers[next_indx]) % 2 == 0:
            list_indx.append((indx, next_indx))
    
    return list_indx


def find_number_of_even_numbers(numbers):
    """Find the total number of even numbers in the list 'numbers' and return 
    the number as an integer"""
    return len(list(filter(lambda num: num % 2 == 0, numbers)))

def find_number_of_odd_numbers(numbers):
    """Find the total number of odd numbers in the list 'numbers' and return 
    the number as an integer"""
    return len(list(filter(lambda num: not num % 2 == 0, numbers)))

def find_even_numbers(numbers):
    """Find the even numbers in the list 'numbers' and return them in
    in a tuple"""
    return tuple(filter(lambda num: num % 2 == 0, numbers))
            
def find_odd_numbers(numbers):
    """Find the odd numbers in the list 'numbers' and return them in
    in a tuple"""
    return tuple(filter(lambda num: not num % 2 == 0, numbers))

def return_list_stats(numbers):
    """Given the list 'numbers', use the relevant functions to return a
        dictionary of statics for the list. This dictionary must have
        the following keys:
            unique_numbers : a set containing unique numbers from the list 'numbers',
            max : largest number in the list 'numbers',
            min : smallest number in the list 'numbers',
            average : average of the numbers in the list 'numbers',
            even_pairs : a list of tuples that have neighboring pairs 
                that sum up to an even number in the list 'numbers',
            odd_pairs : a list of tuples that have neighboring pairs 
                that sum up to an even number in the list 'numbers',
            even_numbers : a tuple of all the even numbers in the list
                'numbers',
            odd_numbers : a tuple of all the odd numbers in the list 
                'numbers',
            number_of_even_numbers : the total number of even numbers in the 
                list 'numbers',
            number_of_odd_numbers : the total number of even numbers in the list
                 'numbers'
    """
    stats = {
             "unique_numbers": set(numbers),
            "min": find_min(numbers),
            "max": find_max(numbers),
            "average": find_average(numbers),
            "even_pairs": find_even_pairs(numbers),
            "odd_pairs": find_odd_pairs(numbers),
            "even_numbers": find_even_numbers(numbers),
            "odd_numbers": find_odd_numbers(numbers),
            "number_of_even_numbers": find_number_of_even_numbers(numbers),
            "number_of_odd_numbers": find_number_of_odd_numbers(numbers)
        }

    return stats

if "__name__" == "__main__":
    pass