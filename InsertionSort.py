class ISort:
    def InsertionSort( self,arr):
        for i in range(len(arr) - 1):
            x = i + 1
            for j in reversed(range(i+1)):
                if arr[x] < arr[j]:
                    arr[j],arr[x] = arr[x],arr[j]
                    x = j
        return arr
a = ISort()
arr = [5, -2, 23, 7, 87, -42, 509 ]
print(a.InsertionSort(arr))
