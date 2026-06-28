class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0

        for _, value in enumerate(nums):
            
            xor = xor ^ value
        
        # first index where bit is 1
        print(xor)
        index = 0
        i = 0
        x=32
        while x>0:
            if xor & 1 > 0:
                index=i
                break
            xor = xor>>1
            i+=1
            x-=1

        box1 = 0
        box2 = 0
        print(index)
        for _, value in enumerate(nums):
            if value & (1<<index) > 0:
                box1 = box1 ^ value
            else :
                print(value)
                # print("box2 ", value)
                box2 = box2 ^ value
        
        return [box1, box2]
        

        
        