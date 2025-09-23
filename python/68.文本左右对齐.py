#
# @lc app=leetcode.cn id=68 lang=python3
#
# [68] 文本左右对齐
#

# @lc code=start
from typing import *
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ret = []
        curr_words = []
        for w in words:
            # 不断地尝试加入新词
            if self.can_add_new_word(curr_words, w, maxWidth):
                # 可以加入新词，继续
                curr_words.append(w)
                pass
            else:
                # 不能加入新词了，居中对齐，并将当前w加入下一循环
                mid_words_str = self.mid_format_row(curr_words, maxWidth)
                ret.append(mid_words_str)
                curr_words = [w]
        # 最后一行左对齐
        left_words_str = self.left_format_row(curr_words, maxWidth)
        if left_words_str :
            ret.append(left_words_str)

        return ret

    def can_add_new_word(self, sub_words: List[str], new_word: str, maxWidth: int) -> bool:
        ret = True
        if len(sub_words) + len("".join(sub_words)+new_word) > maxWidth:
            # len(sub_words) 至少一个空格
            # len("".join(sub_words)+new_word) 总字符数
            ret = False
        # print('can_add_new_word: ', sub_words, new_word, ret)
        return ret
    
    def mid_format_row(self, sub_words: List[str], maxWidth: int) -> str:
        if len(sub_words) == 1:
            return sub_words[0] + " " * (maxWidth - len(sub_words[0]))
        all_blank_num = maxWidth - len("".join(sub_words))
        base_blank_num = all_blank_num//(len(sub_words)-1)
        blank = [base_blank_num] * (len(sub_words)-1)    # 表示第i个单词后的空格数量
        for i in range(all_blank_num%(len(sub_words)-1)):
            blank[i] += 1
        text = ""
        for i, count in enumerate(blank):
            text += sub_words[i] + ' '*count
        text += sub_words[-1]
        # print('mid_format_row: ', sub_words, text)
        return text

    
    def left_format_row(self, sub_words: List[str], maxWidth: int) -> str:
        text = " ".join(sub_words) 
        text += " " * (maxWidth - len(text))
        # print('left_format_row: ', sub_words, text)

        return text 

# @lc code=end

if __name__ == "__main__":
    test = Solution()
    try:
        with open(__file__, 'r') as file:
            content = file.read()
            words = content.split()
            ret = test.fullJustify(words, 64)
            for line in ret:
                print(line)
    except FileNotFoundError:
        print('No found file')
    except Exception as e:
        print('Exception',e)

