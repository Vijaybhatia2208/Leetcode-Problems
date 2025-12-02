/*
    Problem Statement : https://leetcode.com/problems/two-sum/description/
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    You can return the answer in any order.
    
    Ex.
    nums = [2,7,11,15], target = 9
    
    1 solution
    same element is not used twice 


    stroing value in hash map 
    {
        1: true,
        7: true,
        11: true,
        15: true,
    }

*/

function twoSum(nums: number[], target: number): number[] {
  let hashMap: any = {};
  let len = nums.length;

  for (let index = 0; index < len; index++) {
    hashMap[nums[index]] = index;
  }

  console.log(hashMap);
  for (let index = 0; index < len; index++) {
    const subtractedNum: any = String(target - nums[index]);
    console.log(subtractedNum, hashMap?.[subtractedNum]);
    const hashReturn = hashMap?.[subtractedNum];
    if (
      (hashReturn || (hashReturn === 0 && index !== 0)) &&
      hashReturn !== index
    ) {
      return [index, hashMap?.[subtractedNum]];
    }
  }
  return [];
}

console.log(twoSum([2, 7, 11, 15], 9));
console.log(twoSum([3, 2, 4], 6));
console.log(twoSum([3, 3], 6));
console.log(twoSum([1, 3, 4, 2], 6));
