def recursive_factorial(fact):
    if fact == 0:  # base case
        return 1

    return fact * recursive_factorial(fact - 1)  # recursive call


factorial = int(input())
print(recursive_factorial(factorial))
