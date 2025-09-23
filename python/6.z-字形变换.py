#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] Z 字形变换
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        queue_list = list()
        for i in range(numRows):
            queue_list.append(list())

        flag = 1
        queue_index = 0
        for c in s:
            if queue_index == 0:
                flag = 1
            if queue_index == numRows-1:
                flag = -1
            queue_list[queue_index].append(c)
            queue_index += flag
        
        ret = ""
        for li in queue_list:
            ret += "".join(li)
        return ret

# @lc code=end

