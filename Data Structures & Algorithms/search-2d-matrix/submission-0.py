class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def b_search(arr, target):
            left = 0; right = len(arr)-1\
            
            while left <= right:
                mid = (left + right) // 2
                print(f"Considering left as {left} and right as {right} and mid as {mid}")
                if arr[mid] == target:
                    return mid
                elif arr[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                return -1
        
        for coll in matrix:
            res = b_search(coll, target)
            if res!= -1:
                return True
        
        return False