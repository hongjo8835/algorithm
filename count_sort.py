#모든 원소의 값이 0보다 크거나 같다고 가정
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
#모든 범위를 포함하는 리스트 선언(모든 값은 0으로 초기화)
count = [0] * (max(array) + 1)

for i in range(len(array)): #count 배열에 인덱스 값에 갯수 매칭
    count[array[i]] += 1

for i in range(len(count)):
    for j in range(count[i]): #여러 개 있을 경우 반복 출력
        print(i, end=' ')