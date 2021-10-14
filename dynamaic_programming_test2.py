n = int(input())

array = list(map(int, input().split()))

d = [0] * 100  # 정답 도출을 위한 dp table 생성

d[0] = array[0]
d[1] = max(array[0], array[1])
for i in range(2, n):
    d[i] = max(d[i - 1], d[i - 2] + array[i])    # 기준점을 같게 잡아주면 합하는 수가 큰쪽 값이 선택되는 쪽의 값이 더 크다는 걸 알 수 있음.

print(d[n - 1])
