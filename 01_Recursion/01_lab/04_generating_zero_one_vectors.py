







def generating_zero_one_vectors(index, vector):
    if index >= len(vector):
        print(*vector, sep='')
        return

    for num in range(2):
        vector[index] = num
        generating_zero_one_vectors(index + 1, vector)


n_vectors = int(input())
vector = [0] * n_vectors

generating_zero_one_vectors(0, vector)
