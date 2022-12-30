class BubSort:
    def Bsort( self,arr):
        flag = True
        for i in range(len(arr)):
            for j in range(1,len(arr)-i):
                if arr[j] < arr[j-1]:
                    arr[j],arr[j-1] = arr[j-1],arr[j]
                    flag = False
            if flag:
                break
        return arr
a = BubSort()
arr = [5,4,3,2,1]
print(a.Bsort(arr))
