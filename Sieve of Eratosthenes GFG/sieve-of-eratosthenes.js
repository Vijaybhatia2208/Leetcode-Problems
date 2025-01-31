class Solution {

  sieveOfEratosthenes(N){
    let isPrime = Array(N+1).fill(true);
    for(let i=2; i*i <= N; i++) {
      if(isPrime[i]) {
        for(let j=2*i; j<=N; j=j+i) {
          isPrime[j] = false;
        }
      }
    }
    let ans=[]
    for ( let  i=2; i<=N;i++) {
      if(isPrime[i]) {
        ans.push(i);
      }
    }
    return ans;
  }
}