class SelectSort:
    def Selection_Sort( self,arr ):
        for i in range(len(arr)):
            max = 0
            last = len(arr) - i - 1
            for j in range(last + 1):
                if arr[j] > arr[max]:
                    max = j
            arr[last],arr[max] = arr[max],arr[last]
        return arr
a= SelectSort()
arr = [1,2,5,4,3]
print(a.Selection_Sort(arr))
