import doctest

from fizz_buzz_basic import fizz_buzz

def fizz_buzz_list(num):
    """
    For numbers between 1 and num, add one of the following to the list
        - Fizz if number is divisible by 3 only
        - Buzz if number is divisible by 5 only
        - FizzBuzz if number is divisible by 3 and 5
        - number otherwise
    
    >>> fizz_buzz_list(4)
    ['FizzBuzz', 1, 2, 'Fizz', 4]
    >>> fizz_buzz_list(-1)
    []
    
    """
    fizz_buzzed_nums = []
    for n in range(num+1):
        fizz_buzzed_nums.append(fizz_buzz(n))
    return fizz_buzzed_nums

if __name__ == "__main__":
    doctest.testmod()