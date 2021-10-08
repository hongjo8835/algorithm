n, m = list(map(int, input().split(' ')))
array = list(map(int, input().split()))

start = 0
end = max(array)

result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    for x in array:
        if x > mid:
            total += x - mid  # 잘린 떡의 길이의 합
        if total < m:  # total 이 자르려는 길이보다 작으면
            end = mid - 1
        else:
            result = mid
            start = mid + 1

print(result)
