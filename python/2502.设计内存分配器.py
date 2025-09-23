#
# @lc app=leetcode.cn id=2502 lang=python3
#
# [2502] 设计内存分配器
#

# @lc code=start

class Allocator:
    def __init__(self, n: int):
        self.memo = [0] * n

    def __str__(self):
        return f"memo: {self.memo}"

    def allocate(self, size: int, mID: int) -> int:
        start_index = 0
        count = 0
        for index in range(len(self.memo)):
            if self.memo[index] != 0:
                count = 0
                start_index = index+1
            else:
                count += 1
            if count == size:
                break
        if start_index + size > len(self.memo):
            return -1
           
        for i in range(size):
            self.memo[start_index+i] = mID
        # print(self)
        return start_index      

    def freeMemory(self, mID: int) -> int:
        count = 0
        for index in range(len(self.memo)):
            if self.memo[index] == mID:
                self.memo[index] = 0
                count += 1
        # print(self)
        return count
        


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.freeMemory(mID)
# @lc code=end

obj = Allocator(10)
print(obj.allocate(1,1))
print(obj.allocate(1,2))
print(obj.allocate(1,3))
print(obj.freeMemory(2))
print(obj.allocate(3,4))
print(obj.allocate(1,1))
print(obj.allocate(1,1))
print(obj.freeMemory(1))
print(obj.allocate(10,2))
print(obj.freeMemory(7))

# obj = Allocator(2)
# print(obj.freeMemory(8))
# print(obj.freeMemory(10))
# print(obj.allocate(5,10))
# print(obj.freeMemory(10))