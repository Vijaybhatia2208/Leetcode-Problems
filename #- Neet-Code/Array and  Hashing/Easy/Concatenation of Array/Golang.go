package main

import (
	"fmt"
)

func main() {
	result := getConcatenation(([]int{1, 2, 3}))
	fmt.Println(result) // Output: [1 2 3 1 2 3]
}

func getConcatenation(nums []int) []int {
	ans := make([]int, len(nums))
	copy(ans, nums)
	ans = append(ans, nums...)
	return ans
}
