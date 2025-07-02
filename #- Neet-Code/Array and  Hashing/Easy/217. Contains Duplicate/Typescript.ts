/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums: number[]): boolean {
  const obj: any = {}
  for(let i =0; i<nums.length; i++) {
      obj[nums[i]] = obj[nums[i]] ? obj[nums[i]]+1 : 1
      if(obj[nums[i]] > 1) return true 
  }
  return false
};