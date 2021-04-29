# Product Sum
def ProductSum(array, multiplier = 1):
    sum = 0
    for element in array:
        if type(element) is list:
            sum += ProductSum(element, multiplier+1)
        else:
            sum += element

    return sum * multiplier

print(ProductSum([5,2,[7,-1],3,[6,[-13,8],4]]))