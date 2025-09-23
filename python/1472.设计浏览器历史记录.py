#
# @lc app=leetcode.cn id=1472 lang=python3
#
# [1472] 设计浏览器历史记录
#

# @lc code=start
from typing import *
class BrowserHistory:
    back_stack: List[str]
    forward_stack: List[str]
    curr_url: str
    
    def __str__(self):
            # 自定义对象的字符串表示
            return f"BrowserHistory(curr_url={self.curr_url}, back_stack={self.back_stack},forward_stack={self.forward_stack})"
    
    def __init__(self, homepage: str):
        self.back_stack = []    
        self.forward_stack = []    
        self.curr_url = homepage

    def visit(self, url: str) -> None:
        if self.curr_url:
            self.back_stack.append(self.curr_url)
        self.forward_stack = []
        self.curr_url = url
        # print("visit: ", self)
        

    def back(self, steps: int) -> str:
        if steps > len(self.back_stack):
            steps = len(self.back_stack)
        for _ in range(steps):
            self.forward_stack.append(self.curr_url)
            self.curr_url = self.back_stack.pop()
        # print("back: ", self)
        return self.curr_url

    def forward(self, steps: int) -> str:
        if steps > len(self.forward_stack):
            steps = len(self.forward_stack)
        for _ in range(steps):
            self.back_stack.append(self.curr_url)
            self.curr_url = self.forward_stack.pop()
        # print("forward: ", self)
        return self.curr_url

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
# @lc code=end

obj = BrowserHistory("leetcode")
obj.visit("google")
obj.visit("facebook")
obj.visit("youtube")


print(obj.back(1))
print(obj.back(1))
print(obj.forward(1))
obj.visit("linkedin")
print(obj.forward(2))

print(obj.back(2))
print(obj.back(7))
