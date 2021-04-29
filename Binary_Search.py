# # Binary Search
# # O(log(n)) Time | O(log(n)) Space
# def binarySearch(array, target):
#     return binarySearchHelper(array, target, 0, len(array) - 1)
#
#
# def binarySearchHelper(array, target, left, right):
#     if left > right:
#         return -1
#     middle = (left + right) // 2
#     potentialMatch = array[middle]
#     if target == potentialMatch:
#         return middle
#     elif target < potentialMatch:
#         return binarySearchHelper(array, target, left, middle - 1)
#     else:
#         return binarySearchHelper(array, target, middle + 1, right)

# O(log(n)) Time | O(log(1)) Space
def binarySearch(array, target):
    return binarySearchHelper(array, target, 0, len(array) - 1)


def binarySearchHelper(array, target, left, right):
    while left <= right:
        middle = (left + right) // 2
        potentialMatch = array[middle]
        if target == potentialMatch:
            return middle
        elif target < potentialMatch:
            right = middle - 1
        else:
            left = middle + 1

    return -1

print(binarySearch([1,2,3,4,5,6,7,8], 9))