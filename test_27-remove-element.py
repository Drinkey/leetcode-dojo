from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        pass

s = Solution()

def test_sample_1():
    nums = [3,2,2,3]
    val = 3
    assert s.removeElement(nums, val) == 2
    assert nums == [2,2]

def test_sample_2():
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    assert s.removeElement(nums, val) == 5
    assert nums == [0, 1, 3, 0, 4]

def test_val_not_in_nums():
    nums = [0,1,2,2,3,0,4,2]
    val = 7
    assert s.removeElement(nums, val) == 8
    assert nums == [0,1,2,2,3,0,4,2]

def test_nums_all_is_val():
    nums = [110, 110, 110, 110, 110, 110, 110]
    val = 110
    assert s.removeElement(nums, val) == 7

