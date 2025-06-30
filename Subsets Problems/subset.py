class Subset:
  def solution(self, str, i=0, curr=''):
    if i == len(str):
      print(curr)
      return

    self.solution(str, i+1, curr)
    self.solution(str, i+1, curr+ str[i])

subset = Subset()
subset.solution('ABC')