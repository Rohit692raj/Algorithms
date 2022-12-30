class Merge():
    def sortingArr(self, arr):
        n =len(arr)
        mid = (0+n) // 2
        if len(arr) == 1:
            return arr
        left = self.sortingArr(arr[0:mid])
        right = self.sortingArr(arr[mid:])
        return self.merge(arr,left,right)
    def merge( self, arr, left, right):
        i=j=0
        list = []
        while i < len(left) and j <len(right):
            if left[i] < right[i]:
                list.append(left[i])
                i += 1
            else:
                list.append(right[j])
                j += 1
        while i < len(left):
            list.append(left[i])
            i += 1
        while j < len(right):
            list.append(right[j])
            j += 1
        return list

a = Merge()
print(a.sortingArr([5,4,3,2,1]))