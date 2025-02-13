def two_sum(arr,target):
    for i in range(len(arr)):
        for j in range(1,len(arr)):
            if arr[i] + arr[j] == target:
                return arr.index(arr[i]),arr.index(arr[j])

arr = [2,3,4,3]
print(two_sum(arr,7))