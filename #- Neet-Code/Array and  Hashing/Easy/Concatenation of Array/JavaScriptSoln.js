/**
 * @param {number[]} nums
 * @return {number[]}
 * https://leetcode.com/problems/concatenation-of-array/description/
 */
var getConcatenation = function(nums) {
  return [...nums, ...nums];
};