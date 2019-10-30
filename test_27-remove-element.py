from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        len_of_nums = len(nums)
        j = 0 # index of new nums-in-place
        for i in range(len_of_nums):
            if nums[i] != val:
                nums[j] = nums[i]
                j+=1
        return j

s = Solution()

def test_sample_1():
    nums = [3,2,2,3]
    val = 3
    r = s.removeElement(nums, val)
    assert r == 2
    assert nums[:r] == [2,2]

def test_sample_2():
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    r = s.removeElement(nums, val)
    assert r == 5
    assert nums[:r] == [0, 1, 3, 0, 4]

def test_val_not_in_nums():
    nums = [0,1,2,2,3,0,4,2]
    val = 7
    r = s.removeElement(nums, val)
    assert r == 8
    assert nums[:r] == [0,1,2,2,3,0,4,2]

def test_nums_all_is_val():
    nums = [110, 110, 110, 110, 110, 110, 110]
    val = 110
    r = s.removeElement(nums, val)
    assert r == 0

