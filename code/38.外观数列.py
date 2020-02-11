#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
File: 38.外观数列.py
Created: 2020-01-22 16:16:19
Author : Yangmaonan
Email : 59786677@qq.com
Description: 
'''

#
# @lc app=leetcode.cn id=38 lang=python3
#
# [38] 外观数列
#
# https://leetcode-cn.com/problems/count-and-say/description/
#
# algorithms
# Easy (53.98%)
# Likes:    382
# Dislikes: 0
# Total Accepted:    68.5K
# Total Submissions: 126.4K
# Testcase Example:  '1'
#
# 「外观数列」是一个整数序列，从数字 1 开始，序列中的每一项都是对前一项的描述。前五项如下：
#
# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
#
#
# 1 被读作  "one 1"  ("一个一") , 即 11。
# 11 被读作 "two 1s" ("两个一"）, 即 21。
# 21 被读作 "one 2",  "one 1" （"一个二" ,  "一个一") , 即 1211。
#
# 给定一个正整数 n（1 ≤ n ≤ 30），输出外观数列的第 n 项。
#
# 注意：整数序列中的每一项将表示为一个字符串。
#
#
#
# 示例 1:
#
# 输入: 1
# 输出: "1"
# 解释：这是一个基本样例。
#
# 示例 2:
#
# 输入: 4
# 输出: "1211"
# 解释：当 n = 3 时，序列是 "21"，其中我们有 "2" 和 "1" 两组，"2" 可以读作 "12"，也就是出现频次 = 1 而 值 = 2；类似
# "1" 可以读作 "11"。所以答案是 "12" 和 "11" 组合在一起，也就是 "1211"。
#
#


# @lc code=start
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        s = '1*'
        while n > 1:
            s = self.util(s)
            n -= 1
        return s[:-1]

    def util(self, s):
        """ 输入s, 返回s的下一个外观数列, 注意s的最后一个字符是'*'.
        
        Args:
            s (string): 以 * 结尾的字符串
        
        Returns:
            string: 下一个外观数列
        """
        res = ''
        cnt = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                cnt += 1
            else:
                res += (str(cnt) + s[i - 1])
                cnt = 1
        s = res + '*'
        return s


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print("res", s.countAndSay(1))
