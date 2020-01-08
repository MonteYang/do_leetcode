/*
 * @lc app=leetcode.cn id=28 lang=cpp
 *
 * [28] 实现 strStr()
 */

// @lc code=start
#include <string>
using namespace std;

class Solution {
public:
  int strStr(string haystack, string needle) {
    if (needle.empty())
      return 0;
    for (int i = 0; i < haystack.size() - needle.size() + 1; i++) {
      if (haystack.substr(i, needle.size()) == needle) {
        return i;
      }
    }
    return -1;
  }
};

// @lc code=end
