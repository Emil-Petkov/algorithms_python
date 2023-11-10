def fibonacci(num):
    if num <= 1:
        return num

    else:
        return fibonacci(num - 1) + fibonacci(num - 2)


num = int(input())
fibonacci_series = ', '.join(str(fibonacci(n)) for n in range(num + 1))

print(fibonacci_series)


########################################################################

def fibonacci(n):
    a, b = 0, 1

    series = []

    for i in range(n + 1):
        series.append(str(a))
        a, b = b, a + b

    return ', '.join(series)


print(fibonacci(5))
