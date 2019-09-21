- [leetcode刷题总结](#leetcode%e5%88%b7%e9%a2%98%e6%80%bb%e7%bb%93)
  - [1 two sum](#1-two-sum)
# leetcode刷题总结
## 1 two sum
> 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
> 
> 给定 nums = [2, 7, 11, 15], target = 9
> 因为 nums[0] + nums[1] = 2 + 7 = 9
> 所以返回 [0, 1]

- 使用哈希表,  **查找 `target - num` 是否存在于字典中, 使查询速度更快, 为O(1).** 
  - 在Python中`hash table`使用字典实现, 交换原`list`中的`idx`和`num`的位置, 将`num`作为字典中的`key`, `idx`作为字典的`value`.
