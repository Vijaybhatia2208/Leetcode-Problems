class Solution {
  // Function to check if Kth bit is set or not.
  checkKthBit(n: number, k: number): boolean {
      let leftbit: number = 1<<k;
      return (n & leftbit) !== 0;
  }
}

const checkCode = new Solution();

console.log(checkCode.checkKthBit(4, 0));
console.log(checkCode.checkKthBit(4, 2));
console.log(checkCode.checkKthBit(500, 3));