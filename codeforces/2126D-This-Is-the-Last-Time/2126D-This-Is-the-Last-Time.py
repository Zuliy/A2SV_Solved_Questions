t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    
    casinos = []
    for _ in range(n):
        l, r, real = map(int, input().split())
        casinos.append((l, r, real))
    
    casinos.sort()
    
    x = k
    
    for l, r, real in casinos:
        if l <= x <= r:
            if real > x:
                x = real
    
    print(x)