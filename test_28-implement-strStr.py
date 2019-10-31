class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        len_of_haystack = len(haystack)
        len_of_needle = len(needle)
        
        if len_of_needle == 0:
            return 0
        if len_of_haystack == 0:
            return -1
        if haystack == needle:
            return 0
        print(f"start searching for {len_of_haystack - len_of_needle} times")
        for i in range(len_of_haystack - len_of_needle+1):
            slot = haystack[i:i+len_of_needle]
            print(f"comparing {slot}")
            if slot == needle:
                print(f"found! {i}")
                return i
        return -1

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

def test_haystack_empty_needle_not_empty():
    haystack = ""
    needle = "aaaaa"
    assert s.strStr(haystack, needle) == -1

def test_haystack_needle_both_empty():
    haystack = ""
    needle = ""
    assert s.strStr(haystack, needle) == 0

def test_failed_case_one_letter_eq():
    haystack = "a"
    needle = "a"
    assert s.strStr(haystack, needle) == 0

def test_failed_case_more_letter_eq():
    haystack = "aaa"
    needle = "aaa"
    assert s.strStr(haystack, needle) == 0

def test_failed_case_more_letter_ne():
    haystack = "aaa"
    needle = "bbb"
    assert s.strStr(haystack, needle) == -1

def test_failed_case_mississippi():
    haystack = "mississippi"
    needle = "pi"
    assert s.strStr(haystack, needle) == 9

def test_failed_case_mississippi():
    haystack = "mississippi"
    needle = "i"
    assert s.strStr(haystack, needle) == 1