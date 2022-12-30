class ISort:
    def InsertionSort( self,arr):
        for i in range(len(arr) - 1):
            for j in range(i+1,0,-1 ):
                if arr[j-1] > arr[j]:
                    arr[j],arr[j-1] = arr[j-1],arr[j]
                else:
                    break
        return arr
a = ISort()
arr = [5, -2, 23, 7, 87, -42, 509 ]
print(a.InsertionSort(arr))
