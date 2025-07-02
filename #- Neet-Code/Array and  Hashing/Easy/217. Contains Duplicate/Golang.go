package main

import (
	"fmt"
)

func main() {
	result := containsDuplicate(([]int{1, 2, 3}))
	fmt.Println(result) // Output: [1 2 3 1 2 3]
}

func containsDuplicate(nums []int) bool {
	value := make(map[int]int)
	for i := 0; i < len(nums); i++ {
		val, exists := value[nums[i]]
		if exists {
			value[nums[i]] = val + 1
		} else {
			value[nums[i]] = 1
		}

		if value[nums[i]] > 1 {
			return true
		}

	}
	return false
}
