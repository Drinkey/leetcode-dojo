from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        _max = nums[-1]
        _min = nums[0]
        print(_min, _max)
        _len_of_nums = len(nums)
        if target <= _min:
            return 0
        if target > _max:
            return _len_of_nums
        if target == _max:
            return _len_of_nums - 1
        for i in range(_len_of_nums - 1):
            _start = nums[i]
            _end = nums[i+1]
            if target == _start:
                return i
            if _start < target <= _end:
                return i + 1
        return -1

s = Solution()

def test_sample_1():
    nums = [1,3,5,6]
    target = 5
    assert s.searchInsert(nums, target) == 2

def test_sample_2():
    nums = [1,3,5,6]
    target = 2
    assert s.searchInsert(nums, target) == 1

def test_sample_3():
    nums = [1,3,5,6]
    target = 7
    assert s.searchInsert(nums, target) == 4

def test_sample_4():
    nums = [1,3,5,6]
    target = 0
    assert s.searchInsert(nums, target) == 0

def test_sample_5():
    nums = [1,3,5,6]
    target = 1
    assert s.searchInsert(nums, target) == 0

def test_sample_6_duplicated():
    nums = [1,3,3,5,6]
    target = 3
    assert s.searchInsert(nums, target) == 1

def test_sample_6_duplicated():
    nums = [1,3,3,5,6]
    target = 4
    assert s.searchInsert(nums, target) == 3

def test_sample_failed_case_1():
    nums = [1, 3]
    target = 3
    assert s.searchInsert(nums, target) == 1