#
# @lc app=leetcode.cn id=2239 lang=python3
#
# [2239] 找到最接近 0 的数字
#

# @lc code=start
from math import inf


class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        diff_abs = float(inf)
        ans = 0
        for x in nums:
            if abs(x) < diff_abs:
                diff_abs = abs(x)
                ans = x
            elif abs(x) == diff_abs:
                ans = max(ans, x)
        return ans
        
# @lc code=end

