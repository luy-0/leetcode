#
# @lc app=leetcode.cn id=12 lang=python3
#
# [12] 整数转罗马数字
#

# @lc code=start
class Solution:
    def intToRoman(self, num: int) -> str:
        ret = ""
        while num > 0:
            # print(num, ret)
            if num >= 1000:
                num -= 1000
                ret += 'M'
                continue

            if num//100 == 4:
                num -= 400
                ret += 'CD'
                continue 
            elif num//100 == 9:
                num -= 900
                ret += 'CM'
                continue 
            elif num >= 100:
                if num >= 500:
                    num -= 500
                    ret += 'D'
                    continue 
                else:
                    num -= 100
                    ret += 'C'
                    continue 
            
            if num//10 == 4:
                num -= 40
                ret += 'XL'
                continue 
            elif num//10 == 9:
                num -= 90
                ret += 'XC'
                continue 
            elif num >= 10:
                if num >= 50:
                    num -= 50
                    ret += 'L'
                    continue 
                else:
                    num -= 10
                    ret += 'X'
                    continue 
            
            if num == 4:
                num -= 4
                ret += 'IV'
                continue
            elif num == 9:
                num -= 9 
                ret += 'IX'
                continue
            elif num>=5:
                num -= 5
                ret += 'V'
                continue
            else:
                num -= 1
                ret += 'I'
                continue
        return ret
            
                
# @lc code=end

