class Josephus {

    josephus(n: number, k: number) {
        let arr: number[] = [];
        for(let index = 0; index < n; index++) arr.push(index+1)
        return this.solve(arr, k, 0)
    }
    
    solve(arr: number[], k: number, pos: number): number {
        if(arr.length === 1) {
            return arr[0]
        }
        
        pos = (pos + k -1) % arr.length
        arr.splice(pos, 1)
        return this.solve(arr, k, pos)
    }
}