def sum_numbers(numbers, index):
    if index == len(numbers) - 1:
        return numbers[index]

    return numbers[index] + sum_numbers(numbers, index + 1)


nums = [int(x) for x in input().split()]

print(sum_numbers(nums, 0))
