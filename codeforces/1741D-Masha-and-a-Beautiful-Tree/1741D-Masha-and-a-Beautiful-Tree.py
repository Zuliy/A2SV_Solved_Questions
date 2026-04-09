import sys
sys.setrecursionlimit(1 << 20)

def solve(p):
    n = len(p)
    
    def dfs(l, r):
        if l == r:
            return 0, p[l], p[l]  
        
        mid = (l + r) // 2
        left_ops, left_min, left_max = dfs(l, mid)
        right_ops, right_min, right_max = dfs(mid + 1, r)
        
        if left_ops == -1 or right_ops == -1:
            return -1, 0, 0
        
    
        if left_max < right_min:
            return left_ops + right_ops, left_min, right_max
     
        elif right_max < left_min:
            return left_ops + right_ops + 1, right_min, left_max
      
        else:
            return -1, 0, 0
    
    ops, _, _ = dfs(0, n - 1)
    return ops


t = int(input())
for _ in range(t):
    m = int(input())
    p = list(map(int, input().split()))
    print(solve(p))