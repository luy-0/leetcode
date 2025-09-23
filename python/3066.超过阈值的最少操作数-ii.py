#
# @lc app=leetcode.cn id=3066 lang=python3
#
# [3066] 超过阈值的最少操作数 II
#
from typing import *
from heapq import *
# @lc code=start
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # from heapq import *
        # 使用 heapq 来达到堆（优先队列）功能
        # heapify 堆化
        # heappop heappush 等操作
        # 注意这些方法都是 heapq 里面的方法，并没有提供 堆 这个数据结构（类）
        heapify(nums)
        c = 0
        while nums[0] < k:
            x = heappop(nums)
            heapreplace(nums, x * 2 + max(x, nums[0]))
            c += 1
        return c


    # TLE 使用数组排序 超时
    def badAnswer(self, nums: List[int], k: int) -> int:
        heap = [x for x in nums if x < k]
        heap.sort()
        count = 0
        while heap:
            if len(heap) == 1:
                return count + 1
            x = heap.pop(0)
            y = heap.pop(0)
            if min(x, y) * 2 + max(x, y) < k:
                heap.append(min(x, y) * 2 + max(x, y))
                heap.sort()
            count += 1
        return count
# @lc code=end
s = Solution()
a = s.minOperations([2,11,10,1,3], 10)
print(a)
