/*
 * @lc app=leetcode.cn id=88 lang=golang
 *
 * [88] 合并两个有序数组
 */

package main

import "fmt"

// @lc code=start
func merge(nums1 []int, m int, nums2 []int, n int) {
	// 如果从头开始的话会覆盖原有的数据
	// 所以从后往前
	var p, q = m - 1, n - 1
	var tail = m + n - 1
	for p >= 0 && q >= 0 {
		if nums1[p] > nums2[q] {
			nums1[tail] = nums1[p]
			p--
		} else {
			nums1[tail] = nums2[q]
			q--
		}
		tail--
	}
	if q >= 0 {
		// 说明 num2 还有剩余，直接一股脑塞进去
		copy(nums1[0:q+1], nums2[0:q+1])
	}
	// 如果 num1 还有剩余，不用管，它本来就在正确的位置上
	return
}

// @lc code=end

func main() {
	// testCase := [][]int{
	// 	{1, 2, 3, 0, 0, 0},
	// 	{2, 5, 6, 0, 0, 0},
	// }
	// m := 3
	// n := 3
	testCase := [][]int{
		{0},
		{1},
	}
	m := 0
	n := 1
	merge(testCase[0], m, testCase[1], n)
	fmt.Println(testCase[0])
}
