#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#
# https://leetcode-cn.com/problems/palindrome-number/description/
#
# algorithms
# Easy (56.07%)
# Total Accepted:    74.4K
# Total Submissions: 132.8K
# Testcase Example:  '121'
#
# 判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
# 
# 示例 1:
# 
# 输入: 121
# 输出: true
# 
# 
# 示例 2:
# 
# 输入: -121
# 输出: false
# 解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
# 
# 
# 示例 3:
# 
# 输入: 10
# 输出: false
# 解释: 从右向左读, 为 01 。因此它不是一个回文数。
# 
# 
# 进阶:
# 
# 你能不将整数转为字符串来解决这个问题吗？
# 
#
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 方法一：类似于整数反转，将整数转化为字符串
        # return str(x)==str(x)[::-1]
        # 方法二：重复比较整数首尾两个值是否相等，不同则False
        # 方法三：反转一半数字
        # if x<0 or (x%10 == 0 and x!=0):
        #     return False
        # y = 0
        # while (x>y):
        #     y = x%10+y*10
        #     x = x//10 #python数据使用前是不用定义数据类型的，所以如果执行x/10操作，就算x是一个整数，返回的也会是一个小数，所以要用到取整函数。
        # return x==y or x==y//10
        # 方法四：将整数反转
       

