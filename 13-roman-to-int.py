class Solution:
    def romanToInt(self, s: str) -> int:
        ROMANMAP = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000,}
        result = 0
        length = len(s)

        for i in range(length):
            # i+1<length: lazy eval, when this is false, s[i+1] will not be evaluated to avoid out of range error
            # If current char is less than next char, use - op, other, should add all up.
            if i+1 < length and ROMANMAP[s[i]] < ROMANMAP[s[i+1]]:
                result -= ROMANMAP[s[i]]
            else:
                result += ROMANMAP[s[i]]
        print(f"this result: {result}")
        return result

s = Solution()

def test_original_sample_1():
    assert s.romanToInt("III") == 3

def test_original_sample_2():
    assert s.romanToInt("IV") == 4

def test_original_sample_3():
    assert s.romanToInt("IX") == 9

def test_original_sample_4():
    assert s.romanToInt("LVIII") == 58

def test_original_sample_5():
    assert s.romanToInt("MCMXCIV") == 1994

def test_roman_40():
    assert s.romanToInt("XL") == 40

def test_roman_90():
    assert s.romanToInt("XC") == 90

def test_roman_400():
    assert s.romanToInt("CD") == 400

def test_roman_900():
    assert s.romanToInt("CM") == 900