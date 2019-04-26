"""
Leetcode 467: https://leetcode.com/problems/number-complement/
"""

"""
Method 1: filp bit by bit
"""
def findComplement(self, num: int) -> int:
    i = 1
    while i <= num:
        num ^= i
        i <<= 1
    return num

"""
Method 2: num ^ 111...11 (L ones, L is the length of binary representation of num)
"""
def findComplement(self, num: int) -> int:
    return num ^ ((1 << num.bit_length()) - 1)

"""
Method 3: again find the lenght first
"""
def findComplement(self, num: int) -> int:
    return num ^ ((1 << len(bin(num)) - 2) - 1)