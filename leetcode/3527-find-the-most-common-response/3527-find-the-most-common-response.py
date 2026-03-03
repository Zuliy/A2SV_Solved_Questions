class Solution:
    def findCommonResponse(self, responses):
        freq = {}
        
        for day in responses:
            seen = set()
            for response in day:
                if response not in seen:
                    seen.add(response)
                    
                    if response in freq:
                        freq[response] += 1
                    else:
                        freq[response] = 1
        
        max_count = -1
        answer = ""
        
        for response in freq:
            if freq[response] > max_count:
                max_count = freq[response]
                answer = response
            elif freq[response] == max_count:
                if response < answer:
                    answer = response
        
        return answer