n = int(input())


def print_factorial(fact):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    print("The factorial is:", fact)


print_factorial(n)
