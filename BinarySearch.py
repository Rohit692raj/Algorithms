class BinarySearch:
    def BSearch( self, arr, target ):
        arr.sort()
        start = 0
        end = len(arr) - 1
        while start <= end:
            mid = (end + (end - start)) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return -1
a = BinarySearch()
arr = [2,34,5,23,12,4,1]
target = 12
print(a.BSearch(arr,target))

