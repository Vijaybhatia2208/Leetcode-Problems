class Solutions {

  AllPossibleStrings(s: string){
    let bitSize: number =  1<<s.length;
    let answer: string[] = [];
    for(let index: number=1; index < bitSize; index++) {
      let val: string = "";
      for(let j: number = 0; j < s.length; j++) {
        if(index & (1<<j)) val += s[j];
      }
      answer.push(val);
    }
    return answer.sort();
  }
}