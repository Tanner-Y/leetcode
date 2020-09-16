'''
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
 

Constraints:

Each string consists only of '0' or '1' characters.
1 <= a.length, b.length <= 10^4
Each string is either "0" or doesn't contain any leading zero.
'''

# Runtime: 28ms (beats 94.12% of Python3 solutions)
# Memory Usage: 13.8 MB (beats 59.69% of Python3 solutions)

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        out = ""
        i = 0
        carry = 0
        la = len(a)
        lb = len(b)
        while i < len(a) or i < len(b) or carry:
            av = 0
            bv = 0
            if i < la:
                av = int(a[la - i - 1])
            if i < lb:
                bv = int(b[lb - i - 1])
            v = av + bv + carry
            carry = 0
            if v == 0:
                out = '0' + out
            elif v == 1:
                out = '1' + out
            elif v == 2:
                out = '0' + out
                carry = 1
            else:
                out = '1' + out
                carry = 1
            i += 1
        return out