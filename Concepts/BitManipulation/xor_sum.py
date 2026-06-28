def xor_sum(arr):
    index = 32
    count = 0
    ans = 0
    while index > 0:
        set_bit = 0
        non_set_bit = 0
        for _, value in enumerate(arr):
            if (value & (1<<count) )> 0:
                set_bit+=1
            else:
                non_set_bit+=1

        ans += (set_bit* non_set_bit)* pow(2, count)
        count+=1
        index-=1
    
    print(ans*2)

xor_sum([3,5,6,8,2])