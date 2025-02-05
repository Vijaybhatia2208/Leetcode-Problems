
class CountTotalSetBits {
  //Function to return sum of count of set bits in the integers from 1 to n.
  countSetBits(N: number): number {
    var storeBit:number[] = [0];
    // 255 => 11111111  8 - bit any 8- bit number & 255 = number itself
    for (let i:number = 1; i< 256; i++) {
      storeBit[i] = storeBit[i & i-1] + 1;
    }

    let ans = 0;

    for (let i:number = 1; i<=N; i++) {
      ans = ans + storeBit[i&255] + storeBit[i>>8 & 255] + storeBit[i>>16 & 255] + storeBit[i>>24 & 255];
    }
    return ans;
  }
}

var solution = new CountTotalSetBits();
console.log(solution.countSetBits(4))
console.log(solution.countSetBits(17))