class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxRight = -1
        for i in range(len(arr)-1,-1,-1):
            yeni = max(maxRight, arr[i]) 
            arr[i] = maxRight
            maxRight = yeni
        return arr