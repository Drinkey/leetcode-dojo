from typing import List
class Solution:
    def twoSum_v1(self, nums: List[int], target: int) -> List[int]:
        # print(f"INPUT: {nums}, target={target}. building cache...")
        for i, val1 in enumerate(nums):
            x = i+1
            choice = nums[x:]
            for j,val2 in enumerate(choice):
                if val1+val2 == target:
                    return [i, j+x]
        return []

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {}
        for i, num in enumerate(nums):
            n = target - num
            if n in cache:
                return [cache[n], i]
            else:
                cache[nums[i]] = i
        return []

s = Solution()

def test_v1():
    nums = [2, 7, 11, 15]
    target = 9
    expected = [0, 1]
    real = s.twoSum_v1(nums, target)
    print(real)
    assert expected == real

def test_v2():
    nums = [2, 7, 11, 15]
    target = 26
    expected = [2, 3]
    real = s.twoSum(nums, target)
    print(real)
    assert expected == real

