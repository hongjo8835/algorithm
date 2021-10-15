n = int(input())

d = [0] * 1001

d[1] = 1
d[2] = 3

for i in range(3, n + 1):
    d[i] = (d[i - 1] + 2 * d[i - 2]) % 796796  # 기준점 아래로 점화식이 세워진다.

print(d[n])
