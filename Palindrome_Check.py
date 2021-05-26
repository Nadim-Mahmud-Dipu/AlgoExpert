# # Palindrome Check
# O(N^2) Time | O(N) Space
# def isPalindrome(string):
#     reversedString = ""
#     for i in reversed(range(len(string))):
#         reversedString += string[i]
#     return string == reversedString

# O(N) Time | O(N) Space
# def isPalindrome(string):
#     reversedString = []
#     for i in reversed(range(len(string))):
#         reversedString.append(string[i])
#     return string == "".join(reversedString)

# O(N) Time | O(N) Space
# def isPalindrome(string, i=0):
#     j = len(string) - 1 - i
#     return True if i >= j else string[i] == string[j] and isPalindrome(string, i + 1)

# Iterative Solution\
# O(N) Time | O(1) Space
def isPalindrome(string):
    leftIdx = 0
    rightIdx = len(string) - 1
    while leftIdx < rightIdx:
        if string[leftIdx] != string[rightIdx]:
            return False
        leftIdx += 1
        rightIdx -= 1
    return True

print(isPalindrome("abcdba"))
