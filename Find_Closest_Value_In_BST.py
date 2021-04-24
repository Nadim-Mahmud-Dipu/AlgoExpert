# Time complexity, Average: O(log(n)) | Space complexity: O(log(n))
# Worst case: O(n) |Space complexity: O(n)

# Recursive Approach
# def findClosestValueInBst(tree, target):
#     return findClosestValueInBstHelper(tree, target, float("inf"))
#
#
# def findClosestValueInBstHelper(tree, target, closest):
#     if tree is None:
#         return closest
#     if abs(target - closest) > abs(target - tree.value):
#         closest = tree.value
#     if target < tree.value:
#         findClosestValueInBstHelper(tree.left, target, closest)
#     elif target > tree.value:
#         findClosestValueInBstHelper(tree.right, target, closest)
#     else:
#         return closest

class Node:
    def __init__(self, value=None):
        self.value = value
        self.left_child = None
        self.right_child = None


class Binary_search_tree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, cur_node):
        if value < cur_node.value:
            if cur_node.left_child == None:
                cur_node.left_child = Node(value)
            else:
                self._insert(value, cur_node.left_child)
        elif value > cur_node.value:
            if cur_node.right_child == None:
                cur_node.right_child = Node(value)
            else:
                self._insert(value, cur_node.right_child)
        else:
            print("Value laready in tree.")

    def print_tree(self):
        if self.root != None:
            self._print_tree(self.root)

    def _print_tree(self, cur_node):
        if cur_node != None:
            self._print_tree(cur_node.left_child)
            print(cur_node.value)
            self._print_tree(cur_node.right_child)




# Iterative Approach

# Time complexity, Average: O(log(n)) | Space complexity: O(1)
# Worst case: O(n) |Space complexity: O(1)

def findClosestValueInBst(tree, target):
    closest = 100000000000
    currentNode = tree.root
    while currentNode is not None:

        if abs(target - closest) > abs(target - currentNode.value):
            closest = currentNode.value
        if target < currentNode.value:
            currentNode = currentNode.left_child
        elif target > currentNode.value:
            currentNode = currentNode.right_child
        else:
            break
    return closest


bst = Binary_search_tree()
bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(2)
bst.insert(5)
bst.insert(13)
bst.insert(22)
bst.insert(14)

bst.print_tree()
print("Closest value to {target} is {result}".format(target=12,result=findClosestValueInBst(bst,12)))
