def max_prefix_sum(arr):
    current_sum = 0
    max_sum = 0
    for x in arr:
        current_sum += x
        if current_sum > max_sum:
            max_sum = current_sum
    return max_sum

t = int(input())
for _ in range(t):
    n = int(input())
    r = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))
    
    pr = max_prefix_sum(r)
    pb = max_prefix_sum(b)
    
    print(pr + pb)