from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        if len(strs) == 1:
            return strs[0]

        min_, max_ = min(strs), max(strs)
        if max_.startswith(min_):
            return min_
        range_ = min([len(min_), len(max_)])
        print(f"r = {range_}, min = {min_}, max = {max_}")
        for i in range(range_):
            print(f"i={i}, if {min_[i]} =? {max_[i]}")
            if min_[i] != max_[i]:
                return min_[:i]
        return ''

s = Solution()

def test_long_common_prefix_sample():
    test = ["flower","flow","flight","flowerc"]
    exp = 'fl'
    assert s.longestCommonPrefix(test) == exp

def test_long_common_prefix_test1():
    test = ["flower","flow","flowry", "flo"]
    exp = 'flo'
    assert s.longestCommonPrefix(test) == exp

def test_long_common_prefix_one():
    test = ["flower"]
    exp = 'flower'
    assert s.longestCommonPrefix(test) == exp

def test_long_common_prefix_no_common():
    test = ["faower","cflow","flight"]
    exp = ''
    assert s.longestCommonPrefix(test) == exp

def test_long_common_prefix_dup_common():
    test = ["fffaower","ffcflow","ffflight"]
    exp = 'ff'
    assert s.longestCommonPrefix(test) == exp

def test_long_common_prefix_empty_input():
    test = []
    exp = ''
    assert s.longestCommonPrefix(test) == exp