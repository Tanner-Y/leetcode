/*
https://leetcode.com/problems/sort-colors/

Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Example:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

My score:
Runtime: 0 ms, faster than 100.00% of C++ online submissions for Sort Colors.
Memory Usage: 8.6 MB, less than 12.32% of C++ online submissions for Sort Colors. <- I guess those three ints really make a difference?
*/

class Solution {
public:
    void sortColors(vector<int>& nums) {
        if (nums.size() <= 1) {
            return;
        }
        int i0 = 0;
        int i2 = nums.size()-1;
        int i = 0;
        while (i < nums.size() && i <= i2) {
            if (nums[i] == 1) {
                i++;
            } else if (nums[i] == 0) {
                nums[i] = nums[i0];
                nums[i0] = 0;
                i0++;
                i++;
            } else { // (nums[i] == 2)
                nums[i] = nums[i2];
                nums[i2] = 2;
                i2--;
            }
        }
    }
};