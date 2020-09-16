# https://leetcode.com/problems/lucky-numbers-in-a-matrix/

'''
Given a m * n matrix of distinct numbers, return all lucky numbers in the matrix in any order.

A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.

 

Example 1:

Input: matrix = [[3,7,8],[9,11,13],[15,16,17]]
Output: [15]
Explanation: 15 is the only lucky number since it is the minimum in its row and the maximum in its column
Example 2:

Input: matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
Output: [12]
Explanation: 12 is the only lucky number since it is the minimum in its row and the maximum in its column.
Example 3:

Input: matrix = [[7,8],[1,2]]
Output: [7]
 

Constraints:

m == mat.length
n == mat[i].length
1 <= n, m <= 50
1 <= matrix[i][j] <= 10^5.
All elements in the matrix are distinct.
'''

# Not my best work

class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        lucky_nums = []
        for y in range(0,len(matrix)):
            for x in range(0,len(matrix[y])):
                if min_in_row(matrix,x,y) and max_in_col(matrix,x,y):
                    lucky_nums.append(matrix[y][x])
        return lucky_nums
    
def min_in_row(matrix,x,y):
    num = matrix[y][x]
    for i in range(0,len(matrix[y])):
        if i == x:
            continue
        if matrix[y][i] <= num:
            return False
    return True

def max_in_col(matrix,x,y):
    num = matrix[y][x]
    for i in range(0,len(matrix)):
        if i == y:
            continue
        if matrix[i][x] >= num:
            return False
    return True