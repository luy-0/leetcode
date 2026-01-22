/*
 * @lc app=leetcode.cn id=3 lang=golang
 *
 * [3] 无重复字符的最长子串
 */
package main

import "fmt"

// @lc code=start
func lengthOfLongestSubstring(s string) int {
	set := make(map[byte]int)
	left, right := 0, 0
	maxLen := 0
	for right < len(s) {
		if set[s[right]] == 0 {
			// do nothing
		} else {
			// 出现重复字符，更新最大长度
			maxLen = max(maxLen, right-left)
			for set[s[right]] > 0 {
				set[s[left]] -= 1
				left++
			}
		}
		set[s[right]] += 1
		right++
	}
	maxLen = max(maxLen, right-left)
	return maxLen
}

// @lc code=end

func main() {
	s := "abcabcbb"
	s = "a"

	length := lengthOfLongestSubstring(s)
	fmt.Println(length)
}
