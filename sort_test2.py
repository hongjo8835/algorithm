#  두 개의 배열 A,B가 있고, 두 배열은 n개의 원소로 구성, 배열의 원소는 모두 자연수
#  촤대 k번의 원소 바꿔치기를 수행가능, 최종목표는 A의 모든 원소의 합이 최대이다.
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break

print(sum(a))