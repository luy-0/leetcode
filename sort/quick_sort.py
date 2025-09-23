"""
快速排序（quick sort）是一种基于分治策略的排序算法，运行高效，应用广泛。

快速排序的核心操作是“哨兵划分”(partition)，其目标是：选择数组中的某个元素作为“基准数”，
将所有小于基准数的元素移到其左侧，而大于基准数的元素移到其右侧。
通过对于数组进行递归地完成partition行为,即可完成一次快速排序.

具体来说，哨兵划分的流程
选取数组最左端元素作为基准数，初始化两个指针 i 和 j 分别指向数组的两端。
设置一个循环，在每轮中使用 i（j）分别寻找第一个比基准数大（小）的元素，然后交换这两个元素。
这样,偏小的数就会移动到左侧,偏大的数会移动到右侧

循环执行步骤 2. ，直到 i 和 j 相遇时停止，此时这个位置为偏小数组和偏大数组的分界线.
最后将基准数交换至两个子数组的分界线,即可根据"基准数"划分了大小
"""

def partition(nums: list[int], left:int, right:int) -> int:
    # 由于是在一个数组上反复操作，所以使用 left 和 right 进行限制本次划分的范围。
    if len(nums) <= 1:
        return 0

    base = nums[left]
    i, j = left, right
    while i < j:
        while i<j and nums[j] >= base:
            j -= 1    # 从右边开始查找第一个小于base的数字
        while i<j and nums[i] <= base:
            i += 1    # 从左边开始查找第一个大于base的数字
        nums[i], nums[j] = nums[j], nums[i]
        
    # 此时，i=j，为 偏小数组和偏大数组的分界线. 将基准数与之交换
    nums[left], nums[i] = nums[i], nums[left]
    return i # 返回分界点

def quick_sort(nums: list[int], left: int=0, right: int=-2):
    if right == -2:
        right = len(nums)-1
    if left >= right:
        return 
    
    pivot = partition(nums, left, right)
    quick_sort(nums, left, pivot-1)
    quick_sort(nums, pivot + 1, right)
    
nums=[2,1,3,5,4,6,0]
quick_sort(nums)
print(nums)

"""
时间复杂度为 O(nlogn)、非自适应排序：在平均情况下，哨兵划分的递归层数为 logn ，每层中的总循环数为 n ，总体使用 nlogn 时间。
在最差情况下，每轮哨兵划分操作都将长度为 n 的数组划分为长度为 0 和 n-1 的两个子数组.
此时递归层数达到 n ，每层中的循环数为 n ，总体使用 n^2 时间。
空间复杂度为 O(n)、原地排序：在输入数组完全倒序的情况下，达到最差递归深度 n ，使用 O(n) 栈帧空间。
排序操作是在原数组上进行的，未借助额外数组。
非稳定排序：在哨兵划分的最后一步，基准数可能会被交换至相等元素的右侧。

为什么快?
首先是时间复杂度本身就是 nlogn 的.相比于选择/冒泡/插入更快.
快速排序的平均时间复杂度 nlogn 与“归并排序”和“堆排序”相同,但是通常情况下快速排序的效率更高.
出现最差情况的概率很低：虽然快速排序的最差时间复杂度为 O(n^2) ，没有归并排序稳定. 但绝大多数情况不会碰到.
缓存使用效率高：在执行哨兵划分操作时，系统可将整个子数组加载到缓存，因此访问元素的效率较高。
复杂度的常数系数小：在上述三种算法中，快速排序的比较、赋值、交换等操作的总数量最少。
"""