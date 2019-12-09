# coding: utf-8
import random
import string

"""
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"

"""


class Solution:
    def longestPalindrome(self, s):
        s = " ".join(s)
        longest_pali = ""

        for cent_idx in range(len(s)):
            pali = self.get_longest_pali(s, cent_idx)
            if len(pali) > len(longest_pali):
                longest_pali = pali

        return longest_pali

    def get_longest_pali(self, s, cent_idx):
        """返回字符串s中以索引cent_idx为中心的最长回文子串"""
        pali = s[cent_idx]
        i = 1
        while True:
            left_idx = cent_idx - i
            right_idx = cent_idx + i

            # 超出范围,跳出
            if left_idx < 0 or right_idx >= len(s):
                break

            if s[left_idx] == s[right_idx]:
                pali = s[left_idx] + pali + s[right_idx]
            else:
                break

            i += 1

        pali = pali.replace(" ", "")

        return pali


def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


if __name__ == "__main__":
    string_len = random.randint(5, 20)
    s = randomString(string_len)
    solution = Solution()
    print(s)
    print(solution.longestPalindrome(s))
