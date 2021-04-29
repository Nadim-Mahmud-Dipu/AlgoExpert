#
# def findThreeLargestNumbers(array):
#     largest_three = []
#     for i in range(3):
#         maximum = max(array)
#         largest_three.append(maximum)
#         array.remove(maximum)
#     return sorted(largest_three, reverse=False)
#
# print(findThreeLargestNumbers([141,1,17,-7,-17,-27,18,541,8,7,7]))

# O(N) Time| O(N) Space
def findThreeLargestNumber(array):
    negative_inf = - float("inf")
    largest_three = [negative_inf, negative_inf, negative_inf]
    for i in array:
        if i > largest_three[2]:
            largest_three[0] = largest_three[1]
            largest_three[1] = largest_three[2]
            largest_three[2] = i
        else:
            if i > largest_three[1]:
                largest_three[0] = largest_three[1]
                largest_three[1] = i
            else:
                if i > largest_three[0]:
                    largest_three[0] = i

    return largest_three


print(findThreeLargestNumber([141,1,17,-7,-17,-27,18,541,8,7,7]))








