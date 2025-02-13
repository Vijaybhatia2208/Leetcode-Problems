class RopeCutting {
    RopeCutting(arr: any) {
        arr.sort((a: any, b: any) => a - b); // Sort the array in ascending order
        let j = 0;
        let n = arr.length;
        let total = n - 1;
        
        for (let i = 1; i < n; i++) {
            if (arr[i] !== arr[i - 1]) {
                arr[j] = n - i;
                j++;
            }
        }
        
        return arr.slice(0, j);
  }
}