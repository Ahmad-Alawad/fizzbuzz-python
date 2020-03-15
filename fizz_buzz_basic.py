def fizz_buzz(num):
    """
    Return Fizz if number is divisible by 3 only
    Return Buzz if number is divisible by 5 only
    Return FizzBuzz if number is divisible by 3 and 5
    Return number otherwise
    """
    if num%3 == 0  and num%5 == 0:
        return "FizzBuzz"
    elif num%3 == 0:
        return "Fizz"
    elif num%5 == 0:
        return "Buzz"
    else:
        return num
