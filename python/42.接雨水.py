#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#

# @lc code=start

## 思路
## 每个 i 能够存储的水量，取决于 i 两侧的高峰的最小值-height[i]
## 法1: 维护两个数组，左高峰与右高峰， 取数组最小值，三次遍历
## 法2 双指针，两侧往中间走，随时更新
class Solution:
    def trap(self, height: List[int]) -> int:
        return self.trap_2(height) 

    def trap_1(self, height: List[int]) -> int:
        # 左高峰数组
        left_high = []
        left_max = height[0]
        for x in height:
            if x > left_max:
                left_high.append(x)
                left_max = x
            else:
                left_high.append(left_max)
        
        # 右高峰数组
        right_high = []
        right_max = height[-1]
        for x in height[::-1]:
            if x > right_max:
                right_high.insert(0, x)
                right_max = x
            else:
                right_high.insert(0,right_max)
            
        ret = 0
        for i in range(len(height)):
            ret += min(left_high[i], right_high[i]) - height[i]
        return ret
    

    def trap_2(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        left = 0
        right = len(height)-1

        left_max = height[left]
        right_max = height[right]
        ret = 0

        while left < right:
            left_max = max(left_max, height[left])
            right_max  = max(right_max, height[right])
            if left_max < right_max:
                # 左边是短板
                ret += left_max - height[left]
                    # if left == left_max, 则加0
                    # if left < left_max, 则加上 left_max-left(因为right_max>left_max)
                left += 1
            else:                
                ret += right_max - height[right]
                right -= 1
        return ret





        
# @lc code=end

