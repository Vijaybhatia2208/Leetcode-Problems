class MoveZeroes:
	@staticmethod
	def iterative(arr):
		n= len(arr)
		pos = 0
		for i in range(n):
			if(arr[i] != 0):
				temp = arr[pos]
				arr[pos] = arr[i]
				arr[i] = temp
				pos = pos+1
		return arr
	@staticmethod
	def recursive(arr, pos=0, index=0):
		if index == len(arr):
			return arr
		if arr[index] !=0:
			temp = arr[pos]
			arr[pos] = arr[index]
			arr[index] = temp
			pos = pos + 1
		return MoveZeroes.recursive(arr, pos, index+1)


print(MoveZeroes.recursive([0,1,0,3,12]))
