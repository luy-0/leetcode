#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        ret = 0
        for i, c in enumerate(s):
            if c == 'I':
                if i+1 < len(s) and (s[i+1] == 'V' or s[i+1] == 'X'):
                    ret -= 1
                else:
                    ret += 1
            elif c == 'V': 
                ret += 5
            elif c == 'X': 
                if i+1 < len(s) and (s[i+1] == 'L' or s[i+1] == 'C'):
                    ret -= 10
                else:
                    ret += 10
            elif c == 'L': 
                ret += 50
            elif c == 'C': 
                if i+1 < len(s) and (s[i+1] == 'D' or s[i+1] == 'M'):
                    ret -= 100
                else:
                    ret += 100
            elif c == 'D': 
                ret += 500
            elif c == 'M': 
                ret += 1000
        return ret
        
# @lc code=end

