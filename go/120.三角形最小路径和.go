/*
 * @lc app=leetcode.cn id=120 lang=golang
 *
 * [120] 三角形最小路径和
 */
package main

import (
	"fmt"
	"math"
)

// @lc code=start
func minimumTotal(triangle [][]int) int {
	f := make([][]int, len(triangle))

	// 表示到 i,j 时需要的最小步数
	// f(i,j) = f(i-1,j) + triangle[i][j]
	// 		  = f(i-1,j-1) + triangle[i][j+1]
	for i := 0; i < len(triangle); i++ {
		f[i] = make([]int, len(triangle[i]))
		for j := 0; j < len(triangle[i]); j++ {
			if i == 0 && j == 0 {
				f[i][j] = triangle[i][j]
				continue
			}
			// 边界位置
			if j == 0 {
				f[i][j] = f[i-1][j] + triangle[i][j]
				continue
			}
			if j == len(triangle[i])-1 {
				f[i][j] = f[i-1][j-1] + triangle[i][j]
				continue
			}
			// 中间位置
			if f[i-1][j] > f[i-1][j-1] {
				f[i][j] = f[i-1][j-1] + triangle[i][j]
			} else {
				f[i][j] = f[i-1][j] + triangle[i][j]
			}
		}
	}
	ans := math.MaxInt
	ground := len(triangle) - 1
	for k := 0; k < len(triangle[ground]); k++ {
		if f[ground][k] < ans {
			ans = f[ground][k]
		}
	}
	return ans
}

// @lc code=end

func main() {
	// testCase := [][]int{
	// 	{2},
	// 	{3, 4},
	// 	{6, 5, 7},
	// 	{4, 1, 8, 3},
	// }
	testCase := [][]int{
		{-10},
	}
	fmt.Println(minimumTotal(testCase))
}
