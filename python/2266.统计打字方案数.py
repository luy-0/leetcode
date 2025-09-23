#
# @lc app=leetcode.cn id=2266 lang=python3
#
# [2266] 统计打字方案数
#

# @lc code=start
from functools import cache
from itertools import groupby
from typing import *
class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        if not pressedKeys: return 0
        MOD = 1000_000_007
        # 两个子问题
        # 1. 拆成连续字符串
        # 2. 连续字符串的可能性答案
        # 将结果相乘即可
        dp_3 = [1,1,2,4]
        dp_4 = [1,1,2,4]
        for i in range(4, min(len(pressedKeys)+1, 10**5+1)):
            dp_3.append((dp_3[i-3]+dp_3[i-2]+dp_3[i-1])%MOD)
            dp_4.append((dp_4[i-4]+dp_4[i-3]+dp_4[i-2]+dp_4[i-1])%MOD)
    
        
        def split_key(pressedKeys: str) -> List[str]:
            # 这个方法可以使用 group 方法优化
            ans = []
            prev = 0
            for i in range(len(pressedKeys)):
                curr = pressedKeys[i]
                if curr != pressedKeys[prev]:
                    ans.append(pressedKeys[prev:i])
                    prev = i
            ans.append(pressedKeys[prev:])
            # print(ans)
            return ans
        
        def count_word(word: List[str]) -> int:
            # print(word)
            char = word[0]
            if char in '79':
                ans = dp_4[len(word)]
            else:
                ans = dp_3[len(word)] 
            # print(f"{char}[{len(word)}]={ans}")
            return ans

        # words = split_key(pressedKeys)
        ans = 1
        for ch, s in groupby(pressedKeys):
            # print(ch, list(s))
            ans = ans * count_word(list(s)) %  MOD

        # for w in words:
        #     ans *= count_word(w)%(10**9 + 7) 
        # print(f"end print={ans}")
        return ans
                       
# @lc code=end
s = Solution()
a = s.countTexts("22233")
print(a)
