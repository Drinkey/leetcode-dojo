from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        len_of_nums = len(nums)
        uniqcnt = 0
        last_num = None

        for i in range(len_of_nums):
            if last_num == None:
                last_num = nums[i]
                uniqcnt +=1
                continue
            curr = nums[i]
            # print(f"i={i}, curr={curr}, last={last_num}, uniq={uniqcnt}")
            if curr != last_num:
                nums[uniqcnt] = last_num = curr
                uniqcnt += 1
        return uniqcnt

s = Solution()

def test_sample_1():
    nums = [1,1,2]
    l = s.removeDuplicates(nums)
    assert l == 2
    assert nums[:l] == [1, 2]

def test_sample_2():
    nums = [0,0,1,1,1,2,2,3,3,4]
    l = s.removeDuplicates(nums)
    assert l == 5
    assert nums[:l] == [0, 1, 2, 3, 4]

def test_sample_3():
    nums = [0,0,0]
    l = s.removeDuplicates(nums)
    assert l == 1
    assert nums[:l] == [0]

def test_sample_2():
    nums = [-10,-10, -1, 0,0,1,1,1,2,2,3,3,4]
    l = s.removeDuplicates(nums)
    assert l == 7
    assert nums[:l] == [-10, -1, 0, 1, 2, 3, 4]