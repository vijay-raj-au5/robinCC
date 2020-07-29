def search(arr, target):
    if not arr:
        return -1

    low, high = 0 , len(arr) - 1

    while low <= high:
        mid = (low+high) // 2
        if target == arr[mid]:
            return mid

        if arr[low] <= arr[mid]:
            if arr[low] <= target <= arr[mid]:
                high = mid - 1
            else :
                low = mid + 1

        else:
            if arr[mid] <= target <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1
        
    return -1

arr = list(map(int, input("Enter a number: ").strip().split()))
target = int(input("Enter taget value: "))
print(search(arr,target))



