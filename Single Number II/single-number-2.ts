function singleNumber(nums: number[]): number {
  let ans:number = 0;
  for(let i:number= 0; i< nums.length; i++) {
      let x = 0;
      for(let j:number= 0; j<nums.length; j++) {
          if(i !=j && nums[i]==nums[j]) {
              x=1
          }
      }
      if(x===0) {
          ans = nums[i];
      }
  }
  return ans;
};