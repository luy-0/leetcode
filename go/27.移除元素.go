/*
 * @lc app=leetcode.cn id=27 lang=golang
 *
 * [27] 移除元素
 */

package main

import "fmt"

// @lc code=start
func removeElement(nums []int, val int) int {
	count := 0
	fast, slow := 0, 0
	for fast < len(nums) {
		if nums[fast] == val {
			fast++
			count++
			continue
		}
		nums[slow] = nums[fast]
		slow++
		fast++
	}
	return len(nums) - count
}

// @lc code=end

func main() {
	testCase := []int{0, 1, 2, 2, 3, 0, 4, 2}
	val := 2
	result := removeElement(testCase, val)
	println(result)
	fmt.Println(testCase)
}
