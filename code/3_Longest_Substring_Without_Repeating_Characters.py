# coding: utf-8
'''
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 

Example 2:
Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

'''


class Solution:
    def lengthOfLongestSubstring(self, s):
        window = []
        cur_length = 0
        max_length = 0
        for i in range(len(s)):
            if s[i] in window:
                window = window[window.index(s[i])+1:]
            window.append(s[i])
            cur_length = len(window)
            if cur_length > max_length:
                max_length = cur_length

        return max_length
