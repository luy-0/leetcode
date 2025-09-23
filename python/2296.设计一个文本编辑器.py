#
# @lc app=leetcode.cn id=2296 lang=python3
#
# [2296] 设计一个文本编辑器
#

# @lc code=start
class TextEditor:

    def __init__(self):
        self.stack_left = []
        self.stack_right = []

    def __str__(self):
        return f"{''.join(self.stack_left)}|{''.join(self.stack_right)}"

    def addText(self, text: str) -> None:
        self.stack_left.extend(text)

    def deleteText(self, k: int) -> int:
        count = min(k, len(self.stack_left))
        del self.stack_left[-count:]
        return count
        

    def cursorLeft(self, k: int) -> str:
        for _ in range(min(k, len(self.stack_left))):
            self.stack_right.append(self.stack_left.pop())
        return ''.join(self.stack_left[-10:])       

    def cursorRight(self, k: int) -> str:
        for _ in range(min(k, len(self.stack_right))):
            self.stack_left.append(self.stack_right.pop())
        return ''.join(self.stack_left[-10:])       


# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)
# @lc code=end

textEditor = TextEditor(); # 当前 text 为 "|" 。（'|' 字符表示光标）
textEditor.addText("leetcode"); # 当前文本为 "leetcode|" 。
print(textEditor)
textEditor.deleteText(4); # 返回 4
                          # 当前文本为 "leet|" 。
                          # 删除了 4 个字符。
print(textEditor)
textEditor.addText("practice"); # 当前文本为 "leetpractice|" 。
print(textEditor)
print(textEditor.cursorRight(3)); # 返回 "etpractice"
print(textEditor)
                           # 当前文本为 "leetpractice|". 
                           # 光标无法移动到文本以外，所以无法移动。
                           # "etpractice" 是光标左边的 10 个字符。
textEditor.cursorLeft(8); # 返回 "leet"
print(textEditor)
                          # 当前文本为 "leet|practice" 。
                          # "leet" 是光标左边的 min(10, 4) = 4 个字符。
textEditor.deleteText(10); # 返回 4
print(textEditor)
                           # 当前文本为 "|practice" 。
                           # 只有 4 个字符被删除了。
textEditor.cursorLeft(2); # 返回 ""
print(textEditor)
                          # 当前文本为 "|practice" 。
                          # 光标无法移动到文本以外，所以无法移动。
                          # "" 是光标左边的 min(10, 0) = 0 个字符。
print(textEditor.cursorRight(6)); # 返回 "practi"
print(textEditor)
                           # 当前文本为 "practi|ce" 。
                           # "practi" 是光标左边的 min(10, 6) = 6 个字符。