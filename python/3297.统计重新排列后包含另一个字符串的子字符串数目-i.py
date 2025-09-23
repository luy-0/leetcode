#
# @lc app=leetcode.cn id=3297 lang=python3
#
# [3297] 统计重新排列后包含另一个字符串的子字符串数目 I
#

# @lc code=start
from functools import cache
from collections import Counter
class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        return self.good_answer(word1, word2)
    
    # 滑动窗口做法
    def good_answer(self, word1: str, word2: str) -> int:
        # l = start of sub_string, init = 0
        # r = end of sub_string, init = 0
        # if ss=word1[l, r+1], then any sss=word1[l, r+1+k] ok, total count add len(words)-r+1

        # 当 word1[l, r+1] 刚好满足时，l++，必然导致不满足。必须要求r++直到满足
        diff = {}
        count = 0
        for c in word2:
            if not c in diff:
                diff[c] = 0
            diff[c] -= 1

        cnt = sum(1 for v in diff.values() if v < 0)
        # print(f"cnt{cnt}, diff{diff}")

        l = 0
        r = 0
        while l < len(word1):
            while r < len(word1) and cnt > 0:
                # print(f"{l},{r}, word = {word1[l:r]}, diff{diff}")
                c = word1[r]
                if c in diff:
                    diff[c] += 1
                else:
                    diff[c] = 1
                cnt = sum(1 for v in diff.values() if v < 0)
                r += 1

            if cnt == 0:
                count += len(word1) - r + 1
            
            c = word1[l]
            if not c in diff:
                diff[c] = 0
            diff[c] -= 1
            cnt = sum(1 for v in diff.values() if v < 0)
            l += 1
        return count

            


            
    

    # 可以解决题目，但是会超时
    def bad_answer(self, word1: str, word2: str) -> int:
        @cache
        def isLegal(ss: str, sub: str) -> bool:
            ss_dict = Counter(ss)
            sub_dict = Counter(sub)
            for x, time in sub_dict.items():
                if not x in ss_dict or time>ss_dict[x]:
                    return False
            return True
        
        # if ss=word1[i:j] legal, than any sss=word1[i:j+k] legal
        # k = any in range(0, len(word1)-j)
        count = 0
        for i in range(0, len(word1) - len(word2) + 1):
            # i = start of sub_string
            for length in range(len(word2), len(word1) - i+1):
                # length = len of sub_string
                # j = i + length = end of sub_string
                if isLegal(word1[i:i+length], word2):
                    count += len(word1) - (i+length) + 1
                    # print(f"i={i}, length={length}, sub_string={word1[i: i+length]}, so add {len(word1) - (i+length)}, count = {count}")
                    break

        
        
        return count

        
# @lc code=end
s = Solution()
a = s.validSubstringCount("abcabc", "abc")
print(a)

