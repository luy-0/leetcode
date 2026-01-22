/*
 * @lc app=leetcode.cn id=42 lang=golang
 *
 * [42] 接雨水
 */
package main

import "fmt"

// @lc code=start
func trap(height []int) int {
	// 任何一列， 能够接的雨水 = min{左侧最高， 右侧最高} - 自身
	leftHigh := make([]int, len(height))
	rightHigh := make([]int, len(height))
	for i, v := range height {
		if i == 0 {
			leftHigh[0] = height[0]
			continue
		}
		if v > leftHigh[i-1] {
			leftHigh[i] = v
		} else {
			leftHigh[i] = leftHigh[i-1]
		}
	}
	for i := len(height) - 1; i >= 0; i-- {
		if i == len(height)-1 {
			rightHigh[i] = height[i]
			continue
		}
		v := height[i]
		if v > rightHigh[i+1] {
			rightHigh[i] = v
		} else {
			rightHigh[i] = rightHigh[i+1]
		}
	}
	// fmt.Printf("leftHigh: %v", leftHigh)
	// fmt.Printf("rightHigh: %v", rightHigh)
	var sum int
	for i := 0; i < len(height); i++ {
		if leftHigh[i] > rightHigh[i] {
			sum += rightHigh[i] - height[i]
		} else {
			sum += leftHigh[i] - height[i]
		}
	}
	return sum
}

// @lc code=end

func main() {
	// testCase := []int{0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1}
	testCase := []int{4, 2, 0, 3, 2, 5}
	result := trap(testCase)
	fmt.Println(result)
}
