t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    s = input()
    

    curr = s[:k].count('W')
    ans = curr
    

    for i in range(k, n):
        if s[i] == 'W':
            curr += 1
        if s[i - k] == 'W':
            curr -= 1
        
        ans = min(ans, curr)
    
    print(ans)