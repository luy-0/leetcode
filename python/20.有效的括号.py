#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for x in s:
            if len(stack) != 0 and self.match(stack[-1], x):
                stack.pop()
            else:
                stack.append(x)
        return len(stack) == 0
        
    def match(self, c1: str, c2: str) -> bool:
        if c1 == "(" and c2 == ")":
            return True
        if c1 == "[" and c2 == "]":
            return True
        if c1 == "{" and c2 == "}":
            return True
        return False
        
# @lc code=end
s = Solution()
a = s.isValid('()[]{}')
print(a)
a = s.isValid('(}')
print(a)
a = s.isValid('()[]')
print(a)

