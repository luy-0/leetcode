/*
 * @lc app=leetcode.cn id=165 lang=golang
 *
 * [165] 比较版本号
 */

package main

import (
	"strconv"
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
	} else if n1 > n2 {
		for i := 0; i < n1-n2; i++ {
			slice2 = append(slice2, "0")
		}
	}

	for i := 0; i < len(slice1); i++ {
		str1 := slice1[i]
		str2 := slice2[i]
		int1, int2 := 0, 0

		// Atoi 函数
		// strconv.Atoi(s string) (int, error)
		int1, _ = strconv.Atoi(str1)
		int2, _ = strconv.Atoi(str2)
		// 手动实现:
		// for j := 0; j < len(str1); j++ {
		// 	int1 = int1*10 + int(str1[j]-'0')
		// }
		// for j := 0; j < len(str2); j++ {
		// 	int2 = int2*10 + int(str2[j]-'0')
		// }

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
	version1 := "1.0.1"
	version2 := "1.2"
	t := []string{version1, version2}
	ret := compareVersion(t[0], t[1])
	println(ret)
}
