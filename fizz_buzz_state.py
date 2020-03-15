import doctest

from fizz_buzz_basic import fizz_buzz


def fizz_buzz_state(num):
    """
    For numbers between 1 and num, set the state of the number to:
        - Fizz if number is divisible by 3 only
        - Buzz if number is divisible by 5 only
        - FizzBuzz if number is divisible by 3 and 5
        - number otherwise
    """
    fizz_buzzed_state = {}
    for n in range(num+1):
        fizz_buzzed_state[n] = fizz_buzz(n)
    
    return fizz_buzzed_state

if __name__ == "__main__":
    doctest.testmod()