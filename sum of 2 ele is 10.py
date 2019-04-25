def getPairsCount(numbers, shouldEqualTo):
    count = 0
    for i in range(len(numbers)):9
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == shouldEqualTo:
                count += 1
    return count
print getPairsCount([1,2,3,4,5,6,7,8,9],10)
