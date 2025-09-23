#
# @lc app=leetcode.cn id=3095 lang=python3
#
# [3095] 或值至少 K 的最短子数组 I
#

# @lc code=start

from math import inf
from typing import *
class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        # 注意到或逻辑运算：
        # if OR[a,b] then OR[a,b,c]>=OR[a,b]
        
        # So use left, right. From 0,0 to end



        # 使用 bits 存储位
        # bits[x] 表示第 x 位为1的个数，计算时仅需判断是否有>0，无需判读具体有几个
        # << 左移来计算该位的值
        # 计算当前的值: sum(1<<i for i in range(30) if bits[i] > 0)
        bits = [0] * 30
        res = float(inf)
        def calc(bits):
            return sum(1<<i for i in range(30) if bits[i] > 0)
        
        left = 0
        for right in range(len(nums)):
            # 把 第 right 个数加进 bits
            for i in range(30):
                bits[i] += (nums[right]>>i) & 1
            # left ++
            while left <= right and calc(bits) >= k:
                res = min(res, right-left+1)
                # 把 第 left 个数移出 bits
                for i in range(30):
                    bits[i] -= (nums[left]>>i) & 1
                left += 1
        return res if res < inf else -1
        
# @lc code=end

or_res = 1
for x in [16,20,2]:
    or_res |= x
    print(x, or_res)
