/*
 * @lc app=leetcode.cn id=344 lang=golang
 *
 * [344] 反转字符串
 */

// @lc code=start
package main

import "fmt"

func reverseString(s []byte) {
	var p, q = 0, len(s) - 1
	for p < q {
		tmp := s[q]
		s[q] = s[p]
		s[p] = tmp
		p++
		q--
	}
	return
}

// @lc code=end

func main() {
	testCase := []byte{'h', 'e', 'l', 'l', 'o'}
	reverseString(testCase)
	fmt.Println(string(testCase))
}
