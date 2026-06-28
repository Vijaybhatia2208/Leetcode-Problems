class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        eliminate = A[:]

        index = 32

        while index>= 0  :
            set_bit = 0
            set_bit_arr = []
            for _,val in enumerate(eliminate):
                if val & (1<<index) > 0:
                    set_bit+=1
                    set_bit_arr.append(val)
            
            if set_bit > 1 :
                eliminate= set_bit_arr
            
            index-=1


        if len(eliminate) == 0 :
            return 0
        
        ans = eliminate[0]

        # print(eliminate)

        for _,val in enumerate(eliminate):
            ans = ans & val

        return ans