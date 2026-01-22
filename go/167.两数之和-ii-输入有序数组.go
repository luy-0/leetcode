/*
 * @lc app=leetcode.cn id=167 lang=golang
 *
 * [167] 两数之和 II - 输入有序数组
 */
package main

import "fmt"

// @lc code=start
func twoSum(numbers []int, target int) []int {
	// 有序的， 那么左右指针即可
	p, q := 0, len(numbers)-1
	for p < q {
		sum := numbers[p] + numbers[q]
		if sum == target {
			// 注意这玩意从下标 1 开始
			return []int{p + 1, q + 1}
		}
		if sum > target {
			q--
			continue
		}
		p++
	}
	return []int{-1, -1}
}

// @lc code=end
func main() {
	numbers := []int{2, 7, 11, 15}
	target := 9
	result := twoSum(numbers, target)
	fmt.Println(result)
}
