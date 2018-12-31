# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
#
# 示例:
#
# 输入: [0,1,0,3,12]
# 输出: [1,3,12,0,0]
# 说明:
#
# 必须在原数组上操作，不能拷贝额外的数组。
# 尽量减少操作次数。
def moveZeros(nums):
    # 方法1：遇到元素0移除，在数组尾部加0
    # for i in nums:
    #     if i == 0:
    #         nums.remove(i)
    #         nums.append(0)

    # 方法2：删除后一次性补0，减少元素位移
    # 遍历nums数组获得0元素的index
    # idxs = [idx for idx, num in enumerate(nums) if num == 0]
    # for i in idxs[::-1]:
    #     nums.pop(i)
    # nums += len(idxs)*[0]

    #  记录非0元素应该换到第几个位置
    j = 0
    for i in range(len(nums)):
       if nums[i] != 0:
           nums[j],nums[i] = nums[i],nums[j]
           j += 1
    print(nums)

if __name__ == "__main__":

    nums = [0,1,0,3,12]
    moveZeros(nums)
