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
