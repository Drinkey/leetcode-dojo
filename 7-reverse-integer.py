class Solution:
    def reverse(self, x: int) -> int:
        MIN = -2 ** 31
        MAX = 2 ** 31 - 1
        if not (MIN <= x <= MAX):
            return 0
        stringify = str(x)[::-1]
        if x < 0:
            ret = -1 * int(stringify[:-1:])
        else:
            ret = int(stringify)
        return ret if (MIN <= ret <= MAX) else 0

s = Solution()

def test_01_reverse_int_regular_123():
    assert s.reverse(123) == 321

def test_02_reverse_int_big_23456():
    assert s.reverse(23456) == 65432

def test_03_reverse_int_tail_0():
    assert s.reverse(320) == 23

def test_04_reverse_int_negative_543():
    assert s.reverse(-543) == -345

def test_05_reverse_int_negative_tail_0():
    assert s.reverse(-120) == -21

def test_reverse_int_less_than_MIN():
    
    assert s.reverse(1563847412) == 0

# def test_reverse_int_():
#     assert s.reverse() == 
