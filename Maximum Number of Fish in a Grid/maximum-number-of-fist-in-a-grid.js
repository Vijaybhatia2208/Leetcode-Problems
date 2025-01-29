
var findMaxFish = function(grid) {
  let rows = grid.length;
  const columns = grid[0].length;
  let visit = Array.from({length: rows}, () => Array(columns).fill(false));
  const dfs = (r, c) => {
    if(r<0 || c<0 || r>=rows || c>=columns || grid[r][c]===0 || visit[r][c]) {
      return 0;
    }
    visit[r][c] = true;
    if(r==2 && c==3) {
    }
    let res = grid[r][c];
    
    const item = [[r+1, c], [r-1, c], [r, c+1], [r, c-1]];
    for (let index in item) {
      res= res + dfs(item[index][0], item[index][1]);
    }
    return res;
  }
  
  let ans = 0;
  for (let r=0; r< rows; r++) {
    for(let c= 0; c< columns; c++) {
      if  (grid[r][c]!== 0 || !visit[r][c]) {
        ans = Math.max(ans, dfs(r,c));
      }
    }
  }
  return ans;
};

console.log(findMaxFish([
  [0,2,1,0],
  [4,0,0,3],
  [1,0,0,4]])
)