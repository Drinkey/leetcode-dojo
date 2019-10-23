class Solution:
    def isPalindrome(self, x: int) -> bool:
        # negative int is not palindrome
        if x < 0:
            return False
        # one digit int is not palindrome
        if 0 <= x < 10:
            return True
        # tailing 0 is not palindrome
        if x % 10 == 0:
            return False
        
        y = x
        array = []
        while y != 0:
            array.append(y % 10)
            y = int(y/10)
        for i,v in enumerate(array):
            if v != array[-1-i]:
                return False
        return True

s = Solution()
def test_is_palindrome():
    test = 12321
    assert s.isPalindrome(test) == True