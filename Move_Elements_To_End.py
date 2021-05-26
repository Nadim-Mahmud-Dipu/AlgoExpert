# Move element to the end
# O(N) Time | O(1) Space
def moveToTheEnd(array, target):
    i = 0
    j = len(array) - 1
    while i < j:
        if array[i] == target and array[j] == target:
            j -= 1
        if array[i] != target:
            i += 1
        if array[i] == target and array[j] != target:
            array[j], array[i] = array[i], array[j]
            j -= 1

    return array


print(moveToTheEnd([8,9,2, 1, 2, 2, 100,2, 3, 4, 2], 2))
