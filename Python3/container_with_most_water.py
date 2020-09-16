# This one was a lot of fun
'''
https://leetcode.com/problems/container-with-most-water/
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example:

Input: [1,8,6,2,5,4,8,3,7]
Output: 49
'''

class Solution:
    def maxArea(self, height: List[int]) -> int:
        best = 0
        i = 0
        n = len(height) - 1
        while i != n:
            if height[i] > height[n]:
                if best < (height[n] * (n-i)):
                    best = (height[n] * (n-i))
                n -= 1
            else:
                if best < height[i] * (n-i):
                    best = height[i] * (n-i)
                i += 1
        return best