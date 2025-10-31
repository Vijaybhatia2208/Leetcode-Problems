/*
  Question Link : https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
  Question Name : 448. Find All Numbers Disappeared in an Array
  Difficulty: Easy

  Main Content: 
  Ex:  [4, 3, 2, 7, 8, 2, 3, 1]
  nums[] ->  0 <= element < n
  n is length of nums
  we are marking 
  nums[4-1] = -1 => 3
  nums[3-1] = -1 => 2
  nums[2-1] = -1 => 1
  nums[7-1] = -1 => 6
  nums[8-1] = -1 => 7
  nums[2-1] = -1  => 1
  nums[3-1] = -1 => 2
  nums[1-1] = -1 =>0
  
  nums = [-1, -1, -1, -1, 4, 5, -1,-1  ]
  ans i+1, 4+1, 5+1 -> [5, 6]

*/

// Code
function findDisappearedNumbers(nums: number[]): number[] {
  const ans = [];
  for (let i = 0; i < nums.length; i++) {
    const pointing_index = nums[i] > 0 ? nums[i] - 1 : -nums[i] - 1;
    if (nums[pointing_index] > 0) {
      nums[pointing_index] = -1 * nums[pointing_index];
    }
  }
  console.log(nums);

  for (let i = 0; i < nums.length; i++) {
    if (nums[i] > 0) {
      ans.push(i + 1);
    }
  }
  return ans;
}

console.log(findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]));
