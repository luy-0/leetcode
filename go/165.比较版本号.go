/*
 * @lc app=leetcode.cn id=165 lang=golang
 *
 * [165] 比较版本号
 */

package main

import (
	"fmt"
	"strings"
)

// @lc code=start
func compareVersion(version1 string, version2 string) int {
	slice1 := strings.Split(version1, ".")
	slice2 := strings.Split(version2, ".")

	n1, n2 := len(slice1), len(slice2)
	if n1 < n2 {
		// 如果 version1 比 version2 短，则在 version1 后面补 0
		for i := 0; i < n2-n1; i++ {
			slice1 = append(slice1, "0")
		}
		for i := 0; i < n2-n1; i++ {
			slice1 = append(slice1, "0")
		}
	}
	for i := 0; i < len(slice1); i++ {
		str1 := slice1[i]
		str2 := slice2[i]
		int1, int2 := 0, 0

		for j := 0; j < len(str1); j++ {
			int1 = int1*10 + int(str1[j]-'0')
			int2 = int2*10 + int(str2[j]-'0')
		}

		if int1 > int2 {
			return 1
		} else if int1 < int2 {
			return -1
		}
	}
	return 0
}

// @lc code=end
func main() {
	a := "1.01"
	b := "1.001"
	t := []string{a, b}
	ret := compareVersion(t[0], t[1])
	fmt.Println(ret)
}
