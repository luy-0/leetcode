#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 找出字符串中第一个匹配项的下标
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
    # 显然查找子串这条题目的预期是用来编写 KMP 算法
    # 这里不编写了，但是需要掌握一下 KMP 算法的逻辑

    # 对于 needle=ababca
    ## 如果在第4位c匹配错误 那么表明前面的ss串后缀为 xxxxabab? 其中?!=c
    ## 那么接下来应当从ss后缀中的第二个a开始进行匹配，（跳过从后缀第一个b开始匹配的尝试）
    ## 需要找到对于 needle，前缀与后缀相匹配的 pmt 数组

    ### a b a b c a
    ### 0 1 2 3 4 5 (index)
    ### 0 0 1 2 0 1 (pmt)
    ### -1 0 0 1 2 0 (next) 
    ## 先看 pmt 数组
    ##   例如，pmt[2] = 1, 这是由于考察[0:2]的子串(aba)的后缀集合{a, ba} 后缀集合不包括自身
    ##   与needle的前缀集合{a, ab, aba, abab, ...}的最长交集为 a，因此 pmt[2] = 1
    ##   例如，pmt[3] = 2, 这是由于考察[0:3]的子串(abab)的后缀集合{b, ab, bab}
    ##   与needle的前缀集合{a, ab, aba, abab, ...}的最长交集为 ab，因此 pmt[3] = 2
    ## next 数组仅仅是将 pmt 数组平移1位

    ## 如果是在 j 位 失配，那么影响 j 指针回溯的位置的其实是第 j −1 位的 PMT 值
    ## 也即 第 j 位的 next 值
    
    # 参考https://www.zhihu.com/question/21923021/answer/281346746
# @lc code=end

