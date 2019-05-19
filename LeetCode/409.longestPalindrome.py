# -*- coding:utf-8 -*-
"""
@author:xxy
@time:2019/2/18 9:31
@description:
"""

def longestPalindrome(s):
    if(len(s)<2 or s == s[::-1]):
        return s
    n = len(s)
    start,maxlen = 0,1
    for i in range(1,n):
        odd = s[i-maxlen-1:i+1]



