#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#
# https://leetcode-cn.com/problems/reverse-integer/description/
#
# algorithms
# Easy (31.67%)
# Total Accepted:    85.1K
# Total Submissions: 268.7K
# Testcase Example:  '123'
#
# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
# 
# 示例 1:
# 
# 输入: 123
# 输出: 321
# 
# 
# 示例 2:
# 
# 输入: -123
# 输出: -321
# 
# 
# 示例 3:
# 
# 输入: 120
# 输出: 21
# 
# 
# 注意:
# 
# 假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
# 
#
class Solution:
    def reverse(self, x: int) -> int:
        # 方法一：
        # 整数转字符串，反转字符串，再转整数
        # result = int(str(abs(x))[::-1])
        # if x > 0 and result < 2**31:
        #     return result
        # if x < 0: 
        #     result = - result
        #     if result > -2 ** 31:
        #         return result
        # return 0 
        # 方法二：
        # 正常整数实现方法，利用余数*10累加的方法完成。
        # 需要注意的是，python对整数除法采用“向下取整”机制，所以正数和负数要区别运算
        result = 0
        flag = 1 if x > 0 else -1
        x = abs(x)
        while x!=0:
            result = result*10+x%10
            x = x//10
        if (-2**31) <result <(2**31-1):
            return result*flag
        else:
            return 0



