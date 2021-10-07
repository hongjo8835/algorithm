#  n명의 학생 정보가 있다. 학생 정보는 학생의 이름과 학생의 성적으로 구분.
#  각 학생의 이름과 성적을 주어졌을 때 성적이 낮은 순서대로 이름으 출력.

n = int(input())

array = []
for i in range(n):
    input_data = input().split()
    array.append((input_data[0], int(input_data[1])))

array = sorted(array, key=lambda student: student[1])

for student in array:
    print(student[0], end=' ')