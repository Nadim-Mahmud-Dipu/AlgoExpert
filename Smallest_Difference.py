def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    print(arrayOne, arrayTwo)
    idx1 = 0
    idx2 = 0
    smallest = float("inf")
    current = float("inf")
    smallest_difference_pair = []
    while idx1 < len(arrayOne) and idx2 < len(arrayTwo):
        firstNum = arrayOne[idx1]
        secondNum = arrayTwo[idx2]
        if firstNum < secondNum:
            current = secondNum - firstNum
            idx1 += 1
        elif secondNum < firstNum:
            current = firstNum - secondNum
            idx2 += 1
        else:
            return [firstNum, secondNum]

        if smallest > current:
            smallest = current
            smallest_difference_pair = [firstNum, secondNum]
    return smallest_difference_pair


print(smallestDifference([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]))
