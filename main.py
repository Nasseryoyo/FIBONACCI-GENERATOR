def fibonacci_generator():
    """
    This function is a generator that yields the Fibonacci sequence indefinitely.
    It starts with 0 and 1, and each subsequent number is the sum of the two previous numbers.
    """
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
def main():
    """
    This function tests the fibonacci_generator function by printing the first 11 Fibonacci numbers.
    """
    # Test the fibonacci_generator function
    fib = fibonacci_generator()
    for _ in range(11):
        print(next(fib))

if __name__ == "__main__":
    main()
