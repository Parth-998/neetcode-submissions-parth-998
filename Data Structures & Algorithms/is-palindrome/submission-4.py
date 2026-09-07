class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        result = ""
        for i in s:
            if i.isalnum():
                result += i
        if result == result[::-1]:
            return True
        return False