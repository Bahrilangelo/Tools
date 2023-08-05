arr = [2,8,5,3,9,4,1]

for i in range(0,len(arr)):
    for k in range(i + 1,len(arr)):
        if arr[k] > arr[i]:
            continue
        else:
            arr[k], arr[i] = arr[i], arr[k]

print(arr)