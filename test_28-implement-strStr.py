class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return 0

s = Solution()

def test_sample_1():
    haystack = "hello"
    needle = "ll"
    assert s.strStr(haystack, needle) == 2

def test_sample_2():
    haystack = "aaaaa"
    needle = "bba"
    assert s.strStr(haystack, needle) == -1

def test_needle_empty():
    haystack = "aaaaa"
    needle = ""
    assert s.strStr(haystack, needle) == 0