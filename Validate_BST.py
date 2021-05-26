# O(N) Time | O(D) Space where D is the depth of the tree.
def ValidateBST(tree):
    return validateBstHelper(tree, float("-inf"), float("inf"))

def validateBstHelper(tree, minValue, maxValue):
    if tree is None:
        return True
    if tree.value < minValue or tree.value > maxValue:
        return False
    leftIsValid = validateBstHelper(tree.left, minValue, tree.value)

    return leftIsValid and validateBstHelper(tree.right, tree.value, maxValue)