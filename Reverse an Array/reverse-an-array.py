class ReverseAnArray:

  @staticmethod
  def recursive( arr, start=0, end=None):
    if end == None:
      return arr
    if start == 0:
      end=len(arr)-1

    temp = arr[start]
    arr[start]  = arr[end]
    arr[end] = temp

    arr[start], arr[end] = arr[end], arr[start] 
    return ReverseAnArray.recursive(arr, start+1, end-1); 

print(ReverseAnArray.recursive([2,3,9,8,14,5]))