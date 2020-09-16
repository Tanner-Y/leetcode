# https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/
'''
Given a string s formed by digits ('0' - '9') and '#' . We want to map s to English lowercase characters as follows:

Characters ('a' to 'i') are represented by ('1' to '9') respectively.
Characters ('j' to 'z') are represented by ('10#' to '26#') respectively. 
Return the string formed after mapping.

It's guaranteed that a unique mapping will always exist.

 

Example 1:

Input: s = "10#11#12"
Output: "jkab"
Explanation: "j" -> "10#" , "k" -> "11#" , "a" -> "1" , "b" -> "2".
Example 2:

Input: s = "1326#"
Output: "acz"
Example 3:

Input: s = "25#"
Output: "y"
Example 4:

Input: s = "12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"
Output: "abcdefghijklmnopqrstuvwxyz"
'''

# 24ms runtime beats 95.25% of other solutions.

class Solution:
    def freqAlphabets(self, s: str) -> str:
        dic = {
            '1':'a',
            '2':'b',
            '3':'c',
            '4':'d',
            '5':'e',
            '6':'f',
            '7':'g',
            '8':'h',
            '9':'i',
            '#01':'j',
            '#11':'k',
            '#21':'l',
            '#31':'m',
            '#41':'n',
            '#51':'o',
            '#61':'p',
            '#71':'q',
            '#81':'r',
            '#91':'s',
            '#02':'t',
            '#12':'u',
            '#22':'v',
            '#32':'w',
            '#42':'x',
            '#52':'y',
            '#62':'z'
        }
        s = s[::-1]
        i = 0
        output = ''
        while i < len(s):
            if s[i] == '#':
                output += dic[s[i:i+3]]
                i += 3
            else:
                output += dic[s[i]]
                i += 1
        return output[::-1]