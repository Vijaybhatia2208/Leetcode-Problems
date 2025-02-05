function countBits(n: number): number[] {
  var storeBit:number[] = [0];
  // 255 => 11111111  8 - bit any 8- bit number & 255 = number itself
  for (let i:number = 1; i< 256; i++) {
    storeBit[i] = storeBit[i & i-1] + 1;
  }

  let ans:number[] = [0];

  for (let i:number = 1; i<=n; i++) {
    ans.push(storeBit[i&255] + storeBit[i>>8 & 255] + storeBit[i>>16 & 255] + storeBit[i>>24 & 255]);
  }

  return ans;
};

console.log(countBits(2));
console.log(countBits(5));