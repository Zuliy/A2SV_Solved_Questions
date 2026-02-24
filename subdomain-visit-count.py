from collections import defaultdict
from typing import List

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        count_map = defaultdict(int)
        
        for entry in cpdomains:
            count_str, domain = entry.split()
            count = int(count_str)
            
            parts = domain.split('.')
            
            # Generate all subdomains
            for i in range(len(parts)):
                subdomain = '.'.join(parts[i:])
                count_map[subdomain] += count
        
        # Format result
        result = []
        for domain, total in count_map.items():
            result.append(f"{total} {domain}")
        
        return result
