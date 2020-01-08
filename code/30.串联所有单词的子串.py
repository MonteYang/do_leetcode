#
# @lc app=leetcode.cn id=30 lang=python3
#
# [30] 串联所有单词的子串
#

# @lc code=start
import copy
from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        res = []
        if not words: return res
        len_sub_string = len(words[0])  # word字符串的长度
        # 用一个hash表对应word和word的个数
        hash_table = {}
        for w in words:
            if w in hash_table:
                hash_table[w] += 1
            else:
                hash_table[w] = 1
        i = 0  # 遍历所有元素的指针
        while i <= len(s) - len_sub_string*len(words) + 1:
            j = i
            # copy一个hash表作为临时
            _hash_table = copy.deepcopy(hash_table)
            while True:
                # 在当前指针i处遍历,如果hash表为空,则添加i
                if not _hash_table:
                    res.append(i)
                if s[j:j+len_sub_string] in _hash_table:
                    if _hash_table[s[j:j+len_sub_string]] == 1:
                        del _hash_table[s[j:j+len_sub_string]]
                    else:
                        _hash_table[s[j:j+len_sub_string]] -= 1
                    j = j + len_sub_string
                else:
                    break
            i += 1

        return res


# @lc code=end

if __name__ == "__main__":
    S = Solution()
    s = "wordgoodgoodgoodbestword"
    words = ["word","good","best","good"]
    print(S.findSubstring(s, words))