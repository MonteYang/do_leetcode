#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start


class Solution:
    def longestCommonPrefix(self, strs):
        """获得 list of string 的公共子串

        Args:
            strs (list): a list of string

        Returns:
            str: 公共自创
        """
        if not strs:
            return ""
        commom = strs[0]
        for i in range(1, len(strs)):
            commom = self.getCommonPrefix(commom, strs[i])
            if commom == "":
                return ""

        return commom

    def getCommonPrefix(self, str1, str2):
        """返回str1和str2的公共子串

        Args:
            str1 (string): 第一个字符串
            str2 (string): 第二个字符串

        Returns:
            string: 公共字符串
        """
        i = 0
        while i < min(len(str1), len(str2)):
            if str1[i] == str2[i]:
                i += 1
            else:
                break

        return str1[:i]
# @lc code=end
