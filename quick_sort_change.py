array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort_change(array):
    # 리스트가 하나 이하의 원소만을 담고 있다면 정렬할 필요가 없음
    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]  # 피벗을 제외한 리스트

    left_side = [x for x in tail if x <= pivot]  # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot]  # 분할된 오른쪽 부분

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행, 전체 리스트 반환
    return quick_sort_change(left_side) + [pivot] + quick_sort_change(right_side)


print(quick_sort_change(array))

