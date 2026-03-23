class RecentCounter:
    def __init__(self):
        self.requests = []
        self.start = 0  
    
    def ping(self, t: int) -> int:
      
        self.requests.append(t)
        
        
        while self.start < len(self.requests) and self.requests[self.start] < t - 3000:
            self.start += 1
        
        
        return len(self.requests) - self.start