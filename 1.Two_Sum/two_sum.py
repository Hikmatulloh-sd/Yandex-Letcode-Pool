def two_sum(arr,target):
    num_to_index = {}

    for i,num in enumerate(arr):
        complement = target - num
        if complement in num_to_index:
            return num_to_index[complement],i
        
        num_to_index[num] = i

arr = [2,3,4,5]
print(two_sum(arr,9))