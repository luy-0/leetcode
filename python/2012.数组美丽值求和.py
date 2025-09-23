#
# @lc app=leetcode.cn id=2012 lang=python3
#
# [2012] 数组美丽值求和
#

# @lc code=start
from typing import *
class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        n = len(nums)
        ret = 0
        state = [0] * n

        max_pre = nums[0]
        for i in range(1, n-1):
          if nums[i] > max_pre:
             state[i] = -1
             max_pre = nums[i]
        
        min_pos = nums[-1]
        for i in range(n-2, 0 , -1):
            if state[i] == -1 and nums[i] < min_pos:
                ret += 2
            elif nums[i - 1] < nums[i] < nums[i + 1]:
                ret += 1
            if min_pos > nums[i]:
                min_pos = nums[i]
        return ret
        
# @lc code=end
s = Solution()
print(s.sumOfBeauties([55,36,68,97,1,20,5,50,53,21,15,66,93,12,31,14,13,3,24,97,30,14,28,4,67,86,60,59,40,69,83,49,28,88,98,27,94,56,55,66,3,75,76,7,54,68,75,24,13,85,62,47,3,67,16,79,47,38,89,48,40,3,88,53,13,14,40,26,100,87,3,58,8,53,82,63,60,27,76,79,10,1,37,4,48,40,93,10,29,97]))
