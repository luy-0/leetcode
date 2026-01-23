/*
 * @lc app=leetcode.cn id=141 lang=golang
 *
 * [141] 环形链表
 */

package main

type ListNode struct {
	Val  int
	Next *ListNode
}

// @lc code=start
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func hasCycle(head *ListNode) bool {
	// 快慢指针
	if head == nil || head.Next == nil {
		return false
	}
	dummy := &ListNode{
		Next: head,
	}
	fast, slow := dummy, dummy
	for fast.Next != nil && fast.Next.Next != nil {
		if fast.Next == slow || fast.Next.Next == slow {
			return true
		}
		fast = fast.Next.Next
		slow = slow.Next
	}
	// 快指针到达终点， 说明不是环
	return false

}

// @lc code=end

func main() {
	testCase := &ListNode{
		Val: 3,
		Next: &ListNode{
			Val: 2,
			Next: &ListNode{
				Val: 0,
				Next: &ListNode{
					Val: -4,
				},
			},
		},
	}
	testCase.Next.Next.Next.Next = testCase.Next
	// testCase := &ListNode{
	// 	Val: 1,
	// }
	result := hasCycle(testCase)
	println(result)
}
