/*

https://leetcode.com/problems/number-of-good-pairs/

1512. Number of Good Pairs
Easy

473

35

Add to List

Share
Given an array of integers nums.

A pair (i,j) is called good if nums[i] == nums[j] and i < j.

Return the number of good pairs.

 

Example 1:

Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
Example 2:

Input: nums = [1,1,1,1]
Output: 6
Explanation: Each pair in the array are good.
Example 3:

Input: nums = [1,2,3]
Output: 0
 

Constraints:

1 <= nums.length <= 100
1 <= nums[i] <= 100

Runtime: 0 ms, faster than 100.00% of C++ online submissions for Number of Good Pairs.
Memory Usage: 7.5 MB, less than 18.23% of C++ online submissions for Number of Good Pairs.

*/



class Solution {
public:
    int numIdenticalPairs(vector<int>& nums) {
        vector<int> a(101,0);
        for (int num : nums) {
            a[num]++;
        }
        int output = 0;
        for (int n : a) {
            if (n != 0) {
                output += ((n*(n-1))/2);
            }
            
        }
        return output;
    }
};
