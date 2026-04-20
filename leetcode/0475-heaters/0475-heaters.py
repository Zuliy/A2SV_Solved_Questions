import bisect

class Solution:
    def findRadius(self, houses, heaters):
        heaters.sort()
        res = 0
        
        for house in houses:
            
            i = bisect.bisect_left(heaters, house)
            
      
            left_dist = float('inf')
            if i > 0:
                left_dist = house - heaters[i - 1]
            
          
            right_dist = float('inf')
            if i < len(heaters):
                right_dist = heaters[i] - house
            
        
            min_dist = min(left_dist, right_dist)
            
           
            res = max(res, min_dist)
        
        return res