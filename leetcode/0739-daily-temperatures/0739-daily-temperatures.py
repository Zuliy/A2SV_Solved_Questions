class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        results = [0] * n  
        stack = []    
        for today_index in range(n):
            today_temp = temperatures[today_index]
            
            while stack and today_temp > temperatures[stack[-1]]:
                older_day_index = stack.pop()
                results[older_day_index] = today_index - older_day_index
            
            stack.append(today_index)
            
        return results