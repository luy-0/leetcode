/*
 * @lc app=leetcode.cn id=1 lang=golang
 *
 * [1] 两数之和
 */
package main

import "fmt"

// @lc code=start
func twoSum(nums []int, target int) []int {
	// 笨蛋 用哈希表
	hash := make(map[int]int, len(nums))
	for i, v := range nums {
		if pos, ok := hash[target-v]; ok {
			return []int{i, pos}
		}
		hash[v] = i
	}
	return []int{-1, -1}
}

// @lc code=end

func main() {
	testCase1 := []int{3, 2, 4}
	target := 6
	result := twoSum(testCase1, target)
	fmt.Println(result)
}
