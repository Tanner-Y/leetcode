// https://leetcode.com/problems/shuffle-string/
/*

Given a string s and an integer array indices of the same length.
The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.
Return the shuffled string.

Example:
Input: s = "codeleet", indices = [4,5,6,7,0,2,1,3]
Output: "leetcode"
Explanation: As shown, "codeleet" becomes "leetcode" after shuffling.

*/

class Solution {
public:
    string restoreString(string s, vector<int>& indices) {
        vector<char> output(indices.size());
        int idx = 0;
        for (int i : indices) {
            output[i] = s[idx];
            idx++;
        }
        string sout = "";
        for (char o : output) {
            sout += o;
        }
        return sout;
    }
};

// Not the most graceful, but it'll do in a pinch.
