class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = ""
        for i in s:
            i = i.lower()
            if i.isalnum():
                result += i
        if result == result[::-1]:
            return True
        return False