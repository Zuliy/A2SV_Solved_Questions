t = int(input())

for _ in range(t):
    s = input().strip()
    
    working = set()
    i = 0
    n = len(s)
    
    while i < n:
        j = i
        
        while j < n and s[j] == s[i]:
            j += 1
        
        length = j - i
        
        if length % 2 == 1:
            working.add(s[i])
        
        i = j
    
    res = ''.join(sorted(working))
    print(res)