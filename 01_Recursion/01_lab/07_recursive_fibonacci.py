def fibonacci(num):
    num_one = 1
    num_two = 1

    result = 0

    for _ in range(num - 1):
        result = num_one + num_two

        num_one, num_two = num_two, result

    return result


number = int(input())
print(fibonacci(number))
