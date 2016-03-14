from math import sqrt

def factorial(n):
    """
    Simple factorial calculator that takes the number n.
    """
    if n == 0:
        return 1
    return n * factorial(n - 1)

def one_over_pi(n):
    scale = sqrt(8) / 9801
    return scale * sum([(factorial(4*x)/pow(factorial(x), 4)) * ((26390 * x + 1103)/pow(396, 4*x)) for x in range(n)])

if __name__ == "__main__":
    print(1 / one_over_pi(100))
