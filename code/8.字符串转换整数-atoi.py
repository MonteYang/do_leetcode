#
# @lc app=leetcode.cn id=8 lang=python3
#
# [8] 字符串转换整数 (atoi)
#

# @lc code=start
# class Solution:
#     def myAtoi(self, str):
#         flag_find_first = True
#         sign = 1
#         res = 0
#         for c in str:
#             # 找第一个符号, 找到空字符
#             if flag_find_first and c == " ":
#                 continue
#             else:
#                 # 找第一个符号, 找到负号, 就不用找第一个符号了
#                 if flag_find_first and c == "-":
#                     sign = -1
#                     flag_find_first = False
#                     continue
#                 # 找第一个符号, 找到正号, 就不用找第一个符号了
#                 if flag_find_first and c == "+":
#                     sign = 1
#                     flag_find_first = False
#                     continue
#                 asc = ord(c)
#                 if 48 <= asc and asc <= 57:
#                     flag_find_first = False
#                     res = int(res*10 + asc-48)
#                     if sign == 1 and res > (2**31 - 1):
#                         res = 2**31 - 1
#                         break
#                     if sign == -1 and res > 2**31:
#                         res = 2**31
#                         break
#                 else:
#                     break
#         return sign * res

class Solution:
    def myAtoi(self, str):
        flag_find_first = True
        sign = 1
        res = 0
        for c in str:
            asc = ord(c)
            # 找第一个符号, 
            if flag_find_first:
                # 空字符, 跳过
                if asc == 32: continue
                # 负号, 已找到第一个符号
                elif asc == 45:
                    sign = -1
                    flag_find_first = False
                    continue
                # 正号, 已找到第一个符号
                elif asc == 43:
                    sign = 1
                    flag_find_first = False
                    continue
                # 数字字符
                elif 48 <= asc and asc <= 57:
                    flag_find_first = False
                    res = asc-48
                    continue
                # 非上述字符
                else:
                    break
            # 已有第一个符号(正号或符号或数字)的前提下, 接下来只能是数字符号, 如果不是则break
            else:
                if 48 <= asc and asc <= 57:
                    res = int(res*10 + (asc-48))
                    if sign == 1 and res > (2**31 - 1):
                        res = 2**31 - 1
                        break
                    if sign == -1 and res > 2**31:
                        res = 2**31
                        break
                else:
                    break

        return sign * res
        
# @lc code=end

