array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1):  # i 부터 0까지 1씩 감소
        if array[j] < array[j - 1]:  # 비교 기준 왼쪽이 크면 자리 교체
            array[j], array[j - 1] = array[j - 1], array[j]
        else:
            break

print(array)
