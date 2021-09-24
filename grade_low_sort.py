n = int(input())  # 학생수 n 입력

# 학생 정보를 압력받아 리스트 저장
array = []  # 공백 리스트 생성
for i in range(n):
    input_data = input().split()
    # 입력 형태는 이름, 점수 순으로 입력한다. 이름은 문자열 그대로, 점수는 정수형으로 변환하여 저장
    array.append((input_data[0], input_data[1]))

# 키(key)를 이용하여, 점수를 기준으로 정렬
array = sorted(array, key=lambda student: student[1])

for student in array:
    print(student[0], end=' ')
