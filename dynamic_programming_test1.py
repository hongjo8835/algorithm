x = int(input())

d = [0] * 30001  # x의 범위가 3만 까지이다.

#  다이나믹 프로그래밍 진행 (보텀업)
for i in range(2, x + 1):
    d[i] = d[i - 1] + 1  # 프로그램 진행을 위한 첫번째 자료 집어넣기
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
    if i % 5 == 0:
        d[i] = min(d[i], d[i // 5] + 1)

print(d[x])
