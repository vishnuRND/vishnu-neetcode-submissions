import random
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def partition(arr, left, right):
            random_index = random.randint(left, right)

            arr[random_index], arr[right] = arr[right], arr[random_index]
            pivot = arr[right]

            i = left
            for j in range(left, right):
                if arr[j] < pivot:
                    arr[i], arr[j] = arr[j], arr[i]
                    i+=1
            arr[i], arr[right] = arr[right], arr[i]
            return i


        def quickSort(arr, left, right):
            if left < right:
                pivot = partition(arr, left, right)
                quickSort(arr, left, pivot-1)
                quickSort(arr, pivot+1, right)

        quickSort(nums, 0, len(nums)-1)   
        return nums   