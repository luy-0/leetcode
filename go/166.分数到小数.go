/*
 * @lc app=leetcode.cn id=166 lang=golang
 *
 * [166] 分数到小数
 */
package main

import (
	"fmt"
	"math"
	"strconv"
)

// @lc code=start
func fractionToDecimal(numerator int, denominator int) string {
	if numerator == 0 {
		return "0"
	}
	// 不会出现分母为0的情况

	sign := ""
	if numerator*denominator < 0 {
		sign = "-"
	}
	numerator = int(math.Abs(float64(numerator)))
	denominator = int(math.Abs(float64(denominator)))

	// 整数部分
	// / 符号表示整数除法
	// % 符号表示取余数
	// 例如：7/3 = 2 ... 1
	intPart := numerator / denominator
	remainder := numerator % denominator
	if remainder == 0 {
		// if 没有余数，直接返回整数部分
		return sign + strconv.Itoa(intPart)
	}

	// 接着来处理小数部分
	remsinderSet := map[int]int{}
	// 表示某个余数第一次出现的位置
	desPart := ""
	index := 0

	for remainder != 0 {
		if pos, ok := remsinderSet[remainder]; ok {
			// 出现过 说明出现循环节
			desPart = desPart[:pos] + "(" + desPart[pos:] + ")"
			break
		}
		remsinderSet[remainder] = index
		remainder *= 10
		newInt := remainder / denominator
		desPart += strconv.Itoa(newInt)

		remainder = remainder % denominator
		index++
	}

	return fmt.Sprintf("%s%d.%s", sign, intPart, desPart)
}

// @lc code=end

func main() {
	fmt.Println(fractionToDecimal(1, 2))

	fmt.Println(fractionToDecimal(4, 333))
	fmt.Println(fractionToDecimal(9, 8))
	fmt.Println(fractionToDecimal(-3, 14))

}
