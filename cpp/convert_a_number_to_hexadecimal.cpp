/* https://leetcode.com/problems/convert-a-number-to-hexadecimal/

Given an integer, write an algorithm to convert it to hexadecimal. For negative integer, two’s complement method is used.

Note:
All letters in hexadecimal (a-f) must be in lowercase.
The hexadecimal string must not contain extra leading 0s. If the number is zero, it is represented by a single zero character '0'; 
    otherwise, the first character in the hexadecimal string will not be the zero character.
The given number is guaranteed to fit within the range of a 32-bit signed integer.
You must not use any method provided by the library which converts/formats the number to hex directly. */

// Runtime: 0 ms, faster than 100.00% of C++ online submissions for Convert a Number to Hexadecimal.
// Memory Usage: 6.2 MB, less than 15.28% of C++ online submissions for Convert a Number to Hexadecimal. -- the 99th percentile uses 5.8 MB.

// c++ is FAST!

public:
    string toHex(int num) {
        if (num == 0) {
            return "0";
        }
        if (num > 0) {
            return r_hex(num);
        } else {
            return r_hex(pow(2,32)+num);
        }
    }
    string r_hex(long num) {
        if (num == 0) {
            return "";
        }
        string hexes = "0123456789abcdef";
        return (r_hex(num/16)) + hexes[num%16];
    }
};