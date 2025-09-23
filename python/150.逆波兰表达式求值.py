#
# @lc app=leetcode.cn id=150 lang=python3
#
# [150] 逆波兰表达式求值
#

# @lc code=start
from typing import *
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # 题目保证表达式合法
        stack = []
        for x in tokens:
            if x == '+':
                num2, num1 = stack.pop(), stack.pop()
                # print(f'{num1}+{num2} = {num1 + num2}')
                stack.append(num1 + num2)
                continue
            if x == '-':
                # 特别注意 减法 除法 在这里的元素的顺序不要弄反
                num2, num1 = stack.pop(), stack.pop()
                # print(f'{num1}-{num2} = {num1 - num2}')
                stack.append(num1 - num2)
                continue
            if x == '*':
                num2, num1 = stack.pop(), stack.pop()
                # print(f'{num1}*{num2} = {num1 * num2}')
                stack.append(num1 * num2)
                continue
            if x == '/':
                # / 用于执行浮点数除法，即返回除法运算的结果，包括小数部分。
                # // 用于执行整数除法，即返回除法运算的商，但不包括小数部分，结果总是向下取整。
                # % 用于计算两个数相除的余数。
                num2, num1 = stack.pop(), stack.pop()
                print(f'{num1}/{num2} = {num1 / num2}')
                stack.append(int(num1 / num2))
                continue
            stack.append(int(x))
        return stack[0]
        
# @lc code=end

s = Solution()
a = s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
a = s.evalRPN(["4","13","5","/","+"])
print(a)
