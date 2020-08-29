'''
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        largest = ""
        running = ""
        for i in range(len(s)):
            if (s[i] not in running):
                running += s[i]
            else:
                if (len(largest) < len(running)):
                    largest = running
                running = running[running.index(s[i])+1:i] + s[i]
        if len(largest) < len(running):
            largest = running
        return len(largest)
