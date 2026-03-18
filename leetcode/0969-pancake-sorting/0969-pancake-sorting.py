class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        result = []
        n = len(arr)
        
    
        for target in range(n, 1, -1):
           
            index = arr.index(target)
       
            if index == target - 1:
                continue
            
   
            if index != 0:
           
                result.append(index + 1)
     
                arr[:index + 1] = reversed(arr[:index + 1])
            
            result.append(target)
      
            arr[:target] = reversed(arr[:target])
        
        return result