













def sum_numbers(numbers, index):
    if index == len(numbers) - 1:  # base case
        return numbers[index]

    return numbers[index] + sum_numbers(numbers, index + 1)  # recursive call


nums = [int(x) for x in input().split()]

print(sum_numbers(nums, 0))
