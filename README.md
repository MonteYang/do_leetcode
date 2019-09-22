- [Leetcode](#leetcode)
  - [1. Two Sum](#1-two-sum)
  - [2. Add Two Numbers](#2-add-two-numbers)
# Leetcode

## 1. Two Sum

- 使用哈希表,  **查找 `target - num` 是否存在于字典中, 使查询速度更快, 为O(1).** 
  - 在Python中`hash table`使用字典实现, 交换原`list`中的`idx`和`num`的位置, 将`num`作为字典中的`key`, `idx`作为字典的`value`.

## 2. Add Two Numbers

- 技巧: 迭代2个链表的同时,顺便进行计算,使算法复杂度大大降低.