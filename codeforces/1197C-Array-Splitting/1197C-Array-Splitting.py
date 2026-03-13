n, k = map(int, input().split())
a = list(map(int, input().split()))

gaps = []
for i in range(n - 1):
    gaps.append(a[i + 1] - a[i])

gaps.sort(reverse=True)

cost = a[-1] - a[0]

for i in range(k - 1):
    cost -= gaps[i]

print(cost)