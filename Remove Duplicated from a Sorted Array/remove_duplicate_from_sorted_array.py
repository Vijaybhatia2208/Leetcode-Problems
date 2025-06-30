class RemoveDuplicated:
	@staticmethod
	def recursive(arr, index=1, count=1):
		if index == len(arr):
			return arr, count
		if arr[index] != arr[index-1]:
			arr[count] = arr[index]
			count= count+1

		return RemoveDuplicated.recursive(arr, index+1, count)



arr, ans = RemoveDuplicated.recursive([1,2,2,3,3,5])

print(ans-1)
