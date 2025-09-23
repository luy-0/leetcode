#
# @lc app=leetcode.cn id=1328 lang=python3
#
# [1328] 破坏回文串
#

# @lc code=start
class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        new_str = list(palindrome)
        if len(palindrome) <= 1 :
            return ''
        for index in range(len(palindrome)//2):
            x = palindrome[index]
            if x != 'a':
                new_str[index] = 'a'
                return ''.join(new_str)

        new_str[-1] = 'b'
        return ''.join(new_str)
        
# @lc code=end

s = Solution()
print(s.breakPalindrome("aaa"))
print(s.breakPalindrome("aa"))
print(s.breakPalindrome("a"))
print(s.breakPalindrome("aba"))
print(s.breakPalindrome("aabbaa"))
print(s.breakPalindrome("aabcbaa"))
print(s.breakPalindrome("ddbcbdd"))
print(s.breakPalindrome("ddbbdd"))