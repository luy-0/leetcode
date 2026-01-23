/*
 * @lc app=leetcode.cn id=80 lang=golang
 *
 * [80] 删除有序数组中的重复项 II
 */
package main

// @lc code=start
func removeDuplicates(nums []int) int {
	if len(nums) < 3 {
		return len(nums)
	}
	slow, fast := 2, 2
	for fast < len(nums) {
		if nums[fast] == nums[slow-2] {
			fast++
		} else {
			nums[slow] = nums[fast]
			fast++
			slow++
		}
	}
	return slow
}

// @lc code=end
