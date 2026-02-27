t = int(input())

for _ in range(t):
    n = int(input())
    s = input().strip()
    
    ans = float('inf')
    
    for i in range(n):
        
        # length 2
        if i + 1 < n:
            a = b = c = 0
            for ch in s[i:i+2]:
                if ch == 'a':
                    a += 1
                elif ch == 'b':
                    b += 1
                else:
                    c += 1
            if a > b and a > c:
                ans = min(ans, 2)
        
        # length 3
        if i + 2 < n:
            a = b = c = 0
            for ch in s[i:i+3]:
                if ch == 'a':
                    a += 1
                elif ch == 'b':
                    b += 1
                else:
                    c += 1
            if a > b and a > c:
                ans = min(ans, 3)
        
        # length 4
        if i + 3 < n:
            a = b = c = 0
            for ch in s[i:i+4]:
                if ch == 'a':
                    a += 1
                elif ch == 'b':
                    b += 1
                else:
                    c += 1
            if a > b and a > c:
                ans = min(ans, 4)
    
    if ans == float('inf'):
        print(-1)
    else:
        print(ans)
