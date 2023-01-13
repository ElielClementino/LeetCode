# https://leetcode.com/problems/palindrome-number/
x = 121
def isPalindrome(x: int) -> bool:
    if str(x) == str(x)[::-1]:
        return True
    else:
        return False

print(isPalindrome(x))