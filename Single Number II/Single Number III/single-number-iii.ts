function singleNumber(nums: number[]): number[] {
  let ans: number[]= [];

  for(let i:number=0; i<nums.length; i++) {
    let test : boolean = true;
    for(let j:number=0; j< nums.length; j++) {
        if ((j!== i) && (nums[i] === nums[j])) test = false 
    }
    test && ans.push(nums[i])
  } 
  return ans;
};

