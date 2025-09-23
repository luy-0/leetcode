#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest_word = strs[0]
        for str in strs:
            if len(str) < len(shortest_word):
                shortest_word = str
        ret = ""
        index = 0
        for c in shortest_word:
            for s in strs:
                if s[index] == c:
                    continue
                else: 
                    return ret
            ret += c
            index += 1
        return ret
# @lc code=end

