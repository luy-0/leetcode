#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 当两个边界一长一短时，仅有移动短边时可能带来更大收益
        # 如果移动长线，水位高度被短边锁死上限，而宽度减少
        # 如果移动短线，水位高度可能被提高上线，从而对冲宽度损失
        left = 0
        right = len(height) - 1
        vol = min(height[left], height[right]) * (right - left)
        while left < right:
            if height[left] < height[right]:
                left += 1
                new_vol = min(height[left], height[right]) * (right - left)
                vol = max(vol, new_vol)
            else:
                right -= 1
                new_vol = min(height[left], height[right]) * (right - left)
                vol = max(vol, new_vol)
        return vol
    

        
# @lc code=end

