/**
 * @param {number[]} nums
 * @return {number}
 */
const countPrimeFactors = (number) => {
  let obj = {}
  
  // Checking if number divisible by 6
  while(number%2===0) {
    obj[2] = 1;
    number= number/2;
  }

  while(number%3===0) {
    obj[3] = 1;
    number=number/3;
  }

  for(let i=5; i*i<=number; i=i+6) {
    while(number%i===0) {
      obj[i]=1;
      number=number/i;
    }
    while(number%(i+2)===0) {
      obj[i+2]=1;
      number=number/(i+2);
    }
  }

  if(number> 3) obj[number]=1
  return obj;
}


var distinctPrimeFactors = function(nums) {
  let answer = {};
  nums.map((number) => {
    if(number> 1) {
      answer = {...answer, ...countPrimeFactors(number)}
    }
  });
  return Object.keys(answer).length
};

console.log(distinctPrimeFactors([2,4, 5, 450, 34]));