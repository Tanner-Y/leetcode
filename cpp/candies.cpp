/*
https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

Given the array candies and the integer extraCandies, 
where candies[i] represents the number of candies that the ith kid has.

For each kid check if there is a way to distribute extraCandies among the 
kids such that he or she can have the greatest number of candies among them. 
Notice that multiple kids can have the greatest number of candies.

Ex.
Input: candies = [2,3,5,1,3], extraCandies = 3
Output: [true,true,true,false,true] 
*/

class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        int max = -1;
        vector<bool> ret(candies.size());
        // Oh so apparently there's a *max_element(candies.begin(),candies.end());
        // Well here's the for loop I originally had.
        for (int candy : candies) {
            if (candy > max) {
                max = candy;
            }
        }
        for (int i = 0; i < candies.size(); i++) {
            if (candies[i] + extraCandies >= max) {
                ret[i] = true;
            } else {
                ret[i] = false;
            }
        }
        return ret;
    }
};