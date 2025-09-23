#
# @lc app=leetcode.cn id=155 lang=python3
#
# [155] 最小栈
#

import sys
# @lc code=start
class MinStack:
    stack = []
    min_data_stack = []
    
    def __init__(self):  
        self.data = []
        self.min_data_stack = []
        pass

    def push(self, val: int) -> None:
        self.data.append(val)
        if len(self.data) == 1:
            self.min_data_stack.append(val)
        else:
            self.min_data_stack.append(min(val, self.min_data_stack[-1]))

    def pop(self) -> None:
        self.data.pop()
        self.min_data_stack.pop()
        

    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        return self.min_data_stack[-1]
        



# @lc code=end
# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-1)
obj.top()

param_4 = obj.getMin()
print(param_4)

