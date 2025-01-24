const checkPrime = (n) => {
  if (n%2 ==0) return false;
  if (n%3 == 0) return false;

  for(let i=5; i*i<=n; i=i+6) {
    if (n%i === 0 || (n%(i+2))=== 0) return false;
  }
  return true;
}

var countPrimes = function(n) {
    n=n-1;
    let ans = 2;

    if(n<=2) return 0;
    if(n <=2 ) return 1;
    if(n>2 & n<5) return 2;

    for(let i=5; i<=n; i=i+6) {
        console.log(i);
        if(checkPrime(i)) ans++;
        if(i+2 <= n){
            if(checkPrime(i+2)) ans++;
        }
    }
    return ans;
};

console.log(countPrimes(6))