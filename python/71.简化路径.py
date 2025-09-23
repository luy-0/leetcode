#
# @lc app=leetcode.cn id=71 lang=python3
#
# [71] 简化路径
#

# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        path_list = path.split('/')
        vaild_path = []
        for p in path_list:
            if not p or p == '.':
                continue
            if p == '..':
                if vaild_path:
                    vaild_path.pop()
                continue
            vaild_path.append(p)
        
        
        return '/'+'/'.join(vaild_path)
# @lc code=end


s = Solution()
a = s.simplifyPath("/home/")
print(a)
a = s.simplifyPath("/home//foo/")
print(a)
a = s.simplifyPath("/home/user/Documents/../Pictures")
print(a)
a = s.simplifyPath("/../")
print(a)
a = s.simplifyPath("/.../a/../b/c/../d/./")
print(a)

